# Django REST Framework Todo List

This project is a simple Todo List API implemented using Django Rest Framework. It provides endpoints to manage a user's todo items.

## Installation

1. Ensure you have Python (v3.6+) installed on your system.

2. Clone the repository:

   ```
   git clone https://github.com/Blank333/simple-api
   ```

3. Navigate to the project directory:

   ```
   cd simple-api
   ```

4. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Navigate to the core files

   ```
   cd core
   ```

6. Migrate the database:

   ```
   python manage.py migrate
   ```

7. Create a superuser (admin):

   ```
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

## Usage

Start the development server:

```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` to access the admin panel and log in with the superuser credentials.

To interact with the API, use the following endpoints:

- List all todos for the authenticated user:

  ```
  GET /api/v1/todos/
  ```

- Create a new todo for the authenticated user:

  ```
  POST /api/v1/todos/
  ```

  Payload:

  ```json
  {
    "task": "Task description",
    "completed": false
  }
  ```

- Retrieve, update, or delete a specific todo:

  ```
  GET /api/v1/todos/<int:todo_id>/
  PUT /api/v1/todos/<int:todo_id>/
  DELETE /api/v1/todos/<int:todo_id>/
  ```

  For updates, send a JSON payload similar to the one used for creating.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
