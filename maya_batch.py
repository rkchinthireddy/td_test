import maya.standalone
maya.standalone.initialize()

import maya.cmds as mc

def cube_test():
    cube = mc.polyCube()[0]
    print(f'{cube}..........created')

    cube_b = mc.duplicate(cube, n='CubeB')[0]
    print(f'{cube} duplicated and renamed as CubeB')

    mc.addAttr(cube, ln='showDuplicate', at='bool')
    mc.setAttr(f'{cube}.showDuplicate', e=1, k=1)
    print('Show Duplicate Attribute added')
    
    mc.parent(cube_b, cube)
    print(f'{cube_b} parented to {cube}')

    mc.setAttr(f'{cube_b}.tx', 10)
    print(f'{cube_b} moved 10 on X')

    mc.addAttr(cube_b, ln='duplicate', at='bool')
    mc.setAttr(f'{cube_b}.duplicate', e=1, k=1)
    print('Duplicate Attribute added')

    mc.connectAttr(f'{cube}.showDuplicate', f'{cube_b}.v')
    mc.connectAttr(f'{cube}.showDuplicate', f'{cube_b}.duplicate')
    print(f'{cube}.showDuplicate connected to {cube_b}.v')
    print(f'{cube}.showDuplicate connected to {cube_b}.duplicate')

    print('Query geometry of CubeB_________________')
    geometry_info = mc.polyEvaluate(cube_b, ae=True)
    for component, count in geometry_info.items():
        print(f'{component:<20}{count:>10}')

    mc.delete(f'{cube_b}.f[1]')
    print('='*100)
    save_path = input('*****Please Enter Save Path:')

    print('='*100)
    file_name = input('*****Please Enter File Name(ex: TestCube.ma):')

    path = f'{save_path}\{file_name}'

    mc.file(rename=path)
    mc.file( save=True, type='mayaAscii' )

    print(f'{path} ---------- file saved successfully')

cube_test()