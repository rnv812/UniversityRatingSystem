import os
from typing import Optional

import requests as rq


EMPLOYEES_API_URL = os.getenv('EMPLOYEES_API_URL')
EMPLOYEES_MOCK_API_URL = os.getenv('EMPLOYEES_MOCK_API_URL')


def query_employee_data(employee_id: str) -> Optional[dict]:
    """Fetch information about employee from api by his employee id."""
    try:
        url = f'{EMPLOYEES_API_URL}/endpoint/'
        response = rq.get(url, params={'employee_id': employee_id})
        return response.json()
    except rq.exceptions.RequestException:
        return None


def query_mock_employee_data(employee_id: str) -> Optional[dict]:
    return {
        "fullName": "Кузнецов Михаил Андреевич",
        "qualificationName": "Доцент",
        "departmentName": "ЭВМиС",
    }
