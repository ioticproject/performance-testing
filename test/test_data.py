import pytest
from utils import template_get, template_post, HTTPClient
from config import (
    GET_DATA_URL,
    ADD_DATA_URL,
    GET_SENSOR_DATA_URL,
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


def test_get_data():
    template_get(GET_DATA_URL,
                 'get_data',
                 access_token=HTTPClient.admin_access_token)

    assert True


def test_get_sensor_data():
    template_get(GET_SENSOR_DATA_URL.format(USER_ID=HTTPClient.global_id,
                                            DEVICE_ID=HTTPClient.global_device_id,
                                            SENSOR_ID=HTTPClient.global_sensor_id),
                 'get_sensor_data',
                 access_token=HTTPClient.global_access_token)

    assert True


def test_add_data():
    json_path = str('test/helper_jsons/new_data.json')
    template_post(ADD_DATA_URL.format(USER_ID=HTTPClient.global_id,
                                      DEVICE_ID=HTTPClient.global_device_id,
                                      SENSOR_ID=HTTPClient.global_sensor_id),
                  'add_data',
                  json_path=json_path)

    assert True
