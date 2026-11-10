# Backend – Laundry Automation System

The **Backend** is the central service responsible for managing and coordinating the operations of the Laundry Automation System.

Built using **Python and FastAPI**, it acts as the communication layer between the embedded devices (Authenticator and Scanner), the frontend dashboard, and the database.

It handles RFID tag management, laundry bag tracking, batch organization, processing workflows,  audit logging, and notifications. It serves as the single source of truth for the system, ensuring that all connected devices and interfaces operate using consistent and up-to-date information.

## Features (Planned)

- **RFID Tag Management:** Registers, tracks, and manages RFID tags associated with laundry bags.
- **Tag Assignment:** Handles tag-to-user association initiated through the Entrypoint.
- **Bag Management:** Maintains individual laundry tags and their processing status.
- **Batch Management:**: tracks batch progress.
- **Automated Batch Completion:** Determines batch completion based on the status of its associated tags..
- **Scanner Integration:** Processes scanning events and updates bag status.
- **Audit Logging:** Records important system activities and state transitions.
- **Notifications:** Generates individual notifications for relevant operational events.
- **Dashboard Integration:** Provides APIs for retrieving operational data and monitoring system activity.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| FastAPI | REST API framework |
| SQLite | Relational database |
| SQLAlchemy | ORM and database interaction |
| Alembic | Database schema migrations |
| Pydantic | Request validation and response schemas |
| Uvicorn | ASGI application server |

## Project Structure

Note: Some project folders have not been implemented yet; Not completely fixed, can be subject to changes in the future
```
laundry_backend/
│
├── pyproject.toml
├── alembic.ini
├── README.md
│
├── migrations/
│   ├── env.py
│   └── versions/
│
├── src/
│   └── app/
│       │
│       ├── main.py
│       │
│       ├── core/
│       │   ├── config.py
│       │   ├── logging.py
│       │   ├── exceptions.py
│       │   └── lifespan.py
│       │
│       ├── auth/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── schemas.py
│       │   ├── service.py
│       │   ├── repository.py
│       │   ├── dependencies.py
│       │   ├── password.py
│       │   ├── tokens.py
│       │   └── router.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── dependencies.py
│       │   ├── exception_handlers.py
│       │   ├── schemas/
│       │   │   ├── pagination.py
│       │   │   └── responses.py
│       │   │
│       │   └── v1/
│       │       ├── __init__.py
│       │       ├── router.py
│       │       │
│       │       └── modules/
│       │           ├── customers/
│       │           │   ├── router.py
│       │           │   ├── endpoints.py
│       │           │   └── schemas.py
│       │           │
│       │           ├── catalog/
│       │           │   ├── router.py
│       │           │   ├── endpoints.py
│       │           │   └── schemas.py
│       │           │
│       │           ├── orders/
│       │           │   ├── router.py
│       │           │   ├── endpoints.py
│       │           │   └── schemas.py
│       │           │
│       │           ├── processing/
│       │           │   ├── router.py
│       │           │   ├── endpoints.py
│       │           │   └── schemas.py
│       │           │
│       │           ├── billing/
│       │           │   ├── router.py
│       │           │   ├── endpoints.py
│       │           │   └── schemas.py
│       │           │
│       │           └── delivery/
│       │               ├── router.py
│       │               ├── endpoints.py
│       │               └── schemas.py
│       │
│       ├── devices/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── authentication.py
│       │   ├── dependencies.py
│       │   ├── schemas.py
│       │   ├── protocol.py
│       │   ├── endpoints/
│       │   │   ├── events.py
│       │   │   ├── commands.py
│       │   │   └── status.py
│       │   └── services.py
│       │
│       ├── features/
│       │   ├── customers/
│       │   ├── catalog/
│       │   ├── orders/
│       │   ├── processing/
│       │   ├── billing/
│       │   └── delivery/
│       │
│       ├── infrastructure/
│       │   ├── database/
│       │   │   ├── base.py
│       │   │   ├── session.py
│       │   │   └── model_registry.py
│       │   │
│       │   ├── messaging/
│       │   ├── notifications/
│       │   └── external_services/
│       │
│       └── shared/
│           ├── types.py
│           ├── enums.py
│           └── utilities.py
│
└── tests/
    ├── unit/
    ├── integration/
    └── api/
```
## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pragadheesh08/SLMS.git
cd SLMS/backend
```

### 2. TODO

## Core System Workflows

TODO

## Testing
TODO
## Development Guidelines

To maintain code quality and consistency:

- Keep API routes thin; business logic belongs in service modules.
- Keep database operations and transactions consistent.
- Avoid hardcoding credentials or configuration values.
- Document changes to API contracts.

### Git Workflow

All backend development should take place in feature branches.

Example:

```bash
git checkout -b feature/batch-management
```

After implementation and testing, create a Pull Request targeting the development branch.

Avoid directly pushing unfinished code to the main branch.

## Future Improvements

Potential enhancements include:
    - TODO
