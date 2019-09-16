from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class Authentication:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD
    """

    @staticmethod
    def authenticate(username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def has_perm(user_obj, perm, obj=None):
        return user_obj.username == settings.ADMIN_LOGIN
