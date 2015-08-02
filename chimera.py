# --------------------------------------------------------
#
#    Chimera Core      Revision 3
#    Created by:
#        Andromeda <andromeda@cerberuslabs.ca>
#        Jobe <jobe@mdbnet.net>
#
# --------------------------------------------------------

# Load some libs
#moo

# Include some files
import config
import modules.irc
import modules.sock
import modules.parser as parser
import modules.channels
import modules.commands
from subprocess import call

irc = modules.irc.irc()
chanlist = modules.channels.chanlist()
cmd = modules.commands.commands()

sock = modules.sock.sock()
irc.setsock(sock)
cmd.setsock(sock)

sock.connect(config.server, config.port)

irc.conn_nick(config.nick)
irc.conn_user(config.ident, config.realname)

# Begin the loop if we're good to go
while 1:
    feed = sock.recv()
    feed = feed.splitlines()

    for line in feed:
        print line
        x = parser.parse_raw_irc(line)

        if (x['msg'] == "PING"):
            irc.ping(x['params'][-1])

        if (x['msg'] == "001"):
            irc.umode(config.nick)
            irc.join(config.channels)

        if (x['msg'] == "JOIN"):
            chanlist.addchannel(x['params'][0])

        if (x['msg'] == "PART"):
            chanlist.delchannel(x['params'][0])

        if (x['msg'] == "KICK"):
            if (x['params'][1].lower() == botnick.lower()):
                chanlist.delchannel(x['params'][0])

        if (x['msg'] == "NICK"):
            if (x['source']['name'].lower() == botnick.lower()):
                botnick = x['params'][0]

        if (x['msg'] == "PRIVMSG"):
            if (chanlist.ischannel(x['params'][0])):
                if (x['params'][1][0] == config.prefix):
                    tmp = x['params'][1][1:]
                    com = tmp.split(' ')

                    if (com[0].lower() == "uptime"):
                        cmd.uptime(x['params'][0])

            if (x['params'][1] == "\x01VERSION\x01"):
                cmd.version(x['source']['name'])
