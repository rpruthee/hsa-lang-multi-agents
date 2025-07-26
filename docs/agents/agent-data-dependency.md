```mermaid

graph TB
    subgraph "Data Dependencies"
        UD[User Data] --> EA[Eligibility Agent]
        EA --> ER[Eligibility Results]
        ER --> CA[Contribution Agent]
        ER --> DA[Distribution Agent]
        CA --> CR[Contribution Results]
        DA --> DR[Distribution Results]
        CR --> CPA[Compliance Agent]
        DR --> CPA
        ER --> CPA
    end
    
    subgraph "Shared Resources"
        IR[IRS Rules] --> EA
        IR --> CA
        IR --> DA
        IR --> CPA
        VR[Validation Rules] --> EA
        VR --> CA
        VR --> DA
        VR --> CPA
    end
    
    subgraph "External Data"
        TD[Tax Data] --> DA
        TD --> CPA
        LD[Limit Data] --> CA
        LD --> CPA
    end