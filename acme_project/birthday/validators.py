from datetime import date

from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    if 1 > age or 120 < age:
        raise ValidationError('Ожидается возраст от 1 года до 120 лет')
