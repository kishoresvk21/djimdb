import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
# def user_name_validator(user_name):
#     if re.match('^[a-zA-Z0-9]+([_]?[a-zA-Z0-9])*$',user_name):
#         return True
#     else:
#         raise ValueError(_('Invalid Username'))

class DomainUnicodeusernameValidator(UnicodeUsernameValidator):
    regex=r'^[a-zA-Z0-9]+([_]?[a-zA-Z0-9])*$'
    message=_(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and _ characters.'
    )

class DomainUnicodenameValidator(UnicodeUsernameValidator):
    regex=r'^[a-zA-Z]+([\s]?[a-zA-Z])*$'
    message=_(
        'Enter a valid name. This value may contain only characters.'
    )

class DomainUnicodemobileValidator(UnicodeUsernameValidator):
    regex=r'^[0-9]+$'
    message = _(
        'Enter a valid number. This value may contain only numbers and length should be 10.'
    )
