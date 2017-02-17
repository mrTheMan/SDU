
class HTML():

    def __init__(self):
        self.script = []
        self.script.append(self.__class__.__name__)
        self.values = []

    def HEAD(self):
        self.script.append("HEAD")
        return self

    def BODY(self):
        self.script.append("BODY")
        return self

    def TITLE(self, title):
        self.script.append("TITLE")
        self.values.append(["TITLE",title])
        return self

    def DIV(self):
        self.script.append("DIV")
        return self

    def P(self, text):
        self.script.append("P")
        self.values.append(["P", text])
        return self

    def PrintScript(self):

        # start HTML tag
        print("<" + self.script[0] + ">")

        # HEAD
        c = 0
        for tag in self.script:
            if tag == "BODY":
                break
            if tag != "HTML":
                print("<" + tag + ">")
                for v in self.values:
                    if v[0] == tag:
                        print(v[1])
            c = c + 1

        c = c - 1
        while(c != 0):
            print("</" + self.script[c] + ">")
            c = c -1
        # END HEAD


        # BODY
        c = 0
        flag_after_head = 0
        for tag in self.script:
            if tag == "BODY":
                flag_after_head = 1
            if(flag_after_head == 1 and (tag == "BODY" or tag != "HTML")):
                print("<" + tag + ">")
                for v in self.values:
                    if v[0] == tag:
                        print(v[1])
            c = c + 1

        c = c - 1
        while (c != 0):
            if self.script[c] == "BODY":
                print("</" + self.script[c] + ">")
                break
            print("</" + self.script[c] + ">")
            c = c - 1

        # END BODY
        print("</" + self.script[0] + ">")
        #END HTML

{

    HTML().
        HEAD().
            TITLE("This is my title").
        BODY().
            DIV().
                P("My first website").
            DIV().
                P("My second website").PrintScript()

}
