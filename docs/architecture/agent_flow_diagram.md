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

## 3. Add Agent Flow Documentation

```markdown
# HSA Agent Flow Documentation

## Agent Interaction Flow

```mermaid
graph TB
    subgraph "Request Processing Flow"
        START([User Request]) --> ENTRY[Entry Point]
        ENTRY --> EA[Eligibility Agent]
        
        EA --> ROUTE{Route Decision}
        ROUTE -->|Contribution| CA[Contribution Agent]
        ROUTE -->|Distribution| DA[Distribution Agent]
        ROUTE -->|Ineligible| END1([End - Ineligible])
        
        CA --> CPA[Compliance Agent]
        DA --> CPA
        CPA --> END2([End - Complete])
    end
    
    subgraph "State Updates"
        EA --> STATE1[Update Eligibility State]
        CA --> STATE2[Update Contribution State]
        DA --> STATE3[Update Distribution State]
        CPA --> STATE4[Update Compliance State]
    end
    
    subgraph "Message Flow"
        EA --> MSG1[Eligibility Message]
        CA --> MSG2[Contribution Message]
        DA --> MSG3[Distribution Message]
        CPA --> MSG4[Compliance Message]
    end
```