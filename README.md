# 🔐 Smart Password Generator (CLI)

A Python-based Command Line Interface (CLI) application that generates secure and unpredictable passwords using user input, character transformation, and random character insertion. The system converts user-provided words into stronger passwords using **Leetspeak transformation**, adds random characters, and shuffles the final output to increase security.

---

## 🚀 Features

* **Leetspeak Character Transformation**

  * Converts common characters into stronger symbols (e.g., `a → @`, `s → $`, `o → 0`).

* **Custom Password Length**

  * Users can define the desired password length.

* **Random Character Generation**

  * Adds random letters, numbers, and special characters to improve password strength.

* **Password Randomization**

  * Uses a shuffle algorithm to make the password unpredictable.

* **Command Line Interface**

  * Simple and lightweight CLI tool that runs directly in the terminal.

---

## 🛠 Technologies Used

* **Python**
* `random` module
* `string` module

---

## 📂 Project Structure

```
password-generator/
│
├── password_generator.py
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/your-username/password-generator.git
```

2. Navigate to the project folder

```
cd password-generator
```

3. Run the program

```
python password_generator.py
```

---

## ▶️ Usage Example

```
Enter base word: password
Enter desired password length: 12
```

Output:

```
Generated Password: 7@k1n%9X!jP
```

---

## 🧠 How It Works

1. The user enters a base word.
2. The program transforms characters using **Leetspeak substitution rules**.
3. If the transformed word is shorter than the desired password length, random characters are added.
4. The password is shuffled to increase unpredictability.
5. The final secure password is displayed.

---

## 🔑 Example Transformation

| Input Word | Transformed Word |
| ---------- | ---------------- |
| password   | p@$$w0rd         |
| secure     | $3cur3           |

---

## 📌 Future Improvements

* Password strength checker
* Multiple password generation
* Web-based version using **Django**
* Save encrypted passwords
* Password export to file

---

## 👨‍💻 Author

**Ajin**

Python Developer | Backend Developer
Skills: Python, Django, JavaScript, SQL, HTML, CSS

---

## 📄 License

This project is open-source and available under the MIT License.
