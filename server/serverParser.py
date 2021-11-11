from multiprocessing import Lock
from server.sexpr import str2sexpr
from server.singleton import Singleton
#from server.parsr import Parser

class ServerParser(Singleton):
    """
    Class to retrieve and parse the S-Expression sent from the server
    'Consider changing the name to TrainerParser'
    """

    def __init__(self):
        super().__init__()
        self.mutex = Lock()

    def parse(self, string:str):
        parsedString = []       
        with self.mutex:
            parsedString = str2sexpr(string)    
        return parsedString

    def searchObject(self, word: str, lst: list):
        found=False
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                found=self.searchObject(word, lst[i])
            elif lst[i] == word:
                found=True
            if found:
                break
    ##        print("Word: ",str(lst[i]), "Found: ", str(found)) 
        return found

    #Gets the entire ball node
    def getBallIndex(self, lst: list, latestIndex): #Change this to index
        sceneGraph = lst[2]
        sceneGraphHeader = lst[1]
        #ballNd = sceneGraph[35]
        #return ballNd
        foundBall=False
        if(sceneGraphHeader[0]=="RSG"):
            #print("Searching ball in full graph ....")
            for idx, nod in enumerate(sceneGraph):
                foundBall=self.searchObject("models/soccerball.obj",nod)
                if(foundBall):  
                    break
        else:
            if(latestIndex is None):
                latestIndex = 35 #In previous tests, the index 35 seemed to be the ball index almost everytime. This is just to make sure i'm not using None as index.
            ballIndex = latestIndex
            return ballIndex
        if(foundBall):
            #print("Node ball index: ",str(idx), " Graph Size: ", str(len(sceneGraph)))
            ballIndex = idx
            return ballIndex

    def getBallNd(self, lst: list, ballIndex):
        sceneGraph = lst[2]
        ballNd = sceneGraph[ballIndex]
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
            ballPos = [float(x), float(y), float(z)]
            return ballPos

    def search(self, word: str, lst: list):
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                self.search(word, lst[i])
            elif lst[i] == word:
                print(word, '=', lst[i+1])
            continue
        return

    def getValue(self, word: str, lst: list, old):
        value = old
        for i in range(0,len(lst)):
            if value == None or value == old:
                if lst[i] == word:
                    value = lst[i+1]
                    return value
                elif type(lst[i]) is list:
                    value = self.getValue(word, lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value