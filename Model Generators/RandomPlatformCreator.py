import maya.cmds as cmds
import random

selected = cmds.ls(sl=1)
sel = selected[0]
cur = selected[1]

for i in range(20):
    tempObj = cmds.duplicate(sel,n="platform_#")
    if i%2==0:
        cmds.move(3.5*i,0,2,tempObj)
    else:
        cmds.move(3.5*i,0,-2,tempObj)
    cmds.rotate(0,random.randint(-30,30),0,tempObj)
    cmds.scale(random.uniform(0.75,1.2),1,random.uniform(0.75,1.2),tempObj)
        
platform_GRP = cmds.group("platform*")
cmds.select(cl=1)

totalJoints = []
for i in range(31):
    j = cmds.joint(n="chainJtn%d"%i)
    cmds.move(0,0,4*i,j)
    totalJoints.append(j)
    
cmds.bindSkin(platform_GRP,totalJoints[0])
chainIK = cmds.ikHandle(sj=totalJoints[0],ee=totalJoints[-1],c=cur,ccv=0,sol="ikSplineSolver",n="chainIK")

cmds.duplicate(platform_GRP,n="NewPath")

cmds.delete(platform_GRP,cur,chainIK,sel,totalJoints)
