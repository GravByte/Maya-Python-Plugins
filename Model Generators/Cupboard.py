import maya.cmds as cmds

box_H=15
box = cmds.polyCube(w=10,h=box_H,d=10,n="cupboard_#") [0]
cmds.polyExtrudeFacet(box+'.f[4]',ls=(.9,.9,0))
cmds.polyExtrudeFacet(box+'.f[4]',ltz=-9)
cmds.select(box+".e[5]",box+".e[7]",box+".e[9]",box+".e[11]",box+".e[14]",box+".e[16]",box+".e[18:19]")
cmds.polyBevel(offset=0.075)
cmds.delete(box,ch=True)

boxes = []
boxes.append(box)

for i in range(1,4):
    box_D = cmds.duplicate(box)[0]
    cmds.move(0,box_H*i,0,box_D)
    boxes.append(box_D)
    
Cupboard_GRP = cmds.group(boxes,n="Cupboard_GRP")
cmds.move(0,box_H/2,0,Cupboard_GRP)
cmds.makeIdentity(t=1,r=1,s=1,apply = True)