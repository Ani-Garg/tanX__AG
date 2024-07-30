
### Explanation of Files and Directories

- **`app.py`**: This is the main application script that reads the orders from `orders.csv`, computes various metrics (monthly revenue, product revenue, customer revenue, and top 10 customers by revenue), and prints the results.

- **`orders.csv`**: This file contains the sample data for customer orders. It includes columns for order ID, customer ID, order date, product ID, product name, product price, and quantity.

- **`requirements.txt`**: This file lists the Python dependencies required by the project. For this project, we need `pandas`.

- **`Dockerfile`**: This file contains the instructions to build a Docker image for the main application.

- **`Dockerfile.test`**: This file contains the instructions to build a Docker image for running the tests.

- **`docker-compose.yml`**: This file defines the services for the application and tests, allowing you to build and run them using Docker Compose.

- **`README.md`**: This file contains information about the project, including its structure and how to run it.

- **`tests/`**: This directory contains the test files.

  - **`test_orders.py`**: This file contains unit tests for the functions defined in `app.py`.

## Running the Application

To build and run the application, use the following command:

```bash
docker-compose up --build app
