# Blogs API
## Getting Started
To test the api on heroku you can install and run postman collection from \<URL>

### Installing Dependencies
#### Python 3.8.6
#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python server.py
```

## Testing
To run the tests, run
```
python test_flaskr.py
```

## API Reference
### Getting Started
- Base URL: `https://limitless-capstone.herokuapp.com/blogs`
- Authentication: This app uses auth0.
### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": false,
    "error": 400,
    "message": "Bad Request"
}
```
The API will return one error type when requests fail:
- 401 Unauthorized
- 500 Internal Server Error
- 400 Bad Request
- 404 Not Found
### Endpoints
#### GET /blogs
- General:
    - Returns a list of blog objects and a success value.
- Sample `curl https://limitless-capstone.herokuapp.com/blogs`
```json
{
    "success": true,
    "blogs": [{
        "id": 11,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 12,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 13,
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 14,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 15,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 16,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 17,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 18,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 19,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    },
    {
        "id": 20,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    }]
}
```
#### GET /blogs/\<int:blog_id>
- General:
    - Returns a blog object with the given id, current user id and a success value.
- Sample `curl https://limitless-capstone.herokuapp.com/blogs/1`
```json
{
    "success": true,
    "user_id": "auth0|5f9efc5599d1f80076005f49",
    "blog": {
        "id": 1,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "This is an example title",
        "content": "This is an example content"
    }
}
```
#### POST /blogs
- General:
    - Creates a new blog using the submitted title and content. Returns a success value and the created object.
- Sample `curl -d "title=Example&content=Example" -X POST https://limitless-capstone.herokuapp.com/blogs`
```json
{
    "success": true,
    "blog": {
        "id": 1,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "Example",
        "content": "Example"
    }
}
```
#### PUT /blogs/\<int:blog_id>
- General:
    - Returns a blog object with the given id and a success value.
    - Update the blog with the submitted title, content.
- Sample `curl -d "title=Example&content=Example" -X PUT https://limitless-capstone.herokuapp.com/blogs/1`
```json
{
    "success": true,
    "blog": {
        "id": 1,
        "author_id": "auth0|5f9efc5599d1f80076005f49",
        "title": "Example",
        "content": "Example"
    }
}
```
#### DELETE /blogs/\<int:blog_id>
- General:
    - Delete the blog with the given id.
    - Returns a success value.
- Sample `curl -X DELETE https://limitless-capstone.herokuapp.com/blogs/1`
```json
{
    "success": true
}
```
## Author
Ahmed Alzubaidi <3
