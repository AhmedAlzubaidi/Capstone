import os
import json
import unittest
from models.blog import setup_db, db, Blog
from app import app

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
        'Authorization': os.environ.get('ADMIN_TOKEN')
    }

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.app.config['DEBUG'] = False
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = f'postgres://postgres:root@localhost:5432/{self.database_name}'
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
