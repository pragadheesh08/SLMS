# Frontend – Laundry Automation System

The **Frontend** is the user interface of the Laundry Automation System, designed to provide laundry attendants with a centralized, real-time view of laundry operations.

It has two main components
1. Dashboard
2. User Login Portal

## Features
TODO

## Dashboard Components
TODO


## Project Structure
TODO: Decide project structure

## Technology Stack
TODO: Decide the stack

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pragadheesh08/SLMS.git
cd SLMS/frontend
```


### TODO: Complete rest of setup

## Backend Integration

The frontend communicates with the FastAPI backend to retrieve and display operational information.

Expected backend interactions include:

- Retrieving active laundry batches.
- Fetching individual bag information.
- Retrieving processing history and audit events.
- Retrieving delayed bags.
- Receiving updates when tags are assigned or processing stages change.

The frontend should not independently determine or modify the authoritative processing state. Business logic and data validation must remain in the backend.

Refer to the backend API documentation for endpoint definitions, request formats, and response schemas.


## Development Guidelines

To maintain consistency across the development team:

- Keep reusable UI elements inside `components/`.
- Separate API communication from UI components.
- Use centralized API configuration.
- Maintain consistent naming conventions.
- Avoid duplicating business logic already implemented in the backend.
- Document new API integrations.
- Test components before merging changes.
- Keep environment-specific configuration outside the source code.

### Git Workflow

All frontend development should take place in feature branches.

Example:

```bash
git checkout -b feature/dashboard-ui
```

After implementation and testing, create a Pull Request targeting the development branch.

Avoid pushing unfinished changes directly to the main branch.

## Future Improvements

Potential enhancements include:

- TODO: Add Enhancements