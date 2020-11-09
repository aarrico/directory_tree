from typing import Dict, List, Set, Tuple, Union


class FileSystem():

    def __init__(self):
        self.root: Directory = None
        self.seperator = '/'

    def process_command(self, command_str: str) -> str:
        command = tuple([x.strip() for x in command_str.split(' ')])
        action = command[0]

        if action == 'LIST':
            return f'LIST\n{self.list()}'
        if action == 'CREATE':
            if self.create(command[1]) is None:
                return command_str
            return f'error creating directory {command[1]}'
        if action == 'MOVE':
            pass
        if action == 'DELETE':
            return self.delete(command[1])

    def list(self) -> str:
        if self.root:
            return str(self.root)
        return ''

    def create(self, path: str) -> str:
        if not self.root:
            self.root = Directory(path)
            return None

        dir_names = path.split(self.seperator)
        self.root.add_directory(dir_names)
        return None

    def delete(self, path: str) -> str:
        path_to_delete = path.split(self.seperator)
        (message, removed) = self.root.remove_directory(path_to_delete)
        if not removed:
            return f'Cannot delete {path} - \n{message} does not exist'
        return ''


class Directory():

    def __init__(self, dir_name: str):
        self.name: str = dir_name
        self.subdirs: Dict(str, Directory) = {}

    def add_directory(self, dir_names: List[str]) -> str:
        """Adds a subdirectory to the current directory. The new directory is the last element in the dir_names arg.

        Args:
            dir_names (List[str]): path to the new directory as a list

        Returns:
            str: will be empty if directory added successfully, otherwise it will return the first
            directory that could not be found in this directory's subdirs.
        """
        if self.name != dir_names[0]:
            return dir_names[0]

        first_subdir = dir_names[1]

        # If the path is only two items then we add the sub-directory
        if len(dir_names) == 2:
            self.subdirs[first_subdir] = Directory(first_subdir)
            return None
        if len(dir_names) > 2:
            if first_subdir in self.subdirs:
                return self.subdirs[first_subdir].add_subdirectory(dir_names[1:])
            else:
                return first_subdir

        return None

    def remove_directory(self, path_to_remove: List[str]):
        if self.name != path_to_remove[0]:
            return path_to_remove[0], False

        first_subdir = path_to_remove[1]
        if len(path_to_remove) == 2:
            try:
                return self.subdirs.pop(first_subdir).name, True
            except KeyError:
                return first_subdir, False
        if len(path_to_remove) > 2:
            if first_subdir in self.subdirs:
                return self.subdirs[first_subdir].remove_directory(path_to_remove[1:]), True

        return first_subdir, False

    def __str__(self) -> str:
        output = self.name

        # add indentation if a leaf subdir, otherwise recurse
        if not self.subdirs:
            return f'  {output}'
        for subdir in self.subdirs.values():
            output = f'{output}\n  {str(subdir)}'
        return output
