graph LR
    subgraph "Agent Communication"
        A1[Agent 1] --> MSG[Message Queue]
        MSG --> A2[Agent 2]
        A2 --> MSG
        MSG --> A3[Agent 3]
    end
    
    subgraph "State Sharing"
        A1 --> STATE[Shared State]
        A2 --> STATE
        A3 --> STATE
        STATE --> A1
        STATE --> A2
        STATE --> A3
    end
    
    subgraph "Event Flow"
        A1 --> EVT1[Event: Eligibility Complete]
        A2 --> EVT2[Event: Contribution Complete]
        A3 --> EVT3[Event: Distribution Complete]
    end