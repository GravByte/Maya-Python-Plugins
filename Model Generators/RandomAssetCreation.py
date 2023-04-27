import maya.cmds as cmds
import random

try:
    if cmds.window(window, exists = True):
        cmds.deleteUI(window)
except NameError:
    print ("ERROR")
    

def addElements():
    cmds.textScrollList( elementsTFG,e=1,ra=1)
    sel = cmds.ls(sl=1)
    cmds.textScrollList( elementsTFG,e=1,a=sel)

def createRandom():
    objects = cmds.textScrollList( elementsTFG,q=1,ai=1)
    for i in range(10):
        sRandomObj = random.choice(objects)
        obj = cmds.duplicate(sRandomObj)
        cmds.move(random.uniform(-10,10),0,random.uniform(-10,10),obj)

randomWin = cmds.window(t="RK_RandomCreator",wh=(250,300),s=0)
cmds.columnLayout(adjustableColumn=True)
cmds.text(l="Objects in Collection",fn="boldLabelFont")
cmds.separator(h=10)
elementsTFG = cmds.textScrollList(numberOfRows=8,allowMultiSelection=True,h=125)
cmds.separator(h=10)
addElementsBtn = cmds.button(l="Add Elements",h=50,c="addElements()")
cmds.separator(h=10)
createRandomBtn = cmds.button(l="Create Random",h=50,c="createRandom()")
cmds.showWindow( randomWin )
