import re
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    # Регулярное выражение для валидации номера телефона (базовый пример)
    pattern = "^[+]{1}7 [(]{1}[0-9]{3}[)]{1} [0-9]{3} [0-9]{4}$"
    if not re.match(pattern, value):
        raise ValidationError(
            f'Проверьте правильность номера',
            params={'value': value},
        )
