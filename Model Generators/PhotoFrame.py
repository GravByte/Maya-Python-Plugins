import maya.cmds as cmds

frame = cmds.polyPipe(r=5,h=4,t=1,sa=4,n="Frame")
cmds.rotate(0,45,0,frame)
#cmds.select(frame[0]+".e[4:11]")
cmds.polyBevel(frame[0]+".e[4:11]",offset=0.075)
cmds.delete(ch=1)
cmds.makeIdentity(t=1,r=1,s=1,apply=True)

photo=cmds.polyCube(w=6.25,h=0.5,d=6.25,n="Photo",ch=0)

photoFrameGRP=cmds.group(frame[0],photo,n="PhotoFrame_GRP")