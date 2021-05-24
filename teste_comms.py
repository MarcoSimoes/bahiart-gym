from server.trainer import Trainer

command = Trainer()

#command.changePlayMode("PlayOn")
command.beamBall(0,0,0)
command.beamPlayer(1, "Left", -0.15, 0, 0.3)