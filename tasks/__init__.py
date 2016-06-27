import digdag
import os

class MyWorkflow(object):
    def __init__(self):
        pass

    def loadEnv(self, session_time = None):
        digdag.env.store({"AWS_ACCESS_KEY":os.environ.get("AWS_ACCESS_KEY_ID")})
        digdag.env.store({"AWS_SECRET_KEY":os.environ.get("AWS_SECRET_ACCESS_KEY")})

