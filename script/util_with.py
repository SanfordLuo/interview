"""
上下文管理器
"""


class MyShell(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            self.session.rollback()
        else:
            self.session.commit()
