

class TV():

    channel = 0
    state = 0
    volume = 20

    def __init__(self):
        self.channel = 0
        self.state = 0
        self.volume = 20

    def PowerOn(self):
        self.state = 1
        self.channel = 1
        return self

    def PowerOff(self):
        self.state = 0
        self.channel = 0
        self.volume = 20
        return self

    def ChannelUp(self):
        if self.channel <= 100:
            self.channel = self.channel + 1
        return self

    def ChannelDown(self):
        if self.channel > 0:
            self.channel = self.channel - 1
        return self

    def ChannelSet(self, channel):
        if channel >= 0 and channel <= 100:
            self.channel = channel
        return self

    def VolumeUp(self):
        if self.volume < 100:
            if(self.volume + 2) > 100:
                self.volume = 100
            else:
                self.volume = self.volume + 2
        return self

    def VolumeDown(self):
        if self.volume > 0:
            if (self.volume - 2) < 0:
                self.volume = 0
            else:
                self.volume = self.volume - 2
        return self

    def VolumeSet(self, volume):
        if volume >= 0 and volume <= 100:
            self.volume = volume

        return self

    def Print(self):
        print("Channel: " + str(self.channel))
        if self.state == 0:
            print("State: OFF")
        else:
            print("State: ON")

        print("Volume: " + str(self.volume))
        print("")
        return self

{

    TV().
        PowerOn().
            ChannelUp().
            ChannelUp().
        Print().VolumeSet(1).Print().VolumeDown().Print().VolumeDown().Print()

}
