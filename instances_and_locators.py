import maya.cmds as cmds


a = cmds.ls(os=True)
for i in range(0 , len(a)-1): 
    if cmds.objectType( cmds.listRelatives( a[i])) == 'locator':
        print i
        xPos = cmds.getAttr(a[i]+".tx")
        yPos = cmds.getAttr(a[i]+".ty")
        zPos = cmds.getAttr(a[i]+".tz")
        inst = cmds.instance( a[-1] , n='instanceTruc#')
        cmds.move( xPos, yPos, zPos, inst)
        print xPos 
        print yPos 
        print zPos 

'''
for i in cmds.ls(os=True):
    print cmds.xform( cmds.ls(os=True)[i] , q=True, t=True, ws=True )