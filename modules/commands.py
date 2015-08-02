# Commands module
# Handles everything to do with commands
import subprocess
import re

class commands:
    _s = 0

    def setsock(self, sock):
        self._s = sock

    def version(self, tnick):
        self._s.send("NOTICE "+tnick+" :\x01VERSION Chimera Core [Python] v0.0.3\x01\r\n")

    def uptime(self, target):

        proc = subprocess.Popen('uptime', stdout=subprocess.PIPE)
        vuptime = proc.stdout.read()
        vuptime = vuptime.strip()

        proc = subprocess.Popen('hostname', stdout=subprocess.PIPE)
        vhostname = proc.stdout.read()
        vhostname = vhostname.strip()

        proc = subprocess.Popen(['lsb_release', '-ds'], stdout=subprocess.PIPE)
        vdistro = proc.stdout.read()
        vdistro = vdistro.strip()
        vdistro = re.sub('["]', '', vdistro)
        vdistro = vdistro.rsplit(' ', 1)[0]

        self._s.send("PRIVMSG "+target+" :Uptime for "+vhostname.lower()+" ("+vdistro+"): "+vuptime+"\r\n")

