import maya.cmds as cmds


try:
    if cmds.window(window, exists = True):
        cmds.deleteUI(window)
except NameError:
    print ("ERROR")

#Create Stairs Function
def createStairs():
    steps = []
    sCount = cmds.intSliderGrp( stepCountISG, query=True, value=True )
    vValue = cmds.intSliderGrp( curValueISG, query=True, value=True )

    for i in range(sCount):
        step = cmds.polyCube(n="step#",w=8,d=2,h=0.5,ch=False)[0]
        cmds.move(0,0.5*i,2*i)
        steps.append(step)

    cmds.select(steps)  
    Steps_Grp = cmds.group(n="step_Grp")
    bendNL = cmds.nonLinear(Steps_Grp,type='bend',curvature=vValue)
    cmds.rotate(-90,0,0,bendNL)
    cmds.delete(Steps_Grp,ch=True)
    
    #Create Wagon Function
def createWagon():
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
    
def createStreetLight():
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

# Make a new window

window = cmds.window( t="CreateModels", widthHeight=(400, 600),s=False )
cmds.columnLayout( adjustableColumn=True )
#Access Logo image using internalVar
logoPath = cmds.internalVar(upd=True)+"icons/logo.png"
cmds.image(w=400,h=100,image=logoPath)
#Create window buttons, sliders and separators
cmds.separator(height=10, style='out')
cmds.text(l="Create a Staircase" ,bgc=(0.3,0.5,0.7),h=45)
cmds.separator(height=10, style='out')
stepCountISG = cmds.intSliderGrp( field=True, label='Num Steps', min=2, max=100, value=0 )
cmds.separator(height=10, style='out')
curValueISG = cmds.intSliderGrp( field=True, label='Curvature Value', min=-180, max=180, value=0 )
cmds.separator(height=10, style='out')
cmds.symbolButton(image='stairs.png', c="createStairs()")
#cmds.button( label='Create Stairs' ,h=100,c="CreateStairs()")
cmds.separator(height=10, style='in')
cmds.symbolButton(image='wagon.png', c="createWagon()")
cmds.separator(height=10, style='in')
cmds.symbolButton(image='wagon.png', c="createStreetLight()")
cmds.separator(height=10, style='in')
cmds.text(l="Created by Brandon")
cmds.separator(height=10, style='in')
cmds.showWindow( window )