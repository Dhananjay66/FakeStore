# 🛍️ Fake Store (Django + Bootstrap)

A Django web app that displays products from the [FakeStoreAPI](https://fakestoreapi.com/). It features a responsive Bootstrap interface with filtering, search, and dynamic product listings.

---

## 🔧 Features

- 💡 Fetches real-time data from [FakeStoreAPI](https://fakestoreapi.com/)
- 🔍 Search and category filter
- ⚙️ Django-powered backend
- 🎨 Styled with Bootstrap 5
- 📱 Mobile-friendly layout

---

## 🌐 Live Demo

> 🔗 https://fakestore-p80j.onrender.com

---

## 📁 Project Structure

```

fakestore/
│
├── fakestore/             # Django project settings
│   └── **pycache**/
│
├── store/                 # Main Django app
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   └── **pycache**/
│
├── manage.py
├── requirements.txt
└── README.md

````

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Dhananjay66/FakeStore.git
cd FakeStore
````

### 2. Create & activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 📦 requirements.txt

```txt
Django>=4.0,<5.0
requests
```

You can generate or update this file anytime with:

```bash
pip freeze > requirements.txt
```

---

## 🌐 API Source

Powered by:

> 📦 [FakeStoreAPI](https://fakestoreapi.com/)

---

## 📄 License

MIT License. Open for learning, contribution, or customization.

---

## ✨ Author

**Dhananjay**
🔗 [github.com/Dhananjay66](https://github.com/Dhananjay66)
