import unittest
from directories import process_command

class TestCommand(unittest.TestCase):
    def test_process_command(self):
        self.assertEqual(process_command('LIST'), '')