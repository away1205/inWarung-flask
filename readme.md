# Flask REST API Example

The project demonstrates an API that allows you to create, read, update, and delete records in a SQLite database.

## Project Structure

The project is organized into the following files:

- `app.py`: The main application file to run the Flask app.
- `config.py`: Configuration settings for the Flask app.
- `models.py`: Database models.
- `resources.py`: API resources.
- `database.db`: SQLite database file (auto-generated).

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/away1205/inWarung-flask.git
   cd flask-rest-api-example
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

   The application will be running at `http://127.0.0.1:5000/`.

## API Endpoints

### List Users

- **URL:** `/api/users/`
- **Method:** `GET`
- **Description:** Retrieves a list of all users.
- **Response:**

  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "email": "john@example.com"
      },
      ...
  ]
  ```

### Create a User

- **URL:** `/api/users/`
- **Method:** `POST`
- **Description:** Creates a new user.
- **Form Data:**
  - `name` (string, required)
  - `email` (string, required)
- **Response:**

  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "email": "john@example.com"
      },
      ...
  ]
  ```

### Get a User by ID

- **URL:** `/api/users/<int:id>`
- **Method:** `GET`
- **Description:** Retrieves a user by ID.
- **Response:**

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

### Update a User by ID

- **URL:** `/api/users/<int:id>`
- **Method:** `PATCH`
- **Description:** Updates a user by ID.
- **Form Data:**
  - `name` (string, required)
  - `email` (string, required)
- **Response:**

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

### Delete a User by ID

- **URL:** `/api/users/<int:id>`
- **Method:** `DELETE`
- **Description:** Deletes a user by ID.
- **Response:**

  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "email": "john@example.com"
      },
      ...
  ]
  ```

## Configuration

The configuration settings are located in the `config.py` file. By default, the application uses an SQLite database named `database.db`.

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
