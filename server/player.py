from server.agentParser import AgentParser

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

    def __init__(self, unum):

        #Number/id
        self.unum = unum

        #ACC / GYR
        self.acc = None
        self.gyro = None

        #Force Perceptors
        self.lfp = None
        self.rfp = None

        #ballPos
        self.ballPos = None

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


    def isStanding(self):
        pass

    def getUnum(self):
        return self.unum

    def getBallPos(self):
        return self.ballPos

    def updateStats(self, agentMsg):

        #AGENT MSG
        parsedMsg = self.parser.parse(agentMsg)
        
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

        #BALL
        self.ballPos = self.parser.getBallVision(parsedMsg, self.ballPos)