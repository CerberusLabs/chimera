# Line parser module
# Handles all the incoming information and makes it usable

def parse_raw_irc(line):
        ret = {'source': {'full': "", 'name': "", 'ident': "", 'host': ""}, 'msg': "", 'params': []}

        stat = 0

        words = line.split(' ')

        for word in words:
                if ((stat < 3) and (len(word) == 0)):
                        continue

                if (stat == 0):
                        stat += 1
                        if (word[0] == ":"):
                                 ret['source']['full'] = word[1:]
                        else:
                                ret['msg'] = word
                                stat += 1
                elif (stat == 1):
                        ret['msg'] = word
                        stat += 1
                elif (stat == 2):
                        if (word[0] == ":"):
                                ret['params'].append(word[1:])
                                stat += 1
                        else:
                                ret['params'].append(word)
                else:
                        ret['params'][-1] = ret['params'][-1] + " " + word
        #end for

        if (len(ret['source']['full']) > 0):
                src = ret['source']['full']
                if (src.find("@") >= 0):
                        ret['source']['host'] = src[src.find("@")+1:]
                        src = src[:src.find("@")]
                if (src.find("!") >= 0):
                        ret['source']['ident'] = src[src.find("!")+1:]
                        src = src[:src.find("!")]
                ret['source']['name'] = src
        #end if

        return ret

