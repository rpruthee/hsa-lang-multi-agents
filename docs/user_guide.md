# User Guide for HSA Multi-Agent System

## Introduction
The HSA Multi-Agent System is designed to facilitate the management of Health Savings Accounts (HSAs) in compliance with IRS regulations. This user guide provides an overview of how to interact with the system, including its components and functionalities.

## System Components
The system consists of several agents, each responsible for specific tasks related to HSA management:

1. **EligibilityAgent**: Determines eligibility for HSA based on IRS rules.
2. **ContributionAgent**: Manages contributions to the HSA and ensures compliance with IRS limits.
3. **DistributionAgent**: Handles distributions from the HSA and checks for qualified medical expenses.
4. **ComplianceAgent**: Ensures that all actions taken by the other agents comply with IRS regulations.

## Getting Started
To get started with the HSA Multi-Agent System, follow these steps:

1. **Installation**: Ensure that all dependencies listed in `requirements.txt` are installed. You can use a package manager like pip to install them.

2. **Configuration**: Configure any necessary settings in the `pyproject.toml` file as per your requirements.

3. **Running the System**: Execute the `main.py` file to start the application. This will initialize the agents and begin the workflow.

## Interacting with the System
The system can be interacted with through its API endpoints. Refer to the API documentation in `docs/api/endpoints.md` for detailed information on available endpoints and their usage.

## Workflow Overview
The HSAWorkflow orchestrates the interactions between the different agents. It manages the overall workflow, ensuring that each agent performs its tasks in the correct order and that data flows seamlessly between them.

## Troubleshooting
If you encounter any issues while using the system, check the following:

- Ensure that all dependencies are correctly installed.
- Review the logs for any error messages that may indicate what went wrong.
- Consult the unit tests in the `tests` directory to verify that individual components are functioning as expected.

## Conclusion
This user guide provides a basic overview of the HSA Multi-Agent System. For more detailed information, please refer to the specific documentation files in the `docs` directory. If you have further questions or need assistance, feel free to reach out to the development team.