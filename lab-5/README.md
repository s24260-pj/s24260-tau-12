# User API Integration Tests

This project contains integration tests for a User API that performs basic CRUD operations. The tests ensure that the API behaves correctly when creating, retrieving, updating, and deleting users.

## Tests Overview

### 1. **shouldCreateUser**
- Verifies that a user can be created with valid input. It checks that the response contains the correct `name` and `email`, and the status is `201 Created`.

### 2. **shouldReturnBadRequest**
- Verifies that the API returns a `400 Bad Request` status when required fields are missing (e.g., `email`).

### 3. **shouldUpdateUser**
- Verifies that a user's details can be updated successfully with valid data. It checks that the `name` and `email` fields are updated correctly.

### 4. **shouldThrowNotFoundException**
- Verifies that a `404 Not Found` error is returned when attempting to update a non-existent user.

### 5. **shouldDeleteUser**
- Verifies that a user can be deleted successfully. It checks that the status after deletion is `204 No Content`, and after deletion, any attempts to retrieve the user will return a `404 Not Found`.

### 6. **shouldReturnUserById**
- Verifies that a user can be retrieved by their ID. It checks that the `GET` request returns the correct `name` and `email` for the user.

### 7. **shouldReturnNotFoundException**
- Verifies that a `404 Not Found` error is returned when attempting to retrieve a user that does not exist.

### 8. **shouldReturnUserList**
- Verifies that the API returns a list of all users. It checks that the response is an array and contains the correct user details.

## How to Run the Tests

1. Clone this repository.
2. Make sure you have **Maven** installed.
3. Run the tests with your preferred build tool:
    - **Maven:** `mvn clean install`

## Technologies Used

- **JUnit 5** for writing integration tests.
- **Spring MockMvc** to simulate HTTP requests.
- **Spring Boot** for creating the RESTful API.
- **Jackson** for JSON processing.


## Screenshot
![image](https://github.com/user-attachments/assets/66404417-130c-4646-b11d-c4a6346df4c1)
