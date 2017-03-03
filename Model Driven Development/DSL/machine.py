
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
    events = []

    def __init__(self, end):
        self.end = end

    def addEvent(self, event):
        self.events.append(event)

class event():
    transition = ""
    variable = ""
    value = 0

    def __init__(self,transition, variable, value):
        self.transition = transition
        self.variable = variable
        self.value = value

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
    def setVariable(self, value):
        if self.value > self.min_value and self.value < self.max_value:
            self.value = value

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

    def variable(self, name, min, max):
        newVar = variable(name,min,max)
        self.list_var.append(newVar)
        return self

    def addEvent(self,transition, variable, value):
        index = (len(self.state.transition) -1)
        newEvent = event(transition,variable,value)
        self.state.transition[index].addEvent(newEvent)
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
                for event in i.events:
                    if event.transition == i.end:
                        for v in self.list_var:
                            if v.name == event.variable:
                                print("Variable " + v.name + " changed from " + str(v.value) + " to " + str(event.value))
                                v.setVariable(event.value)

                self.state = new_state


class interperter():
    stm = 0

    def __init__(self, statemachine):
        self.stm = statemachine


    def print(self):
        print(self.stm.name)
        print("Current state: " + self.stm.state.name)
        for v in self.stm.list_var:
            print("Variable " + v.name + " Min: " + str(v.min_value) + " Max: " + str(v.max_value) + " Value: " + str(
                v.value))

        for i in self.stm.list_state:
            print("State: " + i.name)
            for j in i.transition:
                print("Transition: " + i.name + " " + j.end)

class querybuilder():

    query = []

    def changeStateTo(self, name):
        self.query.append(name)
        return self

    def incrementVariable(self, var):
        self.query.append(var)
        self.query.append("up")
        return self

    def decrementVariable(self, var):
        self.query.append(var)
        self.query.append("down")
        return self

    def print(self):
        return self.query



TV = machine()

{
    TV.name("TV").
        variable("Volume",0,100).
        variable("Channel",0,100).
            state_add("ON").
                transition("OFF").
                    addEvent("OFF","Volume", 0).
                    addEvent("OFF","Channel", 0).
            state_add("OFF").
                transition("ON")

}


print(TV.name)

print(interperter(TV).print())

print("")

TV.execute(querybuilder().changeStateTo("OFF").changeStateTo("ON").incrementVariable("Volume").query)


print("")

print(interperter(TV).print())