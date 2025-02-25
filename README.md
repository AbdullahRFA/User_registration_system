# Django User Registration and Authentication System

## 📌 Project Overview
This is a **Django-based User Registration and Authentication System** that allows users to **sign up, log in, log out**, and access protected pages. The project uses Django's built-in authentication system and `messages` framework for user feedback.

## ✨ Features
- **User Signup** with username, email, and password validation.
- **Login and Logout** functionality.
- **Error Handling** for invalid credentials, duplicate usernames/emails, and password mismatches.
- **Authenticated Routes**: Certain pages are only accessible after login.
- **Bootstrap Integration** for better UI/UX.

## 🛠️ Technologies Used
- **Django** (Python Web Framework)
- **SQLite** (Default Django database for development)
- **Bootstrap** (For frontend styling)
- **HTML, CSS, JavaScript**

## 📂 Project Structure
```
project_root/
│── app_name/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── about.html
│   │   ├── services.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── forms.py
│── project_name/
│   ├── settings.py
│   ├── urls.py
│── manage.py
│── db.sqlite3
│── README.md
```

## 🚀 Setup and Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AbdullahRFA/User_registration_system_with_django.git
cd Registration_System
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```
Open **http://127.0.0.1:8000/** in your browser.

## 🔑 User Authentication Flow
1. **Signup** at `/signup` → Creates a new user.
2. **Login** at `/login` → Authenticates user and redirects to home.
3. **Logout** → Logs out and redirects to login page.
4. **Authenticated Pages**: `@login_required` decorator ensures some pages are accessible only after login.

## 📜 API Endpoints
| Endpoint      | Method | Description |
|--------------|--------|-------------|
| `/signup`    | POST   | Register a new user |
| `/login`     | POST   | Log in an existing user |
| `/logout`    | GET    | Logout the current user |
| `/`          | GET    | Home page (requires login) |
| `/about`     | GET    | About page |
| `/services`  | GET    | Services page |

## 🛠️ Future Enhancements
- Add **password reset functionality**.
- Implement **social authentication** (Google, Facebook login).
- Improve **UI design** with more styling.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## 📜 License
This project is licensed under the **MIT License**.

---


## 📬 Contact
- **Developer:** Abdullah Nazmus-Sakib
- **GitHub:** [AbdullahRFA](https://github.com/AbdullahRFA)
- **Portfolio:** [abdullah-nazmus-sakib-rfa.netlify.app](https://abdullah-nazmus-sakib-rfa.netlify.app/)
- **Email:** [shakibrybmn@gmail.com)](mailto:shakibrybmn@gmail.com)

### Developed with ❤️ using Django.
