

class TV():

    channel = 0
    state = 0
    volume = 20

    def __init__(self):
        self.channel = 0
        self.state = 0
        self.volume = 20

    def poweroN(self):
        self.state = 1
        self.channel = 1
        return self

    def powerofF(self):
        self.state = 0
        self.channel = 0
        self.volume = 20
        return self

    def channeluP(self):
        if self.channel <= 100 and self.state != 0:
            self.channel = self.channel + 1
        return self

    def channeldowN(self):
        if self.channel > 0 and self.state != 0:
            self.channel = self.channel - 1
        return self

    def ChannelSet(self, channel):
        if channel >= 0 and channel <= 100 and self.state != 0:
            self.channel = channel
        return self

    def volumeuP(self):
        if self.volume < 100 and self.state != 0:
            if(self.volume + 2) > 100:
                self.volume = 100
            else:
                self.volume = self.volume + 2
        return self

    def volumedowN(self):
        if self.volume > 0 and self.state != 0:
            if (self.volume - 2) < 0:
                self.volume = 0
            else:
                self.volume = self.volume - 2
        return self

    def VolumeSet(self, volume):
        if volume >= 0 and volume <= 100 and self.state != 0:
            self.volume = volume

        return self

    def prinT(self):
        print("Channel: " + str(self.channel))
        if self.state == 0:
            print("State: OFF")
        else:
            print("State: ON")

        print("Volume: " + str(self.volume))
        print("")
        return self


    def __getattr__(self, item):

        method_list = [func for func in dir(TV) if callable(getattr(TV, func)) and not func.startswith("__")]


        for s in method_list:
            if s.lower() == item.lower():
                method = getattr(self, s)
                method()

        print("")

        return self

TV = TV()


{

    TV.PowerOn.
            ChannelSet(34).
            VolumeSet(56).
        Print

}


