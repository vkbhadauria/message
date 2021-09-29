from django.test import TestCase
import json

class MessageTestCase(TestCase):
    def setUp(self):
        data = {
            "mobile": "12345",
            "first_name": "test",
            "last_name": "",
            "password": "test"
            }
        self.message_body = {
                "message":{
                    "text": "test",
                    # "media": None,
                    "message_type": "text"
                },
                    "reciever_mobile": "1234"
                }
        self.do_signup(data)
        self.do_login(username=data['mobile'],password=data['password'])


    def do_signup(self,body):
        res=self.client.post('/signup', body)


    def do_login(self,username, password):
        res=self.client.post('/login', {"mobile":username,"password":password})

    def test_message_list(self):
        res=self.client.get('/message')
        self.assertEqual(res.status_code, 200)

    def test_message_send(self):               
        res=self.client.post('/message', data=json.dumps(self.message_body), content_type='application/json')
        self.assertEqual(res.status_code, 201)
