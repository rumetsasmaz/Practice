class BaseModule:
    def __init__(self , target):
        self.target = target

    def run(self):

        raise NotImplementedError
    