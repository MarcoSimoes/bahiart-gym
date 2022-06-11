"""
        Copyright (C) 2022  Salvador, Bahia
        Gabriel Mascarenhas, Marco A. C. Simões, Rafael Fonseca

        This file is part of BahiaRT GYM.

        BahiaRT GYM is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as
        published by the Free Software Foundation, either version 3 of the
        License, or (at your option) any later version.

        BahiaRT GYM is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.

        You should have received a copy of the GNU Affero General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# -*- coding: utf-8 -*-
import os
import signal
def killEnv(serverPID, envPID, teamPID):
    
    print("Killing server ...\n")
    os.kill(serverPID, signal.SIGKILL)
    print("Killing environment ...\n")
    os.kill(envPID, signal.SIGTERM)
    print("Killing team ...\n")
    os.kill(teamPID, signal.SIGTERM)