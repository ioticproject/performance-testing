import random
import re
import string
import subprocess
from http import HTTPStatus

import matplotlib.pyplot as plt


import random
import string
from http import HTTPStatus

import requests
from config import (AUTH_URL, LOGGER, payload_admin_account,
                    C, N, rq_range, rq_per_s, reqs, concurency_range,
                    time_per_rq, time_per_rq_c,
                    transfer_rate, connect_time,
                    processing_time, waiting_time, failed_rq)



class HTTPClient:
    access_token = None
    global_access_token = None

    def generate_access_token(username=None, password=None):
        url = AUTH_URL
        headers = {'Content-Type': 'application/json'}

        if username and password:
            payload_json = {
                "username": username,
                "password": password
            }
            payload = str(payload_json).replace("\'", "\"")

            response = requests.request(
                method='POST',
                url=url,
                headers=headers,
                data=payload
            )

            if response.status_code != HTTPStatus.OK:
                LOGGER.critical('POST status code = ' + str(response.status_code))
                return

            HTTPClient.global_access_token = "jwt " + response.json()['access_token']
            LOGGER.info('Got the user access token: ' + HTTPClient.global_access_token)

        payload = payload_admin_account
        response = requests.request(
                method='POST',
                url=url,
                headers=headers,
                data=payload
            )
        if response.status_code != HTTPStatus.OK:
            LOGGER.critical('POST status code = ' + str(response.status_code))
            return

        HTTPClient.admin_access_token = "jwt " + response.json()['access_token']
        LOGGER.info('Got the ADMIN access token: ' + HTTPClient.admin_access_token)


    def template_get(url, headers, payload, need_access_token=False):
        response = requests.request("GET", url, headers=headers, data=payload)
        # print("**********************************************************")
        # print(response.text)
        assert (
            response.status_code == HTTPStatus.OK
            or response.status_code == HTTPStatus.CREATED
        )
        ret = response

        if need_access_token:
            del headers["Authorization"]
            response = requests.request("GET",
                                        url=url,
                                        headers=headers,
                                        data=payload)
            assert response.status_code == HTTPStatus.UNAUTHORIZED

            headers["Authorization"] = Utils.get_random_token()
            response = requests.request("GET",
                                        url=url,
                                        headers=headers,
                                        data=payload)
            assert response.status_code == HTTPStatus.UNAUTHORIZED

        return ret


    def template_get_bad_request(url, headers, payload):
        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        return response


    def template_post(url, headers, payload, need_access_token=False):
        response = requests.request("POST", url, headers=headers, data=payload)
        # print("**********************************************************")
        # print(response.text)
        assert (
            response.status_code == HTTPStatus.OK
            or response.status_code == HTTPStatus.CREATED
        )
        ret = response

        if need_access_token:
            del headers["Authorization"]
            response = requests.request("POST",
                                        url=url,
                                        headers=headers,
                                        data=payload)

            assert response.status_code == HTTPStatus.UNAUTHORIZED

            headers["Authorization"] = Utils.get_random_token()
            response = requests.request("POST",
                                        url=url,
                                        headers=headers,
                                        data=payload)

            assert response.status_code == HTTPStatus.UNAUTHORIZED

        return ret


    def template_post_bad_request(url, headers, payload):
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        return response


    def template_post_unauthorized(url, headers, payload):
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == HTTPStatus.UNAUTHORIZED

        return response


