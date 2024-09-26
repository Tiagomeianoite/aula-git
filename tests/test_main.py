import unittest

from main import soma

class TestSoma(unittest.TestCase): def test_soma(self): self.assertEqual(soma(2, 3), 5)

if name == 'main': unittest.main()
