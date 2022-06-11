#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:28:33 2022

@author: marco
"""
from bahiart_gym.server.agentParser import AgentParser


def extractTokens(lst: list,):
    if type(lst[0]) is list:
        return extractTokens(lst[0])
    elif type(lst[0]) is str:
        return lst[0],lst[1:]
    
def updateStats(parsedMsg):

    #AGENT MSG
#    parsedMsg = parser.parse(agentMsg)
    
 #   self.logfile.write(str(parsedMsg))
    
    for value in parsedMsg:
        if type(value is list):
            value,args=extractTokens(value)
        
        if value=='HJ':
            name,value=parser.getHingePos(args)
            joints[name]=value
        elif value=='ACC':
            acc=parser.getAcc(args)
        elif value=='GYR':
            gyr=parser.getGyr(args)
        elif value=='time':
            cTime=parser.getTime(args)
        elif value=='GS':
            gs=parser.getGameState(args)
            leftScore=gs[0]
            rightScore=gs[1]
            gTime=gs[2]
            playmode=gs[3]
        elif value=='FRP':
            if args[0][1]=='rf':
                lf=parser.getFootResistance(args)
            elif args[0][1]=='lf':
                lr=parser.getFootResistance(args)
            elif args[0][1]=='lf1':
                lf1=parser.getFootResistance(args)
            elif args[0][1]=='lr1':
                lr1=parser.getFootResistance(args)

#Main Function

if __name__ == '__main__':
    parser=AgentParser()
    jointNames = ['hj1', 
                  'hj2', 
                  'llj1', 
                  'rlj1', 
                  'llj2', 
                  'rlj2', 
                  'llj3', 
                  'rlj3',
                  'llj4',
                  'rlj4', 
                  'llj5', 
                  'rlj5', 
                  'llj6', 
                  'rlj6', 
                  'laj1', 
                  'raj1', 
                  'laj2', 
                  'raj2', 
                  'laj3', 
                  'raj3', 
                  'laj4', 
                  'raj4',
                  'llj7',
                  'lrj7']
    joints = dict.fromkeys(jointNames,0.0)
    msg=[['time', ['now', '11.14']], ['GS', ['sl', '0'], ['sr', '0'], ['t', '0.00'], ['pm', 'BeforeKickOff']], ['GYR', ['n', 'torso'], ['rt', '0.04', '-0.00', '-0.00']], ['ACC', ['n', 'torso'], ['a', '0.00', '-0.00', '0.05']], ['HJ', ['n', 'hj1'], ['ax', '-0.00']], ['HJ', ['n', 'hj2'], ['ax', '-0.00']], ['HJ', ['n', 'raj1'], ['ax', '0.00']], ['HJ', ['n', 'raj2'], ['ax', '0.00']], ['HJ', ['n', 'raj3'], ['ax', '0.00']], ['HJ', ['n', 'raj4'], ['ax', '-0.00']], ['HJ', ['n', 'laj1'], ['ax', '0.00']], ['HJ', ['n', 'laj2'], ['ax', '-0.00']], ['HJ', ['n', 'laj3'], ['ax', '-0.00']], ['HJ', ['n', 'laj4'], ['ax', '-0.00']], ['HJ', ['n', 'rlj1'], ['ax', '0.00']], ['HJ', ['n', 'rlj2'], ['ax', '0.00']], ['HJ', ['n', 'rlj3'], ['ax', '-0.00']], ['HJ', ['n', 'rlj4'], ['ax', '-0.00']], ['HJ', ['n', 'rlj5'], ['ax', '-0.00']], ['HJ', ['n', 'rlj6'], ['ax', '0.00']], ['HJ', ['n', 'llj1'], ['ax', '0.00']], ['HJ', ['n', 'llj2'], ['ax', '0.00']], ['HJ', ['n', 'llj3'], ['ax', '-0.00']], ['HJ', ['n', 'llj4'], ['ax', '-0.00']], ['HJ', ['n', 'llj5'], ['ax', '-0.00']], ['HJ', ['n', 'llj6'], ['ax', '-0.00']]]
    msg=[['time', ['now', '15.44']], ['GS', ['sl', '0'], ['sr', '0'], ['t', '0.28'], ['pm', 'KickOff_Left']], ['hear', 'BahiaRT', '0.28', '176.84', 'Ew1nt8h8QlDyqM00000H'], ['GYR', ['n', 'torso'], ['rt', '-157.44', '-0.03', '-0.02']], ['ACC', ['n', 'torso'], ['a', '0.12', '-0.00', '9.78']], ['HJ', ['n', 'hj1'], ['ax', '-39.90']], ['HJ', ['n', 'hj2'], ['ax', '-40.09']], ['See', ['G1L', ['pol', '14.91', '47.74', '34.26']], ['G2L', ['pol', '14.78', '55.87', '30.34']], ['F1L', ['pol', '18.30', '11.75', '40.76']], ['B', ['pol', '0.97', '-47.32', '-7.03']], ['P', ['team', 'BahiaRT'], ['id', '1'], ['head', ['pol', '14.15', '51.27', '31.45']], ['rlowerarm', ['pol', '14.13', '50.92', '30.39']], ['llowerarm', ['pol', '14.09', '50.45', '30.89']], ['rfoot', ['pol', '14.20', '50.18', '29.87']], ['lfoot', ['pol', '14.19', '49.91', '29.82']]], ['P', ['team', 'BahiaRT'], ['id', '9'], ['head', ['pol', '8.69', '-51.58', '27.78']], ['rlowerarm', ['pol', '8.61', '-50.79', '26.41']], ['llowerarm', ['pol', '8.80', '-50.67', '26.33']], ['rfoot', ['pol', '8.65', '-49.40', '25.08']], ['lfoot', ['pol', '8.75', '-49.44', '25.03']]], ['P', ['team', 'BahiaRT'], ['id', '2'], ['head', ['pol', '10.01', '41.81', '35.22']], ['rlowerarm', ['pol', '9.96', '42.10', '34.14']], ['llowerarm', ['pol', '9.98', '40.74', '34.75']], ['rfoot', ['pol', '10.03', '40.81', '32.80']], ['lfoot', ['pol', '10.07', '40.24', '32.97']]], ['P', ['team', 'BahiaRT'], ['id', '7'], ['head', ['pol', '3.12', '-48.10', '29.28']], ['rlowerarm', ['pol', '3.04', '-45.98', '25.55']], ['llowerarm', ['pol', '3.23', '-46.73', '25.60']], ['rfoot', ['pol', '3.09', '-42.73', '21.81']], ['lfoot', ['pol', '3.20', '-42.36', '21.79']]], ['P', ['team', 'BahiaRT'], ['id', '3'], ['head', ['pol', '9.75', '56.49', '28.40']], ['rlowerarm', ['pol', '9.74', '56.51', '27.10']], ['llowerarm', ['pol', '9.69', '55.21', '27.91']], ['rfoot', ['pol', '9.78', '55.26', '25.67']], ['lfoot', ['pol', '9.79', '54.60', '26.01']]], ['P', ['team', 'BahiaRT'], ['id', '4'], ['head', ['pol', '5.63', '-39.51', '33.60']], ['rlowerarm', ['pol', '5.54', '-38.47', '31.58']], ['llowerarm', ['pol', '5.72', '-38.90', '31.49']], ['rfoot', ['pol', '5.60', '-36.25', '29.52']], ['lfoot', ['pol', '5.69', '-35.97', '29.74']]], ['P', ['team', 'BahiaRT'], ['id', '6'], ['head', ['pol', '4.74', '44.29', '34.22']], ['rlowerarm', ['pol', '4.75', '44.24', '31.32']], ['llowerarm', ['pol', '4.70', '41.94', '32.30']], ['rfoot', ['pol', '4.79', '42.33', '28.99']], ['lfoot', ['pol', '4.81', '40.86', '29.05']]], ['P', ['team', 'BahiaRT'], ['id', '11'], ['rlowerarm', ['pol', '0.24', '-17.20', '-31.56']], ['llowerarm', ['pol', '0.24', '39.69', '-57.18']], ['rfoot', ['pol', '0.53', '-1.39', '-42.70']], ['lfoot', ['pol', '0.53', '12.67', '-49.61']]], ['L', ['pol', '0.59', '-32.52', '-55.76'], ['pol', '10.82', '-51.97', '24.16']], ['L', ['pol', '14.92', '59.75', '24.13'], ['pol', '18.33', '11.47', '40.49']], ['L', ['pol', '10.97', '-59.94', '19.03'], ['pol', '18.28', '11.58', '40.53']], ['L', ['pol', '13.54', '35.58', '35.13'], ['pol', '13.11', '59.88', '23.92']], ['L', ['pol', '13.54', '35.64', '35.25'], ['pol', '15.25', '37.79', '34.81']], ['L', ['pol', '2.86', '-60.04', '8.72'], ['pol', '2.78', '-38.87', '21.74']], ['L', ['pol', '2.78', '-38.70', '21.78'], ['pol', '2.47', '-10.48', '29.11']], ['L', ['pol', '2.47', '-10.80', '28.87'], ['pol', '2.02', '22.64', '24.95']], ['L', ['pol', '2.02', '22.73', '24.82'], ['pol', '1.54', '55.68', '4.48']], ['L', ['pol', '1.54', '55.87', '4.51'], ['pol', '1.43', '60.06', '-0.72']]], ['HJ', ['n', 'raj1'], ['ax', '-88.28']], ['HJ', ['n', 'raj2'], ['ax', '0.00']], ['HJ', ['n', 'raj3'], ['ax', '7.03']], ['HJ', ['n', 'raj4'], ['ax', '4.57']], ['HJ', ['n', 'laj1'], ['ax', '-88.28']], ['HJ', ['n', 'laj2'], ['ax', '-0.00']], ['HJ', ['n', 'laj3'], ['ax', '-7.03']], ['HJ', ['n', 'laj4'], ['ax', '-4.57']], ['HJ', ['n', 'rlj1'], ['ax', '0.00']], ['HJ', ['n', 'rlj2'], ['ax', '-0.00']], ['HJ', ['n', 'rlj3'], ['ax', '7.03']], ['HJ', ['n', 'rlj4'], ['ax', '-7.03']], ['HJ', ['n', 'rlj5'], ['ax', '7.03']], ['FRP', ['n', 'rf'], ['c', '0.00', '-0.08', '-0.01'], ['f', '-0.09', '2.90', '39.76']], ['HJ', ['n', 'rlj6'], ['ax', '0.00']], ['HJ', ['n', 'llj1'], ['ax', '-0.00']], ['HJ', ['n', 'llj2'], ['ax', '0.00']], ['HJ', ['n', 'llj3'], ['ax', '7.03']], ['HJ', ['n', 'llj4'], ['ax', '-7.03']], ['HJ', ['n', 'llj5'], ['ax', '7.03']], ['FRP', ['n', 'lf'], ['c', '0.00', '-0.08', '-0.01'], ['f', '-0.09', '2.85', '39.33']], ['HJ', ['n', 'llj6'], ['ax', '-0.00']]]
    updateStats(msg)