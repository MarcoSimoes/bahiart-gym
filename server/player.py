from agentParser import AgentParser

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

    def __init__(self):
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
        pass

    def getAgentState(self):
        pass

    def setAgentState(self):
        pass

    def getUnum(self):
        pass

    def getPos(self):
        pass

    def updateJoints(self, agentMsg: list):

        HJlist = self.parser.parse(agentMsg)
        
        self.neckYaw = self.parser.getHinjePos('hj1', HJlist, self.neckYaw)
        self.neckPitch = self.parser.getHinjePos('hj2', HJlist, self.neckPitch)
        self.leftShoulderPitch = self.parser.getHinjePos('laj1', HJlist, self.leftShoulderPitch)
        self.leftShoulderYaw = self.parser.getHinjePos('laj2', HJlist, self.leftShoulderYaw)
        self.leftArmRoll = self.parser.getHinjePos('laj3', HJlist, self.leftArmRoll)
        self.leftArmYaw = self.parser.getHinjePos('laj4', HJlist, self.leftArmYaw)
        self.leftHipYawPitch = self.parser.getHinjePos('llj1', HJlist, self.leftHipYawPitch)
        self.leftHipRoll = self.parser.getHinjePos('llj2', HJlist, self.leftHipRoll)
        self.leftHipPitch = self.parser.getHinjePos('llj3', HJlist, self.leftHipPitch)
        self.leftKneePitch = self.parser.getHinjePos('llj4', HJlist, self.leftKneePitch)
        self.leftFootPitch = self.parser.getHinjePos('llj5', HJlist, self.leftFootPitch)
        self.leftFootRoll = self.parser.getHinjePos('llj6', HJlist, self.leftFootRoll)
        self.rightHipYawPitch = self.parser.getHinjePos('rlj1', HJlist, self.rightHipYawPitch)
        self.rightHipRoll = self.parser.getHinjePos('rlj2', HJlist, self.rightHipRoll)
        self.rightHipPitch = self.parser.getHinjePos('rlj3', HJlist, self.rightHipPitch)
        self.rightKneePitch = self.parser.getHinjePos('rlj4', HJlist, self.rightKneePitch)
        self.rightFootPitch = self.parser.getHinjePos('rlj5', HJlist, self.rightFootPitch)
        self.rightFootRoll = self.parser.getHinjePos('rlj6', HJlist, self.rightFootRoll)
        self.rightShoulderPitch = self.parser.getHinjePos('raj1', HJlist, self.rightShoulderPitch)
        self.rightShoulderYaw = self.parser.getHinjePos('raj2', HJlist, self.rightShoulderYaw)
        self.rightArmRoll = self.parser.getHinjePos('raj3', HJlist, self.rightArmRoll)
        self.rightArmYaw = self.parser.getHinjePos('raj4', HJlist, self.rightArmYaw)