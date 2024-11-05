# FastAPI User Management Project

## Overview

This is a FastAPI project designed for user management with basic authentication functionalities. It includes features such as user creation and deletion, login, logout, etc. The project is containerized using Docker and Docker Compose for streamlined setup and deployment.

## Features

- User Management: Comprehensive management of user accounts, including registration, authentication, and account deletion.
- Authentication: Secure user login and session management to protect user data and maintain integrity.

This project is structured around Domain-Driven Design (DDD) principles, focusing on encapsulating business logic within domain models and ensuring that the user management functionality is both robust and maintainable.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/your_username/your_repository.git>
   cd your_repository
   ```

2. **Set up the environment and start the services:**

- Firstly, start main app with:

    ```bash
    make app-dev
    ```

- Then you can start storages with:

    ```bash
    make storages
    ```

- Make migrations with:

    ```bash
    make migrate
    ```

- Also you can run tests with:

    ```bash
    make test
    ```

## Notes

- Ensure your `.env` file is configured correctly for Docker Compose.
