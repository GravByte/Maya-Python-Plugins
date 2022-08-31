import maya.cmds as cmds

#If window is reopened whilst already open, it will close previous window
try:
    if cmds.window(window, exists = True):
        cmds.deleteUI(window)
except NameError:
    print ("ERROR")

#Create Desk
def createDesk():
    #DeskTop
    DskTop = cmds.polyCube(w=8,h=0.2,d=4,n="DskTop") [0]
    cmds.move(0,2,0,DskTop)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    #DeskRightSupport
    DskSpptR = cmds.polyCube(w=0.4,h=2,d=3.8,n="DskSpptR") [0]
    cmds.move(3.75,1,0,DskSpptR)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    DskSpptL = cmds.polyCube(w=2,h=2,d=3.8,n="DskSpptL") [0]
    cmds.move(-2.95,1,0,DskSpptL)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    DskSupports_Grp = cmds.group(DskSpptR,DskSpptL,n="DskSupports_Grp")
    #DeskDrawers Top,Middle,Bottom
    DskDrwT = cmds.polyCube(w=1.8,h=0.5,d=0.2,n="DskDrwT") [0]
    cmds.move(-2.95,1.55,2,DskDrwT)
    DskDrwM = cmds.duplicate(n="DskDrwM")
    cmds.move(-2.95,1,2,DskDrwM)
    DskDrwB = cmds.duplicate(n="DskDrwB")
    cmds.move(-2.95,0.45,2,DskDrwB)
    cmds.select(DskDrwT,DskDrwM,DskDrwB)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    DskDrawers_Grp = cmds.group(DskDrwT,DskDrwM,DskDrwB,n="DskDrawers_Grp")
    #DeskGroup
    Desk_Grp = cmds.group(DskTop,DskSupports_Grp,DskDrawers_Grp,n="Desk_Grp")
    
#Create ComputerDesk with Desk, Computer tower, Monitor & Keyboard
def createComputerDesk():
    
    #DeskTop
    DskTop = cmds.polyCube(w=8,h=0.2,d=4,n="DskTop") [0]
    cmds.move(0,2,0,DskTop)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    #DeskRightSupport
    DskSpptR = cmds.polyCube(w=0.4,h=2,d=3.8,n="DskSpptR") [0]
    cmds.move(3.75,1,0,DskSpptR)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    DskSpptL = cmds.polyCube(w=2,h=2,d=3.8,n="DskSpptL") [0]
    cmds.move(-2.95,1,0,DskSpptL)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    DskSupports_Grp = cmds.group(DskSpptR,DskSpptL,n="DskSupports_Grp")
    #DeskDrawers Top,Middle,Bottom
    DskDrwT = cmds.polyCube(w=1.8,h=0.5,d=0.2,n="DskDrwT") [0]
    cmds.move(-2.95,1.55,2,DskDrwT)
    DskDrwM = cmds.duplicate(n="DskDrwM")
    cmds.move(-2.95,1,2,DskDrwM)
    DskDrwB = cmds.duplicate(n="DskDrwB")
    cmds.move(-2.95,0.45,2,DskDrwB)
    cmds.select(DskDrwT,DskDrwM,DskDrwB)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    DskDrawers_Grp = cmds.group(DskDrwT,DskDrwM,DskDrwB,n="DskDrawers_Grp")
    
    #DeskGroup
    Desk_Grp = cmds.group(DskTop,DskSupports_Grp,DskDrawers_Grp,n="Desk_Grp")
    
     
    #Monitor
    monitorStand = cmds.polyCube(w=1,h=0.1,d=0.8,n="monitorStand") [0]
    cmds.move(0.7,2.15,-1.1,monitorStand)
    monitorStandSppt = cmds.polyCube(w=0.2,h=1.5,d=0.1,n="monitorStandSppt") [0]
    cmds.move(0.68,2.95,-1.29,monitorStandSppt)
    Monitor = cmds.polyCube(w=2,h=1,d=0.1,n="Monitor") [0]
    cmds.move(0.7,3.58,-1.2,Monitor)
    cmds.select(monitorStand,monitorStandSppt,Monitor)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    Monitor_Grp = cmds.group(monitorStand,monitorStandSppt,Monitor,n="Monitor_Grp")
    
    #Keyboard
    Keyboard = cmds.polyCube(w=1.5,h=0.1,d=0.8,n="Keyboard") [0]
    cmds.move(0.7,2.15,1.11,Keyboard)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    #Computer Tower
    compTower = cmds.polyCube(w=0.8,h=1.5,d=2,n="compTower") [0]
    cmds.move(3.2,2.85,-0.796,compTower)
    cmds.rotate(0,16.215,0,compTower)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    
    #Group Computer Desk
    compDesk_Grp = cmds.group(Desk_Grp,Monitor_Grp,Keyboard,compTower,n="compDesk_Grp")
    
