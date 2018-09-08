from apiapp.models import User


class AbstractVoter:

    request = None

    def __init__(self, request):
        self.request = request

    def is_logged_in(self):
        if isinstance(self.request.user, User):
            return True

        return False

    def is_superuser(self):
        if self.is_logged_in():
            return self.request.user.is_superuser

        return False


class UserVoter(AbstractVoter):

    def user_can_manage_me(self, user_inst: User):
        if self.is_logged_in():
            if self.is_superuser():
                return True
            if self.request.user == user_inst:
                return True

        return False
