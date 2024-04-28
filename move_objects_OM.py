import maya.OpenMaya as om
import maya.cmds as mc

def move_objects(x_val, y_val):
    selection_list = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection_list)

    if selection_list.length() == 0:
        print('Please select an object')
        return

    mc.undoInfo(openChunk=True)  

    try:
        for i in range(selection_list.length()):
            dag_path = om.MDagPath()
            selection_list.getDagPath(i, dag_path)
            transform_fn = om.MFnTransform(dag_path)
            print(transform_fn.name())
            transform_fn.translateBy(om.MVector(x_val, y_val, 0), om.MSpace.kTransform)
    finally:
        mc.undoInfo(closeChunk=True)  

def move_face(obj_name, face_index, offset_value):
    selection_list = om.MSelectionList()
    selection_list.add(obj_name)
    dag_path = om.MDagPath()
    selection_list.getDagPath(0, dag_path)

    mesh_fn = om.MFnMesh(dag_path)
    print(mesh_fn.name())

    vertex_indices = om.MIntArray()
    mesh_fn.getPolygonVertices(face_index, vertex_indices)

    mc.undoInfo(openChunk=True)  

    try:
        for vertex_index in vertex_indices:
            point = om.MPoint()
            mesh_fn.getPoint(vertex_index, point, om.MSpace.kTransform)
            point += om.MVector(0, 0, offset_value)
            mesh_fn.setPoint(vertex_index, point, om.MSpace.kTransform)
    finally:
        mc.undoInfo(closeChunk=True)  

def undo_all():
    mc.undo()

move_objects(1, 1)
move_face('pCube1', 0, 4)