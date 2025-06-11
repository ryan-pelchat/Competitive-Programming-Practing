import addEmUp

import unittest


class TestAddEmUp(unittest.TestCase):
    def test_addEmUp(self):
        self.assertEqual(addEmUp.main(4, 66, ["15", "21", "22", "15"]), True)
        self.assertEqual(addEmUp.main(3, 66, ["15", "22", "22"]), False)


if __name__ == "__main__":
    unittest.main()
