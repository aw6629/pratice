def check_id(id):
    if len(id)  !=10:
        return False
    if not ( id[0].isupper()):
        return False
    if not (id[1] in '12'):
        return False
    for x in id[2:]:
        if not  x.isdigit():
            return False
    return True
import unittest
class MTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_id('A123456789'),True)
    def test_2(self):
        self.assertEqual(check_id('B123456789'),True)
    def test_3(self):
        self.assertEqual(check_id('C123456789'), True)
    def test_4(self):
        self.assertEqual(check_id('D523456789'), False)
    def test_5(self):
        self.assertEqual(check_id('D23456789'), False)
if __name__ =='__main__':
    unittest.main()