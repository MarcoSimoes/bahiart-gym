from server.ball import Ball
from server.agentParser import AgentParser
from math import fabs, sqrt

class Player(object):
    """ 
    Class to deal with the many player instances for each team
    """
    """
    Perceptor Grammar:

    Grammar = (HJ (n <joint_name>) (<angle_in_degrees>))
    Example = (HJ (n raj2) (ax -15.61))

    Joint Names: https://gitlab.com/robocup-sim/SimSpark/-/wikis/Models#physical-properties
    """

    parser = AgentParser()
    ball = Ball()

    def __init__(self, unum):

        #Number/id
        self.unum = unum

        #Standing of Fallen State
        self.isFallen = False

        #ACC / GYR
        self.acc = None
        self.gyro = None

        #Force Perceptors
        self.lf = []
        self.rf = []
        #NAO TOE ONLY
        #self.lf1 = []
        #self.rf1 = []

        #ballPos
        self.ballFinalPos = [] #The returned list corresponds to [distance, horizontal angle, vertical angle] from the object.
        self.ballInitPos = []
        self.ballSpeed = 0
        self.ballCycle = 0

        #Time
        self.time = None

        #Joints
        self.neckYaw = None
        self.neckPitch = None
        self.leftShoulderPitch = None
        self.leftShoulderYaw = None
        self.leftArmRoll = None
        self.leftArmYaw = None
        self.leftHipYawPitch = None
        self.leftHipRoll = None
        self.leftHipPitch = None
        self.leftKneePitch = None
        self.leftFootPitch = None
        self.leftFootRoll = None
        self.rightHipYawPitch = None
        self.rightHipRoll = None
        self.rightHipPitch = None
        self.rightKneePitch = None
        self.rightFootPitch = None
        self.rightFootRoll = None
        self.rightShoulderPitch = None
        self.rightShoulderYaw = None
        self.rightArmRoll = None
        self.rightArmYaw = None
        #NAO TOE ONLY
        #self.leftToePitch = None
        #self.rightToePitch = None


    def getUnum(self):
        return self.unum

    def getBallPos(self):
        return self.ballFinalPos

    # def checkFallen(self):
        
    #     fallen = False

    #     X_ACEL = self.acc[0]
    #     Y_ACEL = self.acc[1]
    #     Z_ACEL = self.acc[2]

    #     if((fabs(X_ACEL) > Z_ACEL or fabs(Y_ACEL) > Z_ACEL) and Z_ACEL < 5):
    #         #print("FALLEN: " + str([X_ACEL, Y_ACEL, Z_ACEL]))
    #         fallen = True
    #     # else:
    #     #     print("STANDING: " + str([X_ACEL, Y_ACEL, Z_ACEL]))
        
    #     return fallen

    def updateStats(self, agentMsg):

        #AGENT MSG
        parsedMsg = self.parser.parse(agentMsg)
        #print(parsedMsg)
        
        #JOINTS
        self.neckYaw = self.parser.getHinjePos('hj1', parsedMsg, self.neckYaw)
        self.neckPitch = self.parser.getHinjePos('hj2', parsedMsg, self.neckPitch)
        self.leftShoulderPitch = self.parser.getHinjePos('laj1', parsedMsg, self.leftShoulderPitch)
        self.leftShoulderYaw = self.parser.getHinjePos('laj2', parsedMsg, self.leftShoulderYaw)
        self.leftArmRoll = self.parser.getHinjePos('laj3', parsedMsg, self.leftArmRoll)
        self.leftArmYaw = self.parser.getHinjePos('laj4', parsedMsg, self.leftArmYaw)
        self.leftHipYawPitch = self.parser.getHinjePos('llj1', parsedMsg, self.leftHipYawPitch)
        self.leftHipRoll = self.parser.getHinjePos('llj2', parsedMsg, self.leftHipRoll)
        self.leftHipPitch = self.parser.getHinjePos('llj3', parsedMsg, self.leftHipPitch)
        self.leftKneePitch = self.parser.getHinjePos('llj4', parsedMsg, self.leftKneePitch)
        self.leftFootPitch = self.parser.getHinjePos('llj5', parsedMsg, self.leftFootPitch)
        self.leftFootRoll = self.parser.getHinjePos('llj6', parsedMsg, self.leftFootRoll)
        self.rightHipYawPitch = self.parser.getHinjePos('rlj1', parsedMsg, self.rightHipYawPitch)
        self.rightHipRoll = self.parser.getHinjePos('rlj2', parsedMsg, self.rightHipRoll)
        self.rightHipPitch = self.parser.getHinjePos('rlj3', parsedMsg, self.rightHipPitch)
        self.rightKneePitch = self.parser.getHinjePos('rlj4', parsedMsg, self.rightKneePitch)
        self.rightFootPitch = self.parser.getHinjePos('rlj5', parsedMsg, self.rightFootPitch)
        self.rightFootRoll = self.parser.getHinjePos('rlj6', parsedMsg, self.rightFootRoll)
        self.rightShoulderPitch = self.parser.getHinjePos('raj1', parsedMsg, self.rightShoulderPitch)
        self.rightShoulderYaw = self.parser.getHinjePos('raj2', parsedMsg, self.rightShoulderYaw)
        self.rightArmRoll = self.parser.getHinjePos('raj3', parsedMsg, self.rightArmRoll)
        self.rightArmYaw = self.parser.getHinjePos('raj4', parsedMsg, self.rightArmYaw)

        #ACC/GYR
        self.acc = self.parser.getGyr('ACC', parsedMsg, self.acc)
        self.gyro = self.parser.getGyr('GYR', parsedMsg, self.gyro)
        
        #TIME
        self.time = self.parser.getTime(parsedMsg, self.time)

        #BALL
        self.ballFinalPos = self.parser.getBallVision(parsedMsg, self.ballFinalPos)
        # print("Ball POS: " + str(self.ballFinalPos))
        # if(self.ballCycle == 0):
        #     self.ballInitPos = self.ballFinalPos
        # self.ballCycle += 1
        # if(self.ballCycle == 29):
        #     self.ballSpeed = sqrt((self.ballFinalPos[0] - self.ballInitPos[0])**2 + (self.ballFinalPos[1] - self.ballInitPos[1])**2) / 0.6
        #     self.ballCycle = 0
        #     print("ball Speed: " + str(self.ballSpeed))

        #FORCE RESISTANCE PERCEPTORS
        self.lf = self.parser.getFootResistance('lf', parsedMsg, self.lf)
        self.rf = self.parser.getFootResistance('rf', parsedMsg, self.rf)
        
        #self.ball.updatePlayer(self.ballPos, self.time)

        #CHECK IF PLAYER IS FALLEN
        #self.isFallen = self.checkFallen()
        
        #NAO TOE
        #self.lf1 = self.parser.getFootResistance('lf1', parsedMsg, self.lf1)
        #self.rf1 = self.parser.getFootResistance('rf1', parsedMsg, self.rf1)
        #self.leftToePitch = self.parser.getHinjePos('llj7', parsedMsg, self.leftToePitch)
        #self.rightToePitch = self.parser.getHinjePos('rlj7', parsedMsg, self.leftToePitch)