from kombu import Exchange, Queue, message
import time


class AuthServer(object):
    _processing = True

    def __init__(self, backend, channel, exchange_name):
        self._exchange = Exchange(name=exchange_name, channel=channel)
        self.queue = Queue(exchange_name + '_queue', self._exchange)
        self._bound_queue = self.queue(channel)
        self._bound_queue.declare()

        self._channel = channel
        self._auth_backend = backend

    def run(self):
        while self._processing:
            request = self._bound_queue.get()
            self._auth_process(request)
            time.sleep(5)

    def _auth_process(self, request):
        if not isinstance(request, message.Message):
            pass
        else:
            headers = request.headers
            if not 'action' in headers:
                pass

            action = headers['action']
            print action

            if action == 'login':
                username = headers['username']
                password = headers['password']
                result = self._auth_backend.login(username, password)
                return result

            elif action == 'check_vhost':
                if self._auth_backend.check_vhost(headers['username'], headers['vhost']):
                    return 'allow'
                else:
                    return 'deny'

    def terminate(self):
        self._processing = False

    def close(self):
        self._bound_queue.close()
