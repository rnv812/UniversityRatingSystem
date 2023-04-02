from datetime import datetime
from typing import Any

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


VSTU_FOUNDATION_YEAR = 1930


class ValidRatingYearField(models.PositiveIntegerField):
    """Custom field for models representing year of report
    Includes validators:
        - minimal year: 1930 (vstu foundation year)
        - maximum year: current year
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs['validators'] = [
            MinValueValidator(VSTU_FOUNDATION_YEAR),
            MaxValueValidator(datetime.now().year)
        ]
        super().__init__(*args, **kwargs)
