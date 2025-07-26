# HSA Multi-Agent System

## Overview
The HSA Multi-Agent System is designed to manage Health Savings Accounts (HSAs) in compliance with IRS rules. This system utilizes multiple agents to handle various aspects of HSA management, including eligibility determination, contribution management, distribution handling, and compliance verification.

## Project Structure
The project is organized into several directories:

- **src/**: Contains the source code for the application.
  - **agents/**: Implements different agents responsible for HSA management.
  - **graph/**: Manages the workflow and state models.
  - **utils/**: Provides utility functions and IRS rule definitions.
  - **main.py**: The entry point for the application.

- **docs/**: Contains documentation related to the system architecture, API endpoints, and user guides.
  - **architecture/**: Overview and diagrams of the system architecture.
  - **api/**: Documentation of API endpoints.
  - **user_guide.md**: Instructions for users on how to interact with the system.

- **tests/**: Contains unit tests for the agents, workflow, and utility functions to ensure the system operates correctly.

- **requirements.txt**: Lists the dependencies required for the project.

- **pyproject.toml**: Contains project metadata and configuration for packaging and dependencies.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hsa-multi-agent-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage
The system allows users to manage their HSAs by interacting with the various agents. Each agent is responsible for a specific function, ensuring that all actions comply with IRS regulations.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.