import maya.cmds as mc
def create_cube():
    mc.polyCube()

    print('DONE')
    
mc.evalDeferred(create_cube)