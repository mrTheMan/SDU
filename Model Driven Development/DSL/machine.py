
class state():
    name = ""
    transition = []
    def __init__(self, name):
        self.name = name
        self.transition = []

    def setTransition(self, transition):
        self.transition.append(transition)

class transition():
    end = ""
    def __init__(self, end):
        self.end = end

class variable():
    name = ""
    value = 0
    min_value = 0
    max_value = 0

    def __init__(self,name, min, max):
        self.name = name
        self.min_value = min
        self.max_value = max

    def increase(self):
        if self.value < self.max_value:
            self.value += 1
    def decrease(self):
        if self.value > self.min_value:
            self.value -= 1

class machine():

    current_count = -1
    list_state = []
    list_var = []
    name = ""
    state = state("")


    def name(self, name ):
        self.name = name
        return self

    def state_add(self, name):
        newState = state(name)
        self.list_state.append(newState)

        if self.state.name == "":
            self.state = newState

        self.current_count += 1
        return self

    def transition(self, end):
        newTransition = transition(end)
        self.list_state[self.current_count].setTransition(newTransition)
        return self

    def execute(self,execute_list):

        for i in range(len(execute_list)):
            for j in self.list_state:
                if execute_list[i] == j.name:
                    self.changestate(j)
                    break

            for k in self.list_var:
                if execute_list[i].lower() == k.name.lower():
                    if execute_list[i+1].lower() == "up":
                        print("Variable " + k.name + " changed from " + str(k.value) + " to " + str(k.value + 1))
                        k.increase()
                    elif execute_list[i+1].lower() == "down":
                        print("Variable " + k.name + " changed from " + str(k.value) + " to " + str(k.value - 1))
                        k.decrease()

                    i += 1
                    break

        return self

    def changestate(self, new_state):
        for i in self.state.transition:
            if i.end.lower() == new_state.name.lower():
                print("Transition from " + self.state.name + " to " + new_state.name)
                self.state = new_state

    def variable(self,name, min,max):
        newVar = variable(name,min,max)
        self.list_var.append(newVar)
        return self

    def print(self):
        print(self.name)
        for v in self.list_var:
            print("Variable " + v.name + " Min: " + str(v.min_value) + " Max: " + str(v.max_value) + " Value: " + str(v.value) )

        for i in self.list_state:
            print("State: " + i.name)
            for j in i.transition:
                print("Transition: " + i.name + " " + j.end)



TV = machine()

{
    TV.name("TV").
        variable("Volume",0,100).
        variable("Channel",0,100).
            state_add("ON").
                transition("OFF").
            state_add("OFF").
                transition("ON").
                transition("NONE").
            state_add("NONE")

}


print(TV.name)

print("")

#TV.execute(["ON", "OFF", "OFF", "OFF", "NONE"])

TV.execute(["ON", "OFF", "ON","Channel", "UP","Volume", "UP", "Volume", "UP", "Volume", "DOWN", "NONE", "OFF", ])

print("")




