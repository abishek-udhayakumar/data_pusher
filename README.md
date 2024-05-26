# Data Pusher Django Web Application

## Overview

The Data Pusher is a Django web application designed to receive data from an account and distribute it to multiple destinations using webhook URLs. This project demonstrates how to create a Django REST API with modules for managing accounts and destinations, handling JSON data, and sending it to specified endpoints.


### Detailed Project Structure

1. **data_pusher_project/**: Root directory of the project.
2. **data_pusher/**: Django project directory.
   - **__init__.py**: Initializes the Django project.
   - **settings.py**: Contains the settings and configurations for the Django project.
   - **urls.py**: Defines the URL routing for the project.
   - **wsgi.py**: Entry-point for WSGI-compatible web servers to serve your project.
3. **core/**: Django app directory.
   - **migrations/**: Directory for database migration files.
     - **__init__.py**: Initializes the migrations directory.
   - **__init__.py**: Initializes the core app.
   - **admin.py**: Configuration for the Django admin interface.
   - **apps.py**: Configuration for the core app.
   - **models.py**: Defines the database models for Account and Destination.
   - **serializers.py**: Defines serializers for the models.
   - **tests.py**: Contains the test cases for the app.
   - **urls.py**: Defines the URL routing for the core app.
   - **views.py**: Contains the views and viewsets for handling requests.

## Features

- **Account Management**: Create, retrieve, update, and delete accounts. Each account has a unique email, account ID, and app secret token.
- **Destination Management**: Create, retrieve, update, and delete destinations for each account. Destinations include URL, HTTP method, and headers.
- **Data Handling**: Receive JSON data via a POST request and forward it to the specified destinations based on the account's secret token.
- **RESTful APIs**: CRUD operations for accounts and destinations, endpoint to receive data and forward it to destinations.

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/data_pusher.git
    cd data_pusher
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Account Management

- **Create Account**: `POST /api/accounts/`
- **Retrieve Account**: `GET /api/accounts/{id}/`
- **Update Account**: `PUT /api/accounts/{id}/`
- **Delete Account**: `DELETE /api/accounts/{id}/`

### Destination Management

- **Create Destination**: `POST /api/destinations/`
- **Retrieve Destination**: `GET /api/destinations/{id}/`
- **Update Destination**: `PUT /api/destinations/{id}/`
- **Delete Destination**: `DELETE /api/destinations/{id}/`
- **Get Destinations for Account**: `GET /api/account/{account_id}/destinations/`

### Data Handling

- **Receive Data**: `POST /api/server/incoming_data/`

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is open source and available under the [MIT License](LICENSE).


## Features

- **Account Management**: Create, retrieve, update, and delete accounts. Each account has a unique email, account ID, and app secret token.
- **Destination Management**: Create, retrieve, update, and delete destinations for each account. Destinations include URL, HTTP method, and headers.
- **Data Handling**: Receive JSON data via a POST request and forward it to the specified destinations based on the account's secret token.
- **RESTful APIs**: CRUD operations for accounts and destinations, endpoint to receive data and forward it to destinations.

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/data_pusher.git
    cd data_pusher
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Account Endpoints

- **Create an Account**

    ```bash
    http POST http://127.0.0.1:8000/api/accounts/ email="user@example.com" account_name="Test Account" website="http://example.com"
    ```

- **Retrieve an Account**

    ```bash
    http GET http://127.0.0.1:8000/api/accounts/<account_id>/
    ```

- **Update an Account**

    ```bash
    http PUT http://127.0.0.1:8000/api/accounts/<account_id>/ email="new_email@example.com" account_name="Updated Account Name" website="http://updated-website.com"
    ```

- **Delete an Account**

    ```bash
    http DELETE http://127.0.0.1:8000/api/accounts/<account_id>/
    ```

### Destination Endpoints

- **Create a Destination**

    ```bash
    http POST http://127.0.0.1:8000/api/destinations/ account="c2dcd2b8-894b-4a3a-ae69-5b902c9292a8" url="http://webhook.site/your-webhook-url" http_method="POST" headers:='{"APP_ID": "1234APPID1234", "APP_SECRET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s", "ACTION": "user.update", "Content-Type": "application/json", "Accept": "*"}'
    ```

- **Retrieve a Destination**

    ```bash
    http GET http://127.0.0.1:8000/api/destinations/<destination_id>/
    ```

- **Update a Destination**

    ```bash
    http PUT http://127.0.0.1:8000/api/destinations/<destination_id>/ url="http://updated-webhook.site/new-webhook-url" http_method="POST" headers:='{"APP_ID": "updated-APPID", "APP_SECRET": "updated-APPSECRET", "ACTION": "user.updated", "Content-Type": "application/json", "Accept": "*"}'
    ```

- **Delete a Destination**

    ```bash
    http DELETE http://127.0.0.1:8000/api/destinations/<destination_id>/
    ```

### Data Handling Endpoint

- **Receive and Forward Data**

    ```bash
    http POST http://127.0.0.1:8000/api/server/incoming_data/ CL-X-TOKEN:c59d64534c9e41a5b4f3d3e56d9e2873 data:='{"user_id": 123, "action": "update", "details": "Some details about the update"}'
    ```
