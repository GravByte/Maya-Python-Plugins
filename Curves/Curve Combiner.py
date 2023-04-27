import maya.cmds as cmds

selList = cmds.ls(sl=1)

cmds.delete(selList,ch=1)
cmds.makeIdentity(apply=True)

selListShape = []
for sel in selList:
    sShape = cmds.listRelatives(sel, s=1)
    selListShape.append(sShape)
    
main = selList[0]
selListShape.pop(0)
for i in range(len(selListShape)):
    cmds.parent(selListShape[i],main, s=1, r=1)
    
cmds.delete(main, ch=1)
selList.pop(0)
cmds.delete(selList)
cmds.select(cl=1)