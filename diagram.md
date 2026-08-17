flowchart TD
    User[User / Web Browser]

    subgraph Docker[Docker Compose]
        
        subgraph FlaskContainer[Flask Application Container]
            Flask[Flask Application]

            subgraph Functions[Inventory Functions]
                View[View Computer List]
                Add[Add Computer]
                Edit[Edit Computer]
                Delete[Delete Computer]
            end
        end

        subgraph MySQLContainer[MySQL Database Container]
            MySQL[(MySQL Database)]

            subgraph Data[Computer Inventory Data]
                ComputerTable[(computers)]
                ID[ID]
                AssetName[Asset Name]
                Serial[Serial Number]
                Brand[Brand]
                Model[Model]
                OS[Operating System]
                Location[Location]
                Status[Status]
            end
        end
    end

    User -->|HTTP| Flask

    Flask --> View
    Flask --> Add
    Flask --> Edit
    Flask --> Delete

    View -->|SELECT| MySQL
    Add -->|INSERT| MySQL
    Edit -->|UPDATE| MySQL
    Delete -->|DELETE| MySQL

    MySQL --> ComputerTable

    ComputerTable --> ID
    ComputerTable --> AssetName
    ComputerTable --> Serial
    ComputerTable --> Brand
    ComputerTable --> Model
    ComputerTable --> OS
    ComputerTable --> Location
    ComputerTable --> Status

    MySQL -->|Query Result| Flask
    Flask -->|HTML Response| User