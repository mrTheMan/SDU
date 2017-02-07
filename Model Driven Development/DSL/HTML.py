

class HTML():

    def __init__(self):
        self.script = []
        self.script.append(self.__class__.__name__)

    def HEAD(self):
        self.script.append(HEAD().head)
        return self

    def BODY(self):
        self.script.append(BODY().body)
        return self

    def PrintScript(self):
        print(self.script)

class BODY():

    def __init__(self):
        self.body = []
        self.body.append(self.__class__.__name__)

class HEAD():

    def __init__(self):
        self.head = []
        self.head.append(self.__class__.__name__)