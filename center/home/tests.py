from django.test import TestCase, SimpleTestCase
import json
class SimpleTests(SimpleTestCase):
    def test_your_test(self):
        python_dict = {
            "1": {
                "id": "8a40135230f21bdb0130f21c255c0007",
                "hasmodel": "e3c3b78ac826184653aed562f1868f592b50e2980d56cf55a020dddc4130a138"
            }
        }
        response = self.client.post('/home/',
                                    json.dumps(python_dict),
                                    content_type="application/json")
