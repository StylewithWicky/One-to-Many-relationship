# 📚 SQLAlchemy One-to-Many Relationship: Author & Posts

This project demonstrates how to create a **one-to-many relationship** using **SQLAlchemy ORM** in Python. An `Author` can have multiple `Post` entries, but each `Post` belongs to only one `Author`.

---

## 🛠 Technologies Used

- Python 3.12+
- SQLAlchemy ORM
- SQLite (in-memory)

---

## 🔗 Relationship Overview

- **One Author ➝ Many Posts**
- This is implemented using SQLAlchemy’s `relationship()` and `ForeignKey()` constructs with `back_populates`.

---

## 🧱 Models

### `Author`
| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key |
| `name` | String | Author's name |
| `posts` | Relationship | List of `Post` objects |

### `Post`
| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key |
| `name` | String | Title of the post |
| `author_id` | Integer | Foreign key linking to `Author.id` |
| `author` | Relationship | The associated `Author` object |

---

## 🚀 How to Run

1. Clone or download the project.
2. Create a virtual environment and install dependencies (if needed).
3. Run the `db.py` file:

```bash
python db.py
