import matplotlib.pyplot as plt
import re
import requests
import subprocess
from http import HTTPStatus

from config import (
    C, N,
    LOGGER,
    rq_range, concurency_range,
    reqs,
    rq_per_s,
    time_per_rq, time_per_rq_c,
    transfer_rate,
    connect_time,
    processing_time, waiting_time,
    failed_rq,
    AUTH_URL,
    payload_admin_account
)

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_access_token():
    url = AUTH_URL
    headers = {'Content-Type': 'application/json'}
    
    LOGGER.info("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n")
    LOGGER.info(payload_admin_account)

    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        data=payload_admin_account
    )
    
    LOGGER.info(str(response.json()))
    
    if response.status_code != 200:
        LOGGER.critical('POST status code = ' + str(response.status_code))
        return

    SharedValues.access_token = response.json()['access_token']
    LOGGER.info('Got the intra access token: ' + SharedValues.access_token)


class SharedValues:
    access_token = None


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
        cmd = [
            'ab',
            '-m', method,
            '-c', concurrency,
            '-n', req_num,
            '-H', '\"Authorization: jwt ' + access_token + '\"',
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
            cmd += ['-H', '\"Authorization: jwt ' + access_token + '\"']

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


def template_get(url, plot_title, access_token):
    payload = {}
    header = {'Authorization': 'jwt ' + access_token}

    response = requests.request(
        method='GET',
        url=url,
        headers=header,
        data=payload
    )

    if response.status_code != 200:
        LOGGER.info(str(response.status_code))
        LOGGER.info(response.text)
        LOGGER.info("***************************")
        LOGGER.info(url)
        
        
        
        LOGGER.critical('GET status code = ' + str(response.status_code))
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
