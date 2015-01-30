import kombu


if __name__ == '__main__':

    conn = kombu.Connection(userid='guest', password='guest1')

    queue = conn.SimpleQueue('myqueue')
    queue.put('sdfsd')

    conn.close()