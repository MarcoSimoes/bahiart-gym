from server.parsr import Parser
from server.singleton import Singleton

class ServerParser(Parser, Singleton):
    """
    Class to retrieve and parse the S-Expression sent from the server
    'Consider changing the name to TrainerParser'
    """

    def __init__(self):
        pass

    #Gets the entire ball node
    def setBallNd(self, lst: list):
        sceneGraph = lst[2]
        ballNd = sceneGraph[35]
        return ballNd

    #Gets only the N.O.A.P Values inside the node
    def getBallGraph(self, lst: list, old):
        value = old
        for i in range(0,len(lst)):
            if value == [] or value == old:
                if lst[i] == 'SLT':
                    value = lst[1:]
                    return value
                elif type(lst[i]) is list:
                    value = self.getBallGraph(lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value

    def getBallPos(self, lst: list, old: list):
        if(lst is None or len(lst) < 12):
            return old
        else:
            x = lst[12]
            y = lst[13]
            z = lst[14]
            ballPos = [x, y, z]
            return ballPos