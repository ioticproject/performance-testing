import pytest
from utils import template_get, template_post, HTTPClient
from config import (
    GET_SENSORS_URL,
    ADD_SENSORS_URL,
    GET_USER_SENSORS_URL,
    GET_SENSOR_URL,
    GET_DEVICE_SENSORS_URL,
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


def test_get_sensors():
    template_get(GET_SENSORS_URL,
                 'get_sensors',
                 access_token=HTTPClient.admin_access_token)

    assert True


def test_get_sensor():
    template_get(GET_SENSOR_URL.format(USER_ID=HTTPClient.global_id,
                                       DEVICE_ID=HTTPClient.global_device_id,
                                       ID=HTTPClient.global_sensor_id),
                 'get_sensor',
                 access_token=HTTPClient.global_access_token)

    assert True


def test_get_user_sensors():
    template_get(GET_USER_SENSORS_URL.format(USER_ID=HTTPClient.global_id),
                 'get_user_sensors',
                 access_token=HTTPClient.global_access_token)

    assert True


def test_get_device_sensors():
    template_get(GET_DEVICE_SENSORS_URL.format(USER_ID=HTTPClient.global_id,
                                               DEVICE_ID=HTTPClient.global_device_id),
                 'get_device_sensors',
                 access_token=HTTPClient.global_access_token)

    assert True


def test_add_sensor():
    json_path = str('test/helper_jsons/new_sensor.json')
    template_post(ADD_SENSORS_URL.format(USER_ID=HTTPClient.global_id,
                                         DEVICE_ID=HTTPClient.global_device_id),
                  'add_sensor',
                  json_path=json_path)

    assert True
