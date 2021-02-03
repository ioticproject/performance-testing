import pytest
from utils import SharedValues
from utils import template_get, template_post
from config import (
    payload_client_account,
    HEALTH_URL,
    USER_LOGIN_URL,
    GET_USERS_URL,
    ADD_USER_URL,
    DELETE_USER_URL,
    UPDATE_USER_URL,
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


def test_health():
    template_get(HEALTH_URL,
                 'health',
                 SharedValues.access_token)

    assert True


def test_login():
    json_path = str('test/helper_jsons/user_credentials.json')
    template_post(USER_LOGIN_URL,
                  'user_login',
                  json_path=json_path)

    assert True


def test_get_users():
    json_path = str('test/helper_jsons/admin_credentials.json')
    template_post(GET_USERS_URL,
                  'get_users',
                  json_path=json_path)

    assert True


def test_add_user():
    json_path = str('test/helper_jsons/new_user_credentials.json')
    template_post(ADD_USER_URL,
                  'add_user',
                  json_path=json_path)

    assert True
