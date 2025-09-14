# AirBnB Clone - The Console

**AirBnB Clone - The Console** is a Python command-line application that allows users to manage objects of a simplified AirBnB system. This project is part of ALU’s curriculum and sets the foundation for later projects involving database storage, web interface, API integration, and more.

---

## Features

- Create, update, and delete objects of multiple classes: `User`, `State`, `City`, `Amenity`, `Place`, `Review`, and `BaseModel`.
- Retrieve all objects or a specific object by class name and ID.
- Count the number of instances of a class.
- Supports advanced command syntax:

  - `<class name>.all()`
  - `<class name>.count()`
  - `<class name>.show(<id>)`
  - `<class name>.destroy(<id>)`
  - `<class name>.update(<id>, <attribute name>, <attribute value>)`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Jonathan2055/alu-AirBnB_clone.git
cd alu-AirBnB_clone
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

---

## Usage

1. Start the console:

```bash
python3 console.py
```

2. Example commands:

```text
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) all
(hbnb) User.count()
(hbnb) User.update 1234-5678-9012 email "user@example.com"
(hbnb) destroy User 1234-5678-9012
(hbnb) quit
```

3. Command syntax supports:

```text
<Class name>.all()
<Class name>.count()
<Class name>.show(<id>)
<Class name>.destroy(<id>)
<Class name>.update(<id>, <attribute name>, <attribute value>)
```

---

## Classes

- **BaseModel** – Base class for all models.
- **User** – Represents a user of the system.
- **State** – Represents a state or region.
- **City** – Represents a city.
- **Amenity** – Represents a service or facility.
- **Place** – Represents a place to stay.
- **Review** – Represents a review left by a user.

---

## File Structure

```
AirBnB_clone/
│
├── console.py        # Main console program
├── models/           # Contains all models
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   └── review.py
├── tests/            # Unit tests for all models
├── web_static/       # Placeholder for web files (future projects)
├── AUTHORS           # Project contributors
└── README.md         # Project documentation
```

---

## Contributors 👥

- **MUGISHA Jonathan** – [j.mugisha3@alustudent.com]

---
