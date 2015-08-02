# Server and protocol module
# Everything needed to keep us connected and stable


class irc:
    _s = 0

    def setsock(self, sock):
        self._s = sock

    def ping(self, res):
        self._s.send("PONG :"+res+"\r\n")

    def send_message(self, chan, msg):
        self._s.send("PRIVMSG "+chan+" :"+msg+"\r\n")

    def send_notice(self, user, msg):
        self._s.send("NOTICE "+target+" :"+msg+"\r\n")

    def join(self, chan):
        self._s.send("JOIN "+chan+"\r\n")
        self._s.send("WHO "+chan+" %na\r\n")

    def part(self, chan):
        self._s.send("PART "+chan+"\r\n")

    def umode(self, nick):
        self._s.send("MODE "+nick+" -ix\r\n")

    def mode(self, chan):
        self._s.send("MODE "+chan+" +s\r\n")

    def conn_nick(self, nick):
        self._s.send("NICK "+nick+"\r\n")

    def conn_user(self, ident, name):
        self._s.send("USER "+ident+" 0 * :"+name+"\r\n")
