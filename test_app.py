import os
import json
import unittest
from models.blog import setup_db, db, Blog
from server import app

# result = self.client().get('/questions?page=1')
# result = self.client().post('/quizzes', json={
#             'previous_questions': [blog.id],
#             'quiz_category': {
#                 'id': blog.category,
#             }
#         })
# self.assertEqual(result.status_code, 200)
# self.assertEqual(data['success'], True)
# self.assertIsNotNone(data['questions'])


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZNYjVTYWF6bDVGUDczbjJtUWF5WCJ9\
        .eyJpc3MiOiJodHRwczovL2Rldi1jaTV6NnpvNC5ldS5hdXRoMC5jb20vIiwic3ViIjoieUZlNEFvakFIdVdRekh3VWZQR1FkQzVKZ\
        3dWVFBIRGhAY2xpZW50cyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiaWF0IjoxNjA0NDAyNDExLCJleHAiOjE2MDQ0ODg4M\
        TEsImF6cCI6InlGZTRBb2pBSHVXUXpId1VmUEdRZEM1Smd3VlRQSERoIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.FDkK5m\
        AHYAww-JO_S2wWnvSVnubsoblVuypEH89mCA6I4Pb6Xtw_I2bf0Mgg8dgkvr9pPN2Ke2VmyyiOrGb2wzji6hsetElI2uetXf2YcJqg\
        _07bX_0AjRHZFHQy5otcbQEkQ6PUw8RPcH3jNgtoT4HYQyUJpeE7T3jG_ugqtMDRh7RhJikuDpTuczYA484tOkQfBKb0v_cGiDlo1E\
        N5TQUsqKZq9QXwFyPxNvURNjS-f2hfd8v1bgC_BTEK2NmyEHrt5IfttC7ooSKH-g_wTb7Z6eGLkJiv4zIaqWF66kVUoOS54MWalrnt\
        CyElk3c6CSPD2YJyIwwAJ_-1ZBG6rw'
    }

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.app.config['DEBUG'] = False
        self.client = self.app.test_client
        self.database_path = 'postgres://jguyipenxdzxig:ef1a95cfcbc265ae17ad55d95f7\
        ba4b794e1d03f58940c2df9f9c9216509b2e2@ec2-54-166-114-48.compute-1.amazonaws.\
        com:5432/d9u9sernqgqat8'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = db

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_all_blog(self):
        result = self.client().get('/blogs')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['blogs'])

    def test_get_blog(self):
        result = self.client().get('/blogs/1')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_store_blog(self):
        result = self.client().post('/blogs', headers=self.headers)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNone(data['blog'])

    def test_edit_blog(self):
        result = self.client().put('/blogs/1', headers=self.headers, json={
            'title': '',
            'content': ''
        })
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_blog(self):
        result = self.client().delete('/blogs/1', headers=self.headers)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    # Note there is no proper way to test a fail scenario for getting all blogs

    def test_get_blog_fail(self):
        result = self.client().get('/blogs/999')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_store_blog_fail(self):
        result = self.client().post('/blogs')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 400)
        self.assertEqual(data['success'], True)

    def test_delete_blog_fail(self):
        result = self.client().get('/blogs/999', headers=self.headers)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
