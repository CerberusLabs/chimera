# Channels module
# Handles everything to do with channels

class chanlist:
    _chanlist = []

    def getchanlist(self):
        return self._chanlist

    def addchannel(self, channel):
        if channel.lower() in self._chanlist:
            return
        self._chanlist.append(channel.lower())

    def delchannel(self, channel):
        if channel.lower() in self._chanlist:
            self._chanlist.remove(channel.lower())

    def ischannel(self, channel):
        if channel.lower() in self._chanlist:
            return True
        return False

