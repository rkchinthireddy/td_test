Task01------------- pyls. (completed 1 to 6)
        Installation
        Download the pyls.py and structure.json files.
        Copy both files into your Python installation path. If you're unsure of your Python installation path, 
        you can find it by running the following Python code:

        import sys
        print(sys.executable)
        
        Once installed, you can use pyls to list files and directories in different ways. Here are some example commands:
        
        To list files and directories:
        
        $ python -m -pyls
        $ python -m -pyls -A
        $ python -m -pyls -l
        $ python -m -pyls -l -r
        $ python -m -pyls -l -r -t
        $ python -m -pyls -l -r -t --filter=dir
        $ python -m -pyls -l -r -t --filter=file

Task02------------- MAYA SETUP
        without updating userSetup.mel and Maya.env

        1. we can add custom paths to PYTHONPATH by using

                import sys
                sys.path.append('path/scripts')
                
        2. add MAYA_SCRIPT_PATH, PYTHONPATH paths to sysyem environment variables
        3. Module Path Configuration:Maya supports the use of module files to specify additional paths for plugins, scripts, and other resources. 
           create a module file (.mod) that points to your custom plugins and scripts folder. 
           Create a new .mod file in your Maya modules directory (usually located in <Maya install directory>\modules).
           Edit the .mod file to include the path to your custom plugins and scripts folder.
           Restart Maya, and it will automatically recognize and load the modules.
           Example .mod file contents:

                + easy_rigger 1.0 D:\maya\scripts\easy_rigger
                scripts: D:\maya\scripts\easy_rigger

Task03------------- MAYA BATCH
        Installation and editing

        Download the maya_batch.py and maya_bat.bat files.
        Open the maya_bat.bat file in a text editor.
        Edit the file to specify the correct path to the mayapy.exe executable and the maya_batch.py script. 
        Replace the placeholder paths with the actual paths where Maya and the script are installed.
        Save the changes to the maya_bat.bat file.
        
        Usage:
        
        To use the Maya Batch Processing Tool, follow these steps:
        
        Double-click the maya_bat.bat file to run it.
        The tool will prompt you to enter the path where you want to save the output file.
        Enter the desired path and press Enter.
        Next, the tool will ask you to enter the name for the output file.
        Enter the desired name for the file and press Enter.
        Maya will launch in batch mode and execute the tasks defined in the maya_batch.py script.
        Once the processing is complete, the tool will display a message indicating that the batch process has finished.

Task04------------- Moving Selected Object in X and Y axis using OM

        to use this script download the move_objects_OM.py and run in tha maya python script editor

Task05------------- Print selected object button with Qt UI, Can be docked into the Maya UI
        to use this script download the ui_dock.py and run in tha maya python script editor. 

Task06------------- test Threading 
        To use the Threading Test Script for Maya, follow these steps:

        Download the ui_threading.py and create_cube.py files.
        Open the ui_threading.py file in a text editor.
        Edit line 34 of the file to specify the path to the create_cube.py script. 
        Replace the placeholder path with the actual path where the create_cube.py script is located.

                34. script_path = "D:/zuru/pipeline/create_cube.py"

        Save the changes to the ui_threading.py file.

        ***The create_cube.py script provided with this tool is used for testing purposes and can be replaced with any other script.

        Usage
        
        Open the ui_threading.py script in the Maya Python Script Editor.
        Run the script  in the Script Editor .
        A window titled "Maya Script Runner" will appear with a button labeled "Run Script From Maya".
        Double-click the "Run Script From Maya" button.
        A new Maya will launch, and the create_cube.py script will be executed in a separate thread.
        While the script is running, you can continue working in the original Maya session without freezing the interface.

                
