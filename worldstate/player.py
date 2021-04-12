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

    neckYaw = None
    neckPitch = None
    leftShoulderPitch = None
    leftShoulderYaw = None
    leftArmRoll = None
    leftArmYaw = None
    leftHipYawPitch = None
    leftHipRoll = None
    leftHipPitch = None
    leftKneePitch = None
    leftFootPitch = None
    leftFootRoll = None
    rightHipYawPitch = None
    rightHipRoll = None
    rightHipPitch = None
    rightKneePitch = None
    rightFootPitch = None
    rightFootRoll = None
    rightShoulderPitch = None
    rightShoulderYaw = None
    rightArmRoll = None
    rightArmYaw = None

    def __init__(self):
        pass

    def getAgentState(self):
        pass

    def setAgentState(self):
        pass

    def getUnum(self):
        pass

    def getPos(self):
        pass

    def updateJoints(self):
        pass