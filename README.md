# Computer Inventory Management System

ระบบจัดการข้อมูลคอมพิวเตอร์ (Computer Inventory Management System) พัฒนาด้วย **Python Flask** และ **MySQL** โดยใช้ **Docker และ Docker Compose** สำหรับจัดการและรัน Application กับ Database ภายใน Container

## System Architecture

```mermaid
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
            ComputerTable[(computers table)]
        end
    end

    User -->|HTTP Request| Flask

    Flask --> View
    Flask --> Add
    Flask --> Edit
    Flask --> Delete

    View -->|SELECT| MySQL
    Add -->|INSERT| MySQL
    Edit -->|UPDATE| MySQL
    Delete -->|DELETE| MySQL

    MySQL --> ComputerTable

    MySQL -->|Query Result| Flask
    Flask -->|HTML Response| User
```



## Features

ระบบสามารถจัดการข้อมูลคอมพิวเตอร์ได้ดังนี้

- แสดงรายการคอมพิวเตอร์ทั้งหมด
- เพิ่มข้อมูลคอมพิวเตอร์
- แก้ไขข้อมูลคอมพิวเตอร์
- ลบข้อมูลคอมพิวเตอร์
- จัดเก็บข้อมูลใน MySQL Database
- จำกัดการลบข้อมูลเฉพาะการเข้าถึงจาก Localhost
- รัน Web Application และ Database ด้วย Docker Compose

---

## Technologies Used

โปรเจกต์นี้ใช้เทคโนโลยีดังต่อไปนี้

| Technology | Description |
|---|---|
| Python | ภาษาหลักสำหรับพัฒนา Backend |
| Flask | Framework สำหรับพัฒนา Web Application |
| MySQL | ระบบจัดการฐานข้อมูล |
| mysql-connector-python | Library สำหรับเชื่อมต่อ Python กับ MySQL |
| HTML | ใช้สร้างหน้าเว็บไซต์ |
| Docker | ใช้สร้างและรัน Application ภายใน Container |
| Docker Compose | ใช้จัดการ Web Application และ Database หลาย Container |

---

# Project Structure

```text
computer-inventory/
│
├── .gitignore
├── app.py
├── diagram.md
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
│
├── db/
│   └── init.sql
│
└── templates/
    ├── add.html
    ├── edit.html
    └── index.html
