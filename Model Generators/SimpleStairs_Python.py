import maya.cmds as cmds

steps = []

for i in range(10):
    step = cmds.polyCube(n="step#",w=8,d=2,h=0.5,ch=False)[0]
    cmds.move(0,0.5*i,2*i)
    steps.append(step)

cmds.select(steps)  
Steps_Grp = cmds.group(n="step_Grp")
bendNL = cmds.nonLinear(Steps_Grp,type='bend',curvature=90)
cmds.rotate(-90,0,0,bendNL)
cmds.delete(Steps_Grp,ch=True)