#Create Chair
def createChair():
    #Seat
    chairSeat = cmds.polyCube(w=2,h=0.2,d=2.5,n="chairSeat") [0]
    cmds.move(0,1.6,0,chairSeat)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    #Back
    chairBack = cmds.polyCube(w=1.95,h=2,d=0.3,n="chairBack") [0]
    cmds.move(0,2.676,1.193,chairBack)
    cmds.rotate(7.434,0,0,chairBack)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    #Arms back & front
    chairArmRB = cmds.polyCube(w=0.2,h=0.2,d=1.5,n="chairArmRB") [0]
    cmds.move(1.082,2.298,0.521,chairArmRB)
    chairArmRF = cmds.polyCube(w=0.2,h=0.2,d=1.1,n="chairArmRF") [0]
    cmds.move(1.09,1.954,-0.562,chairArmRF)
    cmds.rotate(-42.244,0,0,chairArmRF)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    chairArmR_Grp = cmds.group(chairArmRB,chairArmRF,n="chairArmR_Grp")
    chairArmLB = cmds.duplicate(chairArmRB,n="chairArmLB")
    cmds.move(-1.077,2.298,0.521,chairArmLB)
    chairArmLF = cmds.duplicate(chairArmRF,n="chairArmLF")
    cmds.move(-2.164,0,0,chairArmLF)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    chairArmL_Grp = cmds.group(chairArmLB,chairArmLF,n="chairArmL_Grp")
    #Group Seat
    chairSeat_Grp = cmds.group(chairSeat,chairBack,chairArmR_Grp,chairArmL_Grp,n="chairSeat_Grp")
    
    #Legs & Pole
    chairPole = cmds.polyCylinder(r=0.2,h=1.5,n="chairPole") [0]
    cmds.move(0,0.85,0.31,chairPole)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    chairLeg_1 = cmds.polyCube(w=1,h=0.2,d=0.2,n="chairLeg_1") [0]
    cmds.move(-0.639,0.152,0.3,chairLeg_1)
    cmds.rotate(0,0,7,chairLeg_1)
    chairLeg_2 = cmds.duplicate(chairLeg_1,n="chairLeg_2") [0]
    cmds.move(-0.211,0.17,0.884,chairLeg_2)
    cmds.rotate(11.289,69.4,13.23,chairLeg_2)
    chairLeg_3 = cmds.duplicate(chairLeg_1,n="chairLeg_3") [0]
    cmds.move(0.472,0.176,0.724,chairLeg_3)
    cmds.rotate(-4.434,137.59,-6.73,chairLeg_3)
    chairLeg_4 = cmds.duplicate(chairLeg_1,n="chairLeg_4") [0]
    cmds.move(0.538,0.187,-0.08,chairLeg_4)
    cmds.rotate(2.34,214.66,-5.864,chairLeg_4)
    chairLeg_5 = cmds.duplicate(chairLeg_1,n="chairLeg_5") [0]
    cmds.move(-0.18,0.17,-0.29,chairLeg_5)
    cmds.rotate(-196.1,251.512,197.613,chairLeg_5)
    cmds.select(chairLeg_1,chairLeg_2,chairLeg_3,chairLeg_4,chairLeg_5)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    chairBase_Grp = cmds.group(chairPole,chairLeg_1,chairLeg_2,chairLeg_3,chairLeg_4,chairLeg_5,n="chairBase_Grp")
    #GroupChair
    Chair_Grp = cmds.group(chairSeat_Grp,chairBase_Grp,n="Chair_Grp")
    