class Utils:

    @staticmethod
    def get_random_string(length):
        """
        Generates random string from ascii_lowercase set.
        ::length:: The length od the generated sequence. [int]
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))


    @staticmethod
    def get_random_token():
        """
        Generates random token with {TOKEN_LENGTH} length.
        This should be used as a dummy authentication token
        """
        TOKEN_LENGTH = 256
        return "jwt" + Utils.get_random_string(TOKEN_LENGTH)


    def replace_key_in_json(json, key, val):
        if isinstance(json, dict):
            for k, v in json.items():
                if k == key:
                    json[k] = val
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        v[i] = self.replace_key_in_json(item, key, val)
                elif isinstance(v, dict):
                    v = self.replace_key_in_json(v, key, val)
        return json


    def remove_key_from_json(input_dict, keys):
        if isinstance(input_dict, dict):
            return {
                k: self.remove_key_from_json(v, keys)
                for k, v in input_dict.items()
                if k not in keys
            }

        elif isinstance(input_dict, list):
            return [self.remove_key_from_json(element, keys) for element in input_dict]

        else:
            return input_dict


def avg(lst):
    return sum(lst) / len(lst)


def draw_plot(plot_title):
    LOGGER.info("Drawing plot " + plot_title)

    # only for debugging
    LOGGER.info("reqs " + str(reqs))
    LOGGER.info("rq per s " + str(rq_per_s))
    LOGGER.info("time per rq " + str(time_per_rq))
    LOGGER.info("time per rq c " + str(time_per_rq_c))
    LOGGER.info("transfer rate " + str(transfer_rate))

    plt.clf()
    plt.title('Statistics ' + plot_title)

    plt.subplot(2, 2, 1)
    plt.plot(reqs, rq_per_s, label="Requests/s [#/sec]")
    plt.xlabel('Time [s]')
    plt.ylabel('Requests/s')

    plt.subplot(2, 2, 2)
    plt.plot(reqs, time_per_rq, label="Time/Request concurrency [ms]")
    plt.xlabel('Num Requests')
    plt.ylabel('Time/Request [ms]')

    plt.subplot(2, 2, 3)
    plt.plot(reqs, time_per_rq_c, label="Time/Request [ms]")
    plt.xlabel('Num Requests')
    plt.ylabel('Time/Request concurrency [ms]')

    plt.subplot(2, 2, 4)
    plt.plot(reqs, transfer_rate, label="Transfer Rate [Kbytes/sec]")
    plt.xlabel('Time [s]')
    plt.ylabel('Transfer Rate [Kbytes/sec]')

    plt.tight_layout()

    plt.savefig('graphics/' + plot_title)

    LOGGER.info("Avg connection time: " + str(avg(connect_time)) + "[ms]")
    LOGGER.info("Avg processing time: " + str(avg(processing_time)) + "[ms]")
    LOGGER.info("Avg waiting time: " + str(avg(waiting_time)) + "[ms]")
    LOGGER.info("Failed requests: " + str(int(avg(failed_rq))))


def generate_ab_command(method, url, access_token=None,
                        json_path=None, content_type=None):
    concurrency = str(C)
    req_num = str(N)

    if method == 'GET':
        if access_token == None:
            access_token = ''

        cmd = [
            'ab',
            '-m', method,
            '-c', concurrency,
            '-n', req_num,
            '-H', 'Authorization: ' + access_token,
            url
        ]

    elif method == 'POST':
        cmd = [
                'ab',
                '-c', concurrency,
                '-n', req_num
            ]

        if json_path:
            cmd += ['-p', json_path]

        if access_token:
            cmd += ['-H', 'Authorization: ' + access_token]

        cmd += [
                '-T', content_type,
                url
                ]

    return cmd


def parse_result(res):
    for i in range(len(res.splitlines())):
        line = str(res.splitlines()[i])

        if 'Requests per second:' in line:
            rq_per_s.append(float(re.findall(r"\d+\.\d+", line)[0]))
        elif 'Time per request:' in line:
            if 'concurrent' in line:
                time_per_rq_c.append(float(re.findall(r"\d+\.\d+", line)[0]))
            else:
                time_per_rq.append(float(re.findall(r"\d+\.\d+", line)[0]))
        elif 'Transfer rate:' in line:
            transfer_rate.append(float(re.findall(r"\d+\.\d+", line)[0]))
        elif 'Connect:' in line:
            connect_time.append(float(re.findall(r"\d+", line)[1]))
        elif 'Processing:' in line:
            processing_time.append(float(re.findall(r"\d+", line)[1]))
        elif 'Waiting:' in line:
            waiting_time.append(float(re.findall(r"\d+", line)[1]))
        elif 'Failed requests:' in line:
            failed_rq.append(int(re.findall(r"\d+", line)[0]))


def template_get(url, plot_title, access_token=None):
    payload = {}
    header = {}
    if access_token:
        header['Authorization'] = access_token

    response = requests.request(
        method='GET',
        url=url,
        headers=header,
        data=payload
    )

    if response.status_code != 200:
        LOGGER.critical('GET status code = ' + str(response.status_code) + response.text)
        assert False

    for idx in range(int(len(rq_range))):
        N = rq_range[idx]
        C = concurency_range[idx]
        reqs.append(N)
        LOGGER.info("Send " + str(N) + ' requests, concurrency ' + str(C))

        cmd = generate_ab_command(method='GET',
                                  url=url,
                                  access_token=access_token)
        res = subprocess.run(cmd, capture_output=True).stdout
        parse_result(res)

    draw_plot(plot_title)


def template_post(url, plot_title, json_path=None, access_token=None):
    content_type = 'application/json'

    for idx in range(len(rq_range)):
        N = rq_range[idx]
        reqs.append(N)

        cmd = generate_ab_command(method='POST',
                                  url=url,
                                  json_path=json_path,
                                  content_type=content_type,
                                  access_token=access_token)
        res = subprocess.check_output(cmd, shell=False)
        parse_result(res)

    draw_plot(plot_title)
