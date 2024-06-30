# inWarung REST API with Azure PostgreSQL

This project is a Flask REST API connected to an Azure PostgreSQL database. It handles user data, product details, transactions, and restocking information.

## Project Structure

The project is organized into the following files:

- `app.py`: The main application file to run the Flask app.
- `models.py`: Database models.
- `resources.py`: API resources.

## Prerequisites

- Python 3.7+
- PostgreSQL
- Azure PostgreSQL Database (for production)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file in the root directory of the project and add your environment variables. For local development, you need to add your database URI and other necessary configurations.

5. Run database migrations:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Configuration

The application supports different configurations for development and production environments. The configuration is determined by the presence of the `WEBSITE_HOSTNAME` environment variable, which is set in Azure.

- For local development, create a `config/development.py` file with the following content:

  ```python
  import os

  BASE_DIR = os.path.abspath(os.path.dirname(__file__))
  DATABASE_URI = 'postgresql://<username>:<password>@<hostname>:<port>/<database>'
  DEBUG = True
  ```

- For production, create a `config/production.py` file with the following content:

  ```python
  import os

  BASE_DIR = os.path.abspath(os.path.dirname(__file__))
  DATABASE_URI = os.getenv('DATABASE_URL')
  DEBUG = False
  ```

## Running the Application

1. Start the Flask application:

   ```bash
   flask run
   ```

2. The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### User Endpoints

- `GET /api/users/` - Get all users
- `POST /api/users/` - Create a new user
- `GET /api/users/<int:id>` - Get a user by ID
- `PATCH /api/users/<int:id>` - Update a user by ID
- `DELETE /api/users/<int:id>` - Delete a user by ID

### Product Endpoints

- `GET /api/products/` - Get all products
- `POST /api/products/` - Create a new product
- `GET /api/products/<int:id>` - Get a product by ID
- `PATCH /api/products/<int:id>` - Update a product by ID
- `DELETE /api/products/<int:id>` - Delete a product by ID

### Category Endpoints

- `GET /api/categories/` - Get all categories
- `POST /api/categories/` - Create a new category
- `GET /api/categories/<int:id>` - Get a category by ID
- `PATCH /api/categories/<int:id>` - Update a category by ID
- `DELETE /api/categories/<int:id>` - Delete a category by ID

### Detail Transaction Endpoints

- `GET /api/detail-transactions/` - Get all detail transactions
- `POST /api/detail-transactions/` - Create a new detail transaction
- `GET /api/detail-transactions/<int:id>` - Get a detail transaction by ID
- `PATCH /api/detail-transactions/<int:id>` - Update a detail transaction by ID
- `DELETE /api/detail-transactions/<int:id>` - Delete a detail transaction by ID

### Transaction Endpoints

- `GET /api/transactions/` - Get all transactions
- `POST /api/transactions/` - Create a new transaction
- `GET /api/transactions/<int:id>` - Get a transaction by ID
- `PATCH /api/transactions/<int:id>` - Update a transaction by ID
- `DELETE /api/transactions/<int:id>` - Delete a transaction by ID

### Restock Endpoints

- `GET /api/restocks/` - Get all restocks
- `POST /api/restocks/` - Create a new restock
- `GET /api/restocks/<int:id>` - Get a restock by ID
- `PATCH /api/restocks/<int:id>` - Update a restock by ID
- `DELETE /api/restocks/<int:id>` - Delete a restock by ID

## Testing the Connection to Azure PostgreSQL using `psycopg2`

To test the connection to your Azure PostgreSQL database, use the following script:

```python
import psycopg2

DB_HOST = '<hostname>'
DB_NAME = '<database_name>'
DB_USER = '<username>'
DB_PASS = '<password>'

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        print("Connection to database established successfully")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def run_queries():
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            )
        """)
        print("Table created successfully")

        cur.execute("""
            INSERT INTO test_table (name, age)
            VALUES ('John Doe', 30),
                   ('Jane Smith', 25)
            RETURNING id, name, age
        """)
        inserted_rows = cur.fetchall()
        print("Data inserted successfully:")
        for row in inserted_rows:
            print(row)

        cur.execute("SELECT * FROM test_table")
        rows = cur.fetchall()
        print("Data selected successfully:")
        for row in rows:
            print(row)

        cur.execute("""
            UPDATE test_table
            SET age = age + 1
            WHERE name = 'John Doe'
            RETURNING id, name, age
        """)
        updated_row = cur.fetchone()
        print("Data updated successfully:", updated_row)

        cur.execute("""
            DELETE FROM test_table
            WHERE name = 'Jane Smith'
            RETURNING id, name, age
        """)
        deleted_row = cur.fetchone()
        print("Data deleted successfully:", deleted_row)

        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error executing queries: {e}")
    finally:
        conn.close()
        print("Connection closed")

if __name__ == '__main__':
    run_queries()
```

Replace the placeholders (`<hostname>`, `<database_name>`, `<username>`, `<password>`) with your actual Azure PostgreSQL credentials and run the script to test the connection and perform basic CRUD operations.

## Kudos

Kudos to everyone who read up to this line😊.

---
