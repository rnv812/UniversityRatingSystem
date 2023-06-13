from dataclasses import dataclass
from typing import Optional

from ..educators.models import Educator, Qualification
from ..departments.models import Department


@dataclass
class UserData:
    """Class for keeping data for filling user extra data on save"""
    first_name: str
    last_name: str
    patronymic: str


@dataclass
class EducatorData:
    """Class for keeping data for creating educator for user on save"""
    qualification: Qualification
    department: Department


def construct_user_data(employee_data: dict) -> Optional[UserData]:
    """Construct UserData dataclass instance using data
    received from employee server.
    """
    dependent_fields = ['fullName', ]

    for field in dependent_fields:
        if field not in employee_data:
            return None

    [last_name, first_name, *patronymic] = employee_data['fullName'].split(' ')
    patronymic = patronymic[0] if patronymic else ''

    return UserData(first_name, last_name, patronymic)


def construct_educator_data(employee_data: dict) -> Optional[EducatorData]:
    """Construct EducatorData dataclass instance using data
    received from employee server.
    """
    dependent_fields = ['departmentName', 'qualificationName']

    for field in dependent_fields:
        if field not in employee_data:
            return None

    try:
        department = Department.objects.get(
            name=employee_data['departmentName']
        )
    except Department.DoesNotExist:
        return None

    try:
        qualification = Qualification.objects.get(
            name=employee_data['qualificationName']
        )
    except Qualification.DoesNotExist:
        return None

    return EducatorData(qualification, department)


def create_educator_hook(user, qualification, department):
    Educator.objects.create(
        user=user,
        qualification=qualification,
        department=department,
    )
