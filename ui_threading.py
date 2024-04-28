import threading
import subprocess

from PySide2 import QtWidgets, QtCore

class MayaScriptRunner(QtWidgets.QWidget):
    def __init__(self):
        super(MayaScriptRunner, self).__init__()
        
        self.setWindowTitle("Maya Script Runner")
        self.setObjectName("MayaScriptRunner")
        self.resize(200, 50)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
    def create_widgets(self):
        self.run_button = QtWidgets.QPushButton("Run Script from Maya")
        
    def create_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.run_button)
        self.setLayout(layout)
        
    def create_connections(self):
        self.run_button.clicked.connect(self.run_maya_script)
        
    def run_maya_script(self):
        # maya installed path
        maya_executable = "C:/Program Files/Autodesk/Maya2023/bin/maya.exe"  
        
        # script path that execute after launching maya
        script_path = "D:/zuru/pipeline/create_cube.py"
        
        threading.Thread(target=self.execute_script_in_maya, args=(maya_executable, script_path)).start()
        
    def execute_script_in_maya(self, maya_executable, script_path):
        subprocess.Popen([maya_executable, "-command", "python(\"exec(open('{}').read())\")".format(script_path)])
        print('done')
        
def launch_maya_script_runner():
    global maya_script_runner_window
    try:
        maya_script_runner_window.close()
    except:
        pass
    maya_script_runner_window = MayaScriptRunner()
    maya_script_runner_window.show()

launch_maya_script_runner()
