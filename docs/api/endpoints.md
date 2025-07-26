# API Endpoints Documentation

This document outlines the API endpoints available in the HSA Multi-Agent System. Each endpoint is designed to facilitate interactions with the various agents responsible for managing Health Savings Accounts (HSAs) in accordance with IRS rules.

## Base URL
The base URL for accessing the API is:
```
http://localhost:5000/api
```

## Endpoints

### 1. Eligibility Check
- **Endpoint:** `/eligibility`
- **Method:** `POST`
- **Description:** Checks the eligibility of an individual for opening an HSA based on IRS rules.
- **Request Body:**
  ```json
  {
    "age": 30,
    "is_enrolled_in_high_deductible_plan": true,
    "other_conditions": {}
  }
  ```
- **Response:**
  - **200 OK:** Eligibility status
  ```json
  {
    "eligible": true,
    "message": "Eligible for HSA."
  }
  ```
  - **400 Bad Request:** Invalid input data

### 2. Contribution Management
- **Endpoint:** `/contribution`
- **Method:** `POST`
- **Description:** Manages contributions to the HSA and ensures compliance with IRS limits.
- **Request Body:**
  ```json
  {
    "amount": 3000,
    "year": 2023
  }
  ```
- **Response:**
  - **200 OK:** Contribution status
  ```json
  {
    "success": true,
    "message": "Contribution accepted."
  }
  ```
  - **400 Bad Request:** Contribution exceeds limit

### 3. Distribution Handling
- **Endpoint:** `/distribution`
- **Method:** `POST`
- **Description:** Handles distributions from the HSA and checks for qualified medical expenses.
- **Request Body:**
  ```json
  {
    "amount": 500,
    "expense_type": "qualified"
  }
  ```
- **Response:**
  - **200 OK:** Distribution status
  ```json
  {
    "success": true,
    "message": "Distribution processed."
  }
  ```
  - **400 Bad Request:** Invalid expense type

### 4. Compliance Check
- **Endpoint:** `/compliance`
- **Method:** `GET`
- **Description:** Checks the compliance of actions taken by the agents with IRS regulations.
- **Response:**
  - **200 OK:** Compliance status
  ```json
  {
    "compliant": true,
    "message": "All actions are compliant."
  }
  ```
  - **500 Internal Server Error:** Compliance check failed

## Conclusion
This API provides a structured way to interact with the HSA Multi-Agent System, ensuring that all operations adhere to IRS regulations while facilitating the management of Health Savings Accounts.