from datetime import datetime


class RequestContext(object):
    def __init__(self, logged_in_user=None):
        self.logged_in_user = logged_in_user
        self.now = datetime.now()
