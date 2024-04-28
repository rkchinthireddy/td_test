import json
import sys
import datetime as dt

class GetJsonInfo:
    """
    A class to parse and display information from a JSON file representing file structure.
    """

    def __init__(self, json_path):
        """
        Args:
        json_path (str): The path to the JSON file.

        """
        self.json_path = json_path
        self.print_data = {}  # Data to be printed after parsing

    def load_json(self):
        """Load the JSON file."""
        try:
            with open(self.json_path, 'r') as open_file:
                self.json_object = json.load(open_file)
        except FileNotFoundError:
            print(f"Error: File '{self.json_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: '{self.json_path}' is not a valid JSON file.")

    def ls_parser(self):
        """
        Parse and print the contents of the JSON file.

        Ignores hidden files (those starting with '.').
        """
        self.load_json()
        contents = self.json_object['contents']
        for each in contents:
            name = each['name']
            if not name.startswith('.'):
                print(name)

    def a_parser(self):
        """
        Parse and print all contents of the JSON file, including hidden files.
        """
        self.load_json()
        contents = self.json_object['contents']
        for each in contents:
            print(each['name'])

    def l_r_t_parser(self):
        """
        Parse and print the contents of the JSON file with options for sorting and reversing.

        Sorts by modification time if '-t' option is provided.
        Reverses the order if '-r' option is provided.
        """
        self.load_json()
        contents = self.json_object['contents']

        # reverse dict
        if '-r' in sys.argv: 
            contents = self.json_object['contents'][::-1]
        
        # sorting as oldest first
        if '-t' in sys.argv: 
            contents.sort(key=lambda x: x['time_modified'], reverse=True)
        
        for each in contents:
            name = each['name']
            if not name.startswith('.'):
                time_code = each['time_modified']
                time_obj = dt.datetime.fromtimestamp(time_code)
                time_format = time_obj.strftime('%b %d %H:%M')
                self.print_data[name] = (time_format, each['size'], each['permissions'])
                print(f"{each['permissions']}{each['size']:>10}{time_format:>15}   {name}")

    def filter_parser(self, filter_option):
        """
        Args:
        filter_option (str): The filter option. Should be 'dir' or 'file'.

        """
        self.load_json()
        contents = self.json_object['contents']
        filtered_content = []
        for each in contents:
            name = each['name']
            if filter_option == 'dir':
                if 'contents' in each:
                    if not name.startswith('.'):
                        time_code = each['time_modified']
                        time_obj = dt.datetime.fromtimestamp(time_code)
                        time_format = time_obj.strftime('%b %d %H:%M')
                        self.print_data[name] = (time_format, each['size'], each['permissions'])
                        print(f"{each['permissions']}{each['size']:>10}{time_format:>15}   {name}")
            elif filter_option == 'file':
                if 'contents' not in each:
                    if not name.startswith('.'):
                        time_code = each['time_modified']
                        time_obj = dt.datetime.fromtimestamp(time_code)
                        time_format = time_obj.strftime('%b %d %H:%M')
                        self.print_data[name] = (time_format, each['size'], each['permissions'])
                        print(f"{each['permissions']}{each['size']:>10}{time_format:>15}   {name}")
            else:
                print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
                sys.exit()
        return filtered_content

def main():
    """
    Main function to execute the program.
    """
    json_path = "structure.json"
    print_data = GetJsonInfo(json_path)

    # Parsing command line arguments
    if '-A' not in sys.argv and '-l' not in sys.argv:
        print_data.ls_parser()
    if '-A' in sys.argv:
        print_data.a_parser()
    if '-l' in sys.argv:
        filter_option = None
        for arg in sys.argv:
            if arg.startswith("--filter="):
                filter_option = arg.split("=")[1]

        if filter_option:
            x = print_data.filter_parser(filter_option)
        else:
            print_data.l_r_t_parser()

if __name__ == "__main__":
    main()
