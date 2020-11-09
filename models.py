from __future__ import annotations
from typing import Dict, List, Optional, Tuple


class FileSystem():
    """Supports four basic operations on a file system. It contains a repo parameter that allows the
    data structure to be switched out as long as the repo class implements the appropriate methods:
        -find(path_parts: List[str])
        -add_directory(path_parts: List[str])
        -delete_directory(path_parts: List[str])
        -get_as_string(default_tab: str)
    where path_parts is the path split into a list and default_tab is the tab width represented in a string.
    """

    def __init__(self):
        self.repo: DirectoryTree = DirectoryTree()
        self.seperator = '/'
        self.tab = '  '

    def process_command(self, command_str: str) -> str:
        command = tuple([x.strip() for x in command_str.split(' ')])
        action = command[0]

        if action == 'LIST':
            return self.list()
        if action == 'CREATE':
            self.create(command[1])
            return command_str
        if action == 'MOVE':
            message = self.move(command[1], command[2])
            if message:
                return f'{command_str}\n{message}'
            return command_str
        if action == 'DELETE':
            message = self.delete(command[1])
            if message:
                return f'{command_str}{message}'
            return command_str

    def list(self) -> str:
        return f'LIST\n{self.repo.get_as_string(default_tab=self.tab)}'

    def create(self, path: str) -> None:
        path_parts = path.split(self.seperator)
        self.repo.add_directory(path_parts)

    def delete(self, path: str) -> Optional[str]:
        path_parts = path.split(self.seperator)
        (removed, message) = self.repo.delete_directory(path_parts)
        if not removed:
            return f'Cannot delete {path} - \n{message} does not exist'
        return None

    def move(self, src_path: str, dest_path: str) -> Optional[str]:
        src_parts = src_path.split(self.seperator)
        src_name = src_parts[-1]
        src_dir = self.repo.find(src_parts)
        if not src_dir:
            return f'Cannot move {src_path}'

        dest_dir = self.repo.find(dest_path.split(self.seperator))
        if not dest_dir:
            return f'Cannot move {dest_path}'

        src_parent = self.repo.find(src_parts[:len(src_parts)-1])
        dest_dir.subdirs[src_name] = src_parent.subdirs.pop(src_name)

        return None


class Directory:

    def __init__(self):
        self.subdirs: Dict[str, Directory] = {}

    def is_leaf(self):
        return bool(self.subdirs)


class DirectoryTree:
    def __init__(self):
        self.root = Directory()

    def find(self, path_parts: List[str]) -> Optional[Directory]:
        dir = self.root
        for part in path_parts:
            if part not in dir.subdirs:
                return None
            dir = dir.subdirs[part]
        return dir

    def add_directory(self, path_parts: List[str]) -> None:
        dir = self.root
        for part in path_parts:
            if part not in dir.subdirs:
                dir.subdirs[part] = Directory()
            dir = dir.subdirs[part]

    def delete_directory(self, path_parts: List[str]) -> Tuple[bool, str]:
        parent_path = path_parts[:len(path_parts)-1]
        parent = self.find(parent_path)
        if not parent:
            return False, parent_path[0]
        dir_to_delete = path_parts.pop()
        if dir_to_delete in parent.subdirs:
            del parent.subdirs[dir_to_delete]
            return True, dir_to_delete
        return False, dir_to_delete

    def get_as_string(self, default_tab: str) -> str:

        def _get_as_string(root: Directory, depth: int) -> List[str]:
            tree = []
            tab = self._get_multiple_tab(depth, default_tab)
            for name, dir in root.subdirs.items():
                if dir.is_leaf:
                    tree.append(f'{tab}{name}')
                for subtree in _get_as_string(dir, depth+1):
                    tree.append(subtree)
            return tree

        return '\n'.join(_get_as_string(self.root, 0))

    @staticmethod
    def _get_multiple_tab(depth: int, default_tab: str):
        tab = ''
        for i in range(depth):
            tab = f'{default_tab}{tab}'
        return tab
