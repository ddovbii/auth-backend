from login_result import LoginResult


class AuthBackend(object):
    ACCEPTED = LoginResult(True, ['administrator'])
    REFUSED = LoginResult(False)

    def login(self, username, password=''):
        if username == 'murano' and password == 'murano':
            return self.ACCEPTED

        return self.REFUSED

    def check_vhost(self, username, vhost):
        return vhost == '/'
