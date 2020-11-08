import unittest
from filesystem_sim import FileSystem

class TestList(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_list_if_no_dir_exists(self):
        self.assertEqual(self.fs.process_command('LIST'), 'LIST\n')

    def test_list_directory_after_creating_dir(self):
        self.fs.process_command('CREATE pugs')
        self.assertEqual(self.fs.process_command('LIST'), 'LIST\npugs')

    def test_list_dir_with_subdir(self):
        self.fs.process_command('CREATE pugs')
        self.fs.process_command('CREATE pugs/stella')
        self.assertEqual(self.fs.process_command('LIST'), 'LIST\npugs\n\tstella')

class TestCreate(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
    
    def test_creating_root(self):
        self.assertEqual(self.fs.process_command('CREATE pugs'), 'CREATE pugs')
    
    def test_creating_subdir(self):
        self.assertEqual(self.fs.process_command('CREATE pugs/stella'), 'CREATE pugs/stella')

    # def test_move_directory(self):
    #     self.assertEqual(self.fs.process_command('MOVE pugs dogs'), 'MOVE pugs dogs')

    # def test_delete_directory(self):
    #     self.assertEqual(self.fs.process_command('DELETE pugs'), 'DELETE pugs')

if __name__ == '__main__':
    unittest.main()