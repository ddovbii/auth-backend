import kombu
from auth_server import AuthServer

if __name__ == '__main__':
    exchange = 'authentication'

    conn = kombu.Connection()
    ch = conn.channel()

    auth = AuthServer('', ch, exchange)
    auth.run()
