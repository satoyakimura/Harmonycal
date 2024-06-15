# Harmonycal
## データベース設計

```mermaid
erDiagram
    userdata {
        id SERIAL PK
        username VARCHAR(100)
        email VARCHAR(255)
        created_at TIMESTAMP
    }

    schedule {
        id SERIAL PK
        user_id INT FK
        title VARCHAR(255)
        description TEXT
        start_date TIMESTAMP
        end_date TIMESTAMP
    }
    userdata || -- || schedule
```
