from typing import Dict, List


def main():
    fs = FileSystem()

    # Read and process the file one line at a time to simulate a user
    # running these commands at a terminal
    with open('./command_input.txt', 'r') as commands:
        for command in commands:
            print(fs.process_command(command))

class FileSystem():

    def __init__(self):
        self.root: Directory = None
        self.seperator = '/'

    def process_command(self, command_str: str) -> str:
        command = tuple([x.strip() for x in command_str.split(' ')])
        
        if command[0] == 'LIST':
            return f'LIST\n{self.list()}'
        if command[0] == 'CREATE':
            if not self.root:
                self.root = Directory(command[1])
                return command_str
            if self.root.create(command[1]) is None:
                return command_str
            return f'error creating directory {command[1]}'
        if command[0] == 'MOVE':
            pass
        if command[0] == 'DELETE':
            pass
    
    def list(self) -> str:
        if self.root:
            return self.root.list()
        return ''

    def create(self, path: str) -> str:
        if self.root:
            dir_names = path.split(self.seperator)
            self.root.create(dir_names)
        self.root = Directory(path)
        return None
        

class Directory():

    def __init__(self, dir_name: str):
        self.name: str = dir_name
        self.subdirs: List[Directory] = []
    
    def create(self, dir_names: List[str]) -> bool:
        return True

    def list(self) -> str:
        output = self.name
        for dir in self.subdirs:
            output = f'{output}\n\t{dir.name}'
        return output

    def is_subdir(self, dir_name: str) -> bool:
        pass

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Directory) and o.name == self.name


main()