from Parser import Parser 
import unittest
from test import support

class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser("../add/Add.asm")

if __name__ == '__main__':
    unittest.main()
