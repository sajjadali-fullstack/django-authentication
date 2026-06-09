# 🎓 Sajjad Exams - Online Examination Portal

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2%2B-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-563D7C?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

Sajjad Exams ek fully functional, secure aur responsive **Online Examination Portal** hai jise Django aur Bootstrap 5 ka use karke banaya gaya hai. Is platform par students secure login/signup ke baad alag-alag exams (Python, Java, Aptitude) de sakte hain.

---

## 🚀 Features

- **Secure Authentication System:** Django built-in auth backend ke sath custom Login aur Registration flows.
- **Password Masking & Hashing:** Sign-up ke waqt secure password hashing (`PBKDF2`) aur forms me proper password masking (`••••••`).
- **Dynamic Session-Based Navbar:** Logged-in user ke authentication status (`user.is_authenticated`) ke mutabik dynamic links aur custom welcome message display.
- **Exam Area Protection:** `@login_required` decorators ka use karke core exam routes (Python, Java, Aptitude) ko secure kiya gaya hai taaki koi bina login kiye access na kar sake.
- **Professional Guidelines Interface:** Home aur Logout pages par instructions ko modern Bootstrap grid, components, aur alert badges ke sath design kiya gaya hai.
- **Clean Route Separation:** Auth system ke defaults aur custom application views ke beech routing conflicts ko successfully resolve kiya gaya hai.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, Bootstrap 5, Custom CSS
- **Database:** SQLite 

