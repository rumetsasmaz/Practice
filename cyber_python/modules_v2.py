import socket

class BaseModule:

    def __init__(self , target, timeout=1):
        self.target = target


    def run(self):

        raise NotImplementedError()






if __name__ == "__main__":

    BaseModule("x").run()