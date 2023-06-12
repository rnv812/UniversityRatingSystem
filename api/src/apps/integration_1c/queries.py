import os
from typing import Optional

import requests as rq


EMPLOYEES_API_URL = os.getenv('EMPLOYEES_API_URL')

_api_auth_username = os.getenv('EMPLOYEES_API_USERNAME')
_api_auth_password = os.getenv('EMPLOYEES_API_PASSWORD')

_HEADERS = {
    'Authorization': f"Basic {_api_auth_username}:{_api_auth_password}"
}


def query_employee_data(employee_id: str) -> Optional[dict]:
    """Fetch information about employee from api by his employee id."""
    try:
        url = f'{EMPLOYEES_API_URL}/RATING/hs/educatorData/{employee_id}/'
        response = rq.get(url, headers=_HEADERS)
        return response.json()
    except rq.exceptions.RequestException:
        return None


def query_mock_employee_data(employee_id: str) -> Optional[dict]:
    return {
        "fullName": "Кузнецов Михаил Андреевич",
        "qualificationName": "Доцент",
        "departmentName": "ЭВМиС",
    }
