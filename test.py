import unittest
from main import autocorrect


class testautocorrect(unittest.TestCase):

  def test_blank(self):
    self.assertFalse(autocorrect(" ", 'da words.txt'))



if __name__ == '__main__':
    unittest.main()