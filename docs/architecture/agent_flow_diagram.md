# Agent Flow Diagram for HSA Multi-Agent System

This document provides a visual representation of the flow of information between the different agents in the HSA Multi-Agent System. The agents interact with each other to ensure compliance with IRS rules and manage the HSA processes effectively.

## Diagram Description

- **EligibilityAgent**: Determines if an individual is eligible for an HSA based on IRS rules.
- **ContributionAgent**: Manages contributions to the HSA, ensuring they comply with IRS limits.
- **DistributionAgent**: Handles distributions from the HSA and verifies that expenses are qualified.
- **ComplianceAgent**: Ensures that all actions taken by the other agents comply with IRS regulations.

## Flow of Information

1. **Eligibility Check**: The process begins with the EligibilityAgent assessing the individual's eligibility.
2. **Contribution Management**: If eligible, the ContributionAgent manages the contributions to the HSA.
3. **Distribution Handling**: When distributions are requested, the DistributionAgent checks for qualified medical expenses.
4. **Compliance Verification**: Throughout the process, the ComplianceAgent monitors all actions to ensure adherence to IRS regulations.

## Diagram

![Agent Flow Diagram](path/to/agent_flow_diagram.png)

*Note: Replace `path/to/agent_flow_diagram.png` with the actual path to the diagram image file.*

# HSA Agent Flow Documentation

## Overview
This document illustrates the flow and interactions between different agents in the HSA Multi-Agent System, showing how agents communicate, process data, and coordinate to achieve HSA management goals.

## Main Agent Flow

```mermaid
graph TB
    subgraph "Input Layer"
        UR[User Request]
        UD[User Data]
    end
    
    subgraph "Workflow Orchestration"
        WF[HSA Workflow]
        STATE[HSA State]
    end
    
    subgraph "Agent Processing Layer"
        EA[Eligibility Agent]
        CA[Contribution Agent]
        DA[Distribution Agent]
        CPA[Compliance Agent]
    end
    
    subgraph "Utility Layer"
        IR[IRS Rules]
        VR[Validation Rules]
        MS[Message System]
    end
    
    subgraph "Output Layer"
        RESULT[Processing Result]
        AUDIT[Audit Log]
    end
    
    UR --> WF
    UD --> STATE
    WF --> STATE
    
    STATE --> EA
    EA --> STATE
    STATE --> CA
    STATE --> DA
    CA --> STATE
    DA --> STATE
    STATE --> CPA
    CPA --> STATE
    
    EA --> IR
    CA --> IR
    DA --> IR
    CPA --> IR
    
    EA --> VR
    CA --> VR
    DA --> VR
    CPA --> VR
    
    EA --> MS
    CA --> MS
    DA --> MS
    CPA --> MS
    
    STATE --> RESULT
    CPA --> AUDIT