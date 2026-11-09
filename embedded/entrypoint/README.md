# Entrypoint – Laundry Automation System

The **Entrypoint** is an ESP32-based embedded device responsible for RFID-based identification and tag assignment in the Laundry Automation System.

It acts as an interface between physical laundry operations and the central backend, allowing laundry attendants to associate RFID tags with laundry bags and initiate tracking workflows.

The device communicates with the backend over Wi-Fi, enabling centralized tag management, event logging, and real-time updates to the laundry management dashboard.

## Features
TODO: Decide required features
## Project Structure
TODO: Decide project structure

## Getting Started

### 1. Clone the Repository

Clone the main project repository:

```bash
git clone https://github.com/pragadheesh08/SLMS.git
cd SLMS/embedded/entrypoint/
```



## Backend Communication

The authenticator communicates with the central FastAPI backend through HTTP-based API requests.

The backend determines whether a tag operation is valid and updates the corresponding records.

Refer to the backend API documentation for the latest endpoint definitions and request/response formats.

## Development Guidelines

To maintain consistency across the team:

- Keep hardware-specific logic separate from network communication logic.
- Avoid hardcoding credentials and server addresses.
- Use meaningful function and variable names.
- Handle network failures without blocking RFID operations indefinitely.
- Document changes to hardware connections and API communication.
- Test firmware changes before merging them into the main branch.

### Git Workflow

All authenticator development should take place in feature branches.

Example:

```bash
git checkout -b feature/rfid-integration
```

After implementing and testing a feature, create a Pull Request to merge it into the development branch.

Avoid directly pushing unfinished code to the main branch.

## Future Improvements
TODO