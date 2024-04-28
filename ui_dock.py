import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore

class ObjectNamePrinter(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ObjectNamePrinter, self).__init__(parent)
        
        self.setWindowTitle("Object Name Printer")
        self.setObjectName("ObjectNamePrinter")
        self.resize(200, 50)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
    def create_widgets(self):
        self.print_button = QtWidgets.QPushButton("Print Selected Object Name")
        
    def create_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.print_button)
        self.setLayout(layout)
        
    def create_connections(self):
        self.print_button.clicked.connect(self.print_selected_object_name)
        
    def print_selected_object_name(self):
        selected_objects = cmds.ls(selection=True)
        if selected_objects:
            print("Selected Object Name:", selected_objects[0])
        else:
            print("No object selected.")

def launch_object_name_printer():
    global object_name_printer_window
    try:
        object_name_printer_window.close()
    except:
        pass
    object_name_printer_window = ObjectNamePrinter()
    object_name_printer_window.show()
    allowedAreas = ['right', 'left']
    if mc.dockControl('TestDockCtrl', ex=1):
        mc.deleteUI('TestDockCtrl', ctl=True)
    mc.dockControl('TestDockCtrl', l='Object Name Printer', area='left', content='ObjectNamePrinter', allowedArea=allowedAreas )

launch_object_name_printer()
