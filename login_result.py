class LoginResult(object):
    def __init__(self, success, tags=[]):
        self.success = success
        self.tags = tags

    def is_success(self):
        return self.success

    def set_success(self, success):
        self.success = success

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def __str__(self):
        if self.success:
            result = ''
            for tag in self.tags:
                result += result + tag + ', '

            return result

        else:
            return 'refused'
