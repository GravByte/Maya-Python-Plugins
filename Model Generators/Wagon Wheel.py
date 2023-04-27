import maya.cmds as cmds

Wheel = cmds.polyPipe(r=6, h=6, t=1, ax = (1,0,0), sa = 18,ch=0, n= "Wheel");

startFace = 0;
lastFace = 17;

for i in range(startFace,lastFace,2):
    cmds.select(Wheel[0]+".f[%d]"%i,add=True)
   
cmds.polyExtrudeFacet(ltz=4,lsx=0.2,lsy=0.2)
cmds.select(clear=True)

for i in range(36,54,1):
    cmds.select(Wheel[0]+".f[%d]"%i,add=True)
    
cmds.polyExtrudeFacet(ltz=0.5,lsx=0.2)

cmds.select(Wheel)
cmds.delete(ch=True)

centreSmall = cmds.polyCylinder(ax=(1,0,0),r=1,h=3,n="CentreSmall",ch=False)
centreBig = cmds.polyCylinder(ax=(1,0,0),r=3,n="CentreBig",ch=False)

R_Wheel = cmds.group(Wheel,centreSmall,centreBig,n="R_Wheel")

cmds.move(-8.5,0,0, R_Wheel)

L_Wheel = cmds.duplicate(n="L_Wheel")

cmds.move(8.5,0,0, R_Wheel)

wheelLink= cmds.polyCylinder(ax=(1,0,0),r=0.5,h=21, n="wheelLink",ch=False)
cmds.select("L_Wheel","R_Wheel","wheelLink")
Wheels = cmds.group(n="Wheels")
cmds.move(0,6.5,0,Wheels)

for i in range(0,3,1):
    Plank = cmds.polyCube(w=3.75,h=0.72,d=30,n="Plank#")
    cmds.move(-4.15*i,7.25,0,Plank)
    
cmds.select("Plank*")
PlanksGrp = cmds.group(n="PlanksGrp")
cmds.move(4.15,0,0,r=True)
cmds.rotate(27,0,0,PlanksGrp)

cmds.group(Wheels,PlanksGrp,n="WagonWheel")
cmds.select(hi = True)
cmds.makeIdentity(apply=True,t=1,r=1,s=1,n=0,pn=1)

cmds.select(cl=True)
