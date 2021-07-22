from server.singleton import Singleton
from server.parsr import Parser

class AgentParser(Parser, Singleton):
    """
    Class to retrieve and parse the S-Expression sent by the server to the agents
    """
    result = None

    def __init__(self):
        super().__init__()

    def getHinjePos(self, word: str, lst: list, old):
        value = old
        for i in range(0,len(lst)):
            if value == None or value == old:
                if lst[i] == 'HJ':
                    hingeName = lst[i+1]
                    if hingeName[1] == word:
                        ax = lst[i+2]
                        value = ax[1]
                        return float(value)
                    else:
                        continue
                elif type(lst[i]) is list:
                    value = self.getHinjePos(word, lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value

    #Can be used for ACC too. Just send 'ACC' as the word instead of 'GYR'
    def getGyr(self, word: str, lst: list, old):
        value = old
        for i in range(0,len(lst)):
            if value == [] or value == old:
                if lst[i] == word:
                    valuesList = lst[i+2]
                    x = float(valuesList[1])
                    y = float(valuesList[2])
                    z = float(valuesList[3])
                    value = [x, y, z]
                    return value
                elif type(lst[i]) is list:
                    value = self.getGyr(word, lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value

    def getTime(self, lst: list, old, word='GS'):
        value = old
        time = None
        for i in range(0,len(lst)):
            if value == [] or value == old:
                if lst[i] == word:
                    time = self.getValue('t', lst, old)
                    value = float(time)
                    return value
                elif type(lst[i]) is list:
                    value = self.getTime(lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value


    def getBallVision(self, lst: list, old):
        value = old
        for i in range(0,len(lst)):
            if value == [] or value == old:
                if lst[i] == 'B':
                    valuesList = lst[i+1]
                    distance = float(valuesList[1])
                    angle1 = float(valuesList[2])
                    angle2 = float(valuesList[3])
                    value = [distance, angle1, angle2]
                    return value
                elif type(lst[i]) is list:
                    value = self.getBallVision(lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value

    def getFootResistance(self):
        pass