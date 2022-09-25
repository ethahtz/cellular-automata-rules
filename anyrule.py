import numpy as np
from PIL import Image as im
import random

rule = lambda n: [(n & (2 ** i)) >> i for i in range(8)]

decimize = lambda x, y, z: ((x << 2) + (y << 1) + z)

import sys


if len(sys.argv) == 4:
    ruleID = int(sys.argv[1])
    num_itr = int(sys.argv[2])
    if sys.argv[3] == "-r":
        mode = True
    else:
        mode = False
else:
    num_itr = 50
    ruleID = 30
    mode = False

LENGTH = num_itr + 1


def nextCfg(prev, currRule: list):
    newCfg = []

    newCfg.append(currRule[decimize(prev[-1], prev[0],prev[1])])

    for i in range(1, len(prev) - 1):
        newCfg.append(currRule[decimize(prev[i-1], prev[i], prev[i+1])])
    
    newCfg.append(currRule[decimize(prev[-2], prev[-1],prev[0])])

    return newCfg

def outputFunc(lineToPrint):
    strToPrint = ""
    for elem in lineToPrint:
        if elem == 0:
            strToPrint += " "
        else:
            strToPrint += "#"
    
    print(strToPrint)

outputAry = []



if mode:
    init_config = [random.randint(0, 1) for _ in range(LENGTH)]
else:
    init_config = [0 for _ in range(LENGTH)]
    # init_config[int(LENGTH/2)] = 1
    init_config[-1] = 1

currLine = init_config
outputAry.append(currLine)


# for _ in range(1, num_itr):
#     currLine = nextCfg(currLine, rule(ruleID))

for _ in range(1, num_itr):
    currLine = nextCfg(currLine, rule(ruleID))
    outputAry.append(currLine)


outimg = im.fromarray((np.where(np.array(outputAry) == 0, 255, 0)).astype(np.uint8))
outimg.save('rule_arb.png')
print("P(x=1): ", np.mean(outputAry))