# System Overview of the HSA Multi-Agent System

## Introduction
The HSA Multi-Agent System is designed to facilitate the management of Health Savings Accounts (HSAs) in compliance with IRS regulations. The system is composed of multiple agents, each responsible for specific tasks related to eligibility, contributions, distributions, and compliance.

## Components

### Agents
1. **EligibilityAgent**
   - Determines the eligibility of individuals for HSAs based on IRS rules.
   - Interacts with the IRS rules module to validate eligibility criteria.

2. **ContributionAgent**
   - Manages contributions to the HSA.
   - Ensures that contributions comply with IRS limits and regulations.

3. **DistributionAgent**
   - Handles distributions from the HSA.
   - Checks that distributions are made for qualified medical expenses.

4. **ComplianceAgent**
   - Ensures that all actions taken by the other agents comply with IRS regulations.
   - Monitors the overall compliance of the system.

### Workflow
- The **HSAWorkflow** class orchestrates the interactions between the agents.
- It manages the overall workflow, ensuring that each agent performs its tasks in the correct sequence and adheres to the defined rules.

### State Models
- The system utilizes state models to define various states of the HSA process.
- These models help in tracking the progress and status of HSA management tasks.

## Interactions
- The agents communicate with each other through the workflow orchestrated by the HSAWorkflow class.
- Data flows between agents as they perform their respective tasks, ensuring that the system operates cohesively.

## Conclusion
The HSA Multi-Agent System is a modular and compliant solution for managing Health Savings Accounts. By leveraging specialized agents and a structured workflow, the system ensures adherence to IRS regulations while providing a streamlined user experience.

# HSA Multi-Agent System Architecture

## System Overview

The HSA Multi-Agent System uses LangGraph to orchestrate multiple specialized agents that handle different aspects of HSA management according to IRS rules.

## High-Level Architecture

```mermaid
graph TB
    subgraph "User Interface"
        UI[User Request]
    end
    
    subgraph "LangGraph Workflow"
        WF[HSA Workflow Orchestrator]
    end
    
    subgraph "Agent Layer"
        EA[Eligibility Agent]
        CA[Contribution Agent]
        DA[Distribution Agent]
        CPA[Compliance Agent]
    end
    
    subgraph "Utilities"
        IR[IRS Rules Engine]
        VS[Validation Service]
    end
    
    subgraph "State Management"
        HS[HSA State]
        MS[Message Store]
    end
    
    UI --> WF
    WF --> EA
    WF --> CA
    WF --> DA
    WF --> CPA
    
    EA --> IR
    CA --> IR
    DA --> IR
    CPA --> IR
    
    EA --> VS
    CA --> VS
    DA --> VS
    CPA --> VS
    
    EA --> HS
    CA --> HS
    DA --> HS
    CPA --> HS
    
    EA --> MS
    CA --> MS
    DA --> MS
    CPA --> MS