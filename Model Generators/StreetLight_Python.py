import maya.cmds as cmds

base1 = cmds.polyCylinder(n="LightBase1",r=1,h=2,ch=False)
base2 = cmds.polyCylinder(n="LightBase2",r=0.6,h=3,ch=False)
cmds.move(0,2.5,0)
pole = cmds.polyCylinder(n="pole",r=0.2,h=20,sh=20)
cmds.move(0,13.7,0)
bendNL = cmds.nonLinear(pole,type='bend',curvature=60,lowBound = 0)
cmds.delete(pole,ch=True)
light = cmds.polyCube(n="light",w=5,h=2,d=2,ch=False)
cmds.move(6.6,21.6,-0.06)
streetLight_Grp = cmds.group("LightBase1","LightBase2","pole","light",n="streetLight_Grp")