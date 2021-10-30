#!usr/bin/python3.7
from gurobipy import *
import pandas as pd

def getModelData():
    print("WARNING: parser not implemented... returning dummy data")

    modelData = {
        'teachers': ['Marcelo', 'Henrique', 'Kafka'],
        'courses' : ['MC102A', 'MC404A', 'MC739A'],
        'teacherForbiddenTimeSlot': dict({
            ('Marcelo')  :(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            ('Henrique') :(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            ('Kafka')    :(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
        }),

        'assignmentArcs' : {
            ('Marcelo', 'MC102A') : 3,
            ('Marcelo', 'MC404A') : 1,

            ('Henrique', 'MC102A') : 3,
            ('Henrique', 'MC404A') : 2,

            ('Kafka', 'MC739A') :1,
        },

        'courseTimeSlot': dict({
            ('MC102A') : [
                        (1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        (1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        (0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        ],
            ('MC404A') : [
                        (1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        (0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        (0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        ],
            ('MC739A') : [
                        (1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        (0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        (0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                        ],
        }),

        'teacherMaxCredit': dict({
            ('Marcelo')  : 60,
            ('Henrique') : 60,
            ('Kafka')    : 60,

        }),

        'teacherMinCredit': dict({
            ('Marcelo')  : 0,
            ('Henrique') : 0,
            ('Kafka')    : 0,

        }),

        'courseCredits' : dict({
            ('MC102A') : 6,
            ('MC404A') : 4,
            ('MC739A') : 4,
        }),
    }

    return modelData