#Create file cabinet
def createFileCabinet():
    cabinetShell = cmds.polyCube(w=3,h=6,d=2,n="cabinetShell") [0]
    cmds.move(0,3,0,cabinetShell)
    cabinetDrawer_1 = cmds.polyCube(w=2.8,h=1.3,d=1.9,n="cabinetDrawer_1") [0]
    cmds.move(0,1,0.145,cabinetDrawer_1)
    cabinetDrawer_2 = cmds.duplicate(cabinetDrawer_1,n="cabinetDrawer_2") [0]
    cmds.move(0,2.36,0.145,cabinetDrawer_2)
    cabinetDrawer_3 = cmds.duplicate(cabinetDrawer_1,n="cabinetDrawer_3") [0]
    cmds.move(0,3.73,0.145,cabinetDrawer_3)
    cabinetDrawer_4 = cmds.duplicate(cabinetDrawer_1,n="cabinetDrawer_4") [0]
    cmds.move(0,5.1,0.145,cabinetDrawer_4)
    cmds.select(cabinetShell,cabinetDrawer_1,cabinetDrawer_2,cabinetDrawer_3,cabinetDrawer_4)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    fileCabinet_Grp = cmds.group(cabinetShell,cabinetDrawer_1,cabinetDrawer_2,cabinetDrawer_3,cabinetDrawer_4,n="fileCabinet_Grp")
    
#Create Lamp
def createLamp():
    lampBase = cmds.polyCylinder(r=0.4,h=0.4,n="lampBase") [0]
    cmds.move(0,0.2,0,lampBase)
    lampStand = cmds.polyCylinder(r=0.2,h=2,n="lampStand") [0]
    cmds.move(0,1,0,lampStand)
    lampShade = cmds.polyCylinder(r=0.8,h=1,n="lampShade") [0]
    cmds.move(0,1.8,0,lampShade)
    cmds.select(lampBase,lampStand,lampShade)
    cmds.delete(ch=1)
    cmds.makeIdentity(t=1,r=1,s=1,apply=True)
    Lamp_Grp = cmds.group(lampBase,lampStand,lampShade,n="Lamp_Grp")
    

# Make a new window

window = cmds.window( t="AssetGenerator", widthHeight=(400, 750),s=False )
cmds.columnLayout( adjustableColumn=True )
#Access Logo image using internalVar
logoPath = cmds.internalVar(upd=True)+"icons/BGlogoBanner.png"
cmds.image(w=400,h=100,image=logoPath)
#Create window buttons and separators
cmds.separator(height=10, style='out')
cmds.text(l="Create an office!" ,bgc=(0.3,0.5,0.7),h=45)
cmds.separator(height=10, style='out')
cmds.symbolButton(image='DeskButton_Banner.png', c="createDesk()")
cmds.separator(height=10, style='in')
cmds.symbolButton(image='ComputerDeskButton_Banner.png', c="createComputerDesk()")
cmds.separator(height=10, style='in')
cmds.symbolButton(image='ChairButton_Banner.png', c="createChair()")
cmds.separator(height=10, style='in')
cmds.symbolButton(image='FileCabinetButton_Banner.png', c="createFileCabinet()")
cmds.separator(height=10, style='in')
cmds.symbolButton(image='LampButton_Banner.png', c="createLamp()")
cmds.separator(height=10, style='in')
cmds.text(l="Created by Brandon Nyman")
cmds.separator(height=10, style='in')
cmds.showWindow( window )