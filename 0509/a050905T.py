import unittest
from a050902 import app
class MTestCase(unittest.TestCase):
    # def test1(self):
    #     app.testing = True
    #     response =app.test_client().get('/')
    #     print(type(response.data))
    #     print(response.data)
    #     source=response.data.decode('UTF-8')
    #     print(source)
    #     print(type(source))
    #     self.assertEqual(response.status_code,200)
    def test2(self):
        app.testing =True
        response= app.test_client().post('/add',data ={'a':1,'b':4})
        data=response.data.decode('UTF-8')
        self.assertEqual(data,'5')
if __name__=='__main__':
    unittest.main()