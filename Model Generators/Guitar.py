import maya.cmds as cmds
#GuitarBase
cyl_01 = cmds.polyCylinder(r=8,h=2,n="cyl_01")
cyl_02 = cmds.polyCylinder(r=6,h=2,n="cyl_02")
cmds.move(-8,0,0,cyl_02)
cyl_03 = cmds.polyCylinder(r=3,h=1,n="cyl_03")
cmds.move(-8,0.75,0,cyl_03)
cmds.select(cyl_01,cyl_02,cyl_03)
cmds.delete(ch=1)
cmds.makeIdentity(t=1,r=1,s=1,apply=True)
guitarBase_GRP = cmds.group(n="guitarBase_GRP")

#GuitarHandle
guitarHandle=cmds.polyCube(w=25,h=1,d=3,n="guitarHandle")
cmds.move(-25,0.25,0.186,guitarHandle)
Box_01=cmds.polyCube(w=1.5,h=1,d=8,n="Box_01")
cmds.move(3,2,0,Box_01)
Box_02=cmds.polyCube(w=0.8,h=2,d=2.5,n="Box_02")
cmds.move(-36,1,0,Box_02)
cmds.select(guitarHandle,Box_01,Box_02)
cmds.delete(ch=1)
cmds.makeIdentity(t=1,r=1,s=1,apply=True)
Handle_GRP = cmds.group(n="Handle_GRP")

#Threads
Thread = cmds.polyCylinder(h=40,r=0.1,n="thread#")[0]
cmds.rotate(0,0,90,Thread)
cmds.move(-16,1.5,-0.8,Thread)

Threads = []
Threads.append(Thread)

for i in range(1,5):
    Thread_D = cmds.duplicate(Thread)[0]
    cmds.move(0,0,0.5*i,Thread_D,r=1)
    Threads.append(Thread_D)
    
cmds.select(Threads)
cmds.delete(ch=1)
cmds.makeIdentity(t=1,r=1,s=1,apply=True)
Thread_GRP = cmds.group(n="Thread_GRP")

#Knobs
Knob = cmds.polyCylinder(r=0.35,h=0.2,ch=0)[0]
Knob_Box = cmds.polyCube(w=0.25,h=0.12,d=1.5,ch=0)[0]
cmds.move(0,0,0.85,Knob_Box)
k_=cmds.polyUnite(Knob,Knob_Box)
cmds.delete(ch=1)

Knobs = []
Knobs.append(k_[0])
for i in range(1,3):
    d = cmds.duplicate(k_)[0]
    cmds.move(1*i,0,0,d,r=1)
    Knobs.append(d)
    
L_Knobs = cmds.polyUnite(Knobs, n="L_Knobs")
cmds.delete(ch=1)

R_Knobs = cmds.duplicate(L_Knobs, n="R_Knobs")
cmds.scale(1,1,-1,R_Knobs,r=1)
cmds.move(0,0,5,R_Knobs)

k_T = cmds.polyUnite(L_Knobs[0],R_Knobs[0],n="K_Total")
cmds.delete(ch=1)

cmds.move(-36,0,-2.35,k_T[0])
cmds.makeIdentity(t=1,r=1,s=1,apply=True)

Guitar_GRP = cmds.group(k_T[0],Thread_GRP,Handle_GRP,guitarBase_GRP,n="Guitar_GRP")