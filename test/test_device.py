import pytest
from utils import template_get, template_post, HTTPClient
from config import (
    GET_DEVICES_URL,
    ADD_DEVICE_URL,
    GET_USER_DEVICES_URL,
    GET_DEVICE_URL,
    rq_per_s, time_per_rq, time_per_rq_c,
    transfer_rate,
    connect_time, processing_time, waiting_time,
    failed_rq,
    reqs
)


@pytest.fixture(autouse=True)
def run_before_tests():
    rq_per_s.clear()
    time_per_rq.clear()
    time_per_rq_c.clear()
    transfer_rate.clear()
    connect_time.clear()
    processing_time.clear()
    waiting_time.clear()
    failed_rq.clear()
    reqs.clear()


def test_get_devices():
    template_get(GET_DEVICES_URL.format(USER_ID=HTTPClient.global_id),
                 'get_devices',
                 access_token=HTTPClient.admin_access_token)

    assert True


def test_get_device():
    template_get(GET_DEVICE_URL.format(USER_ID=HTTPClient.global_id,
                                       ID=HTTPClient.global_device_id),
                 'get_device',
                 access_token=HTTPClient.global_access_token)

    assert True


def test_get_user_devices():
    template_get(GET_USER_DEVICES_URL.format(USER_ID=HTTPClient.global_id),
                 'get_user_devices',
                 HTTPClient.global_access_token)

    assert True


def test_add_device():
    json_path = str('test/helper_jsons/new_device.json')
    template_post(ADD_DEVICE_URL.format(USER_ID=HTTPClient.global_id),
                  'add_device',
                  json_path=json_path,
                  access_token=HTTPClient.global_access_token)

    assert True
