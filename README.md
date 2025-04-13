# 🚀 API Automation Framework (BDD with Behave + Allure)

### 📁 Folder Structure
- `features/` – Feature files & step definitions
- `utilities/` – Helper scripts (e.g. API wrappers)
- `reports/` – Auto-generated Allure reports
- `runner.py` – Main runner script
- `setup.sh / setup.bat` – One-click setup for dependencies

---

### 🛠️ Setup Instructions

1. Clone the repo
2. Run setup:
   - On Linux/macOS: `./setup.sh`
   - On Windows: `setup.bat`
3. Run your tests:
   ```bash
   python runner.py


📊 Allure Report Output
Allure HTML reports will be saved in:
   
   reports\<CurrentDate>\<Time>\index.html

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`. Main tools used:
- `behave`
- `requests`
- `allure-behave`
- `mysql-connector-python`

---

## 🧰 Useful Commands

| Task                    | Command                         |
|-------------------------|----------------------------------|
| Run tests               | `python runner.py`              |
| Run Specific feature file | `python runner.py -f features/feature-file-name` |
| Run Specific tags       | `python runner.py -t "tag_name"` |
| Run test by name        | `python runner.py -n "testcase_name"` |
| Generate the step_impl methods | `behave --dry-run -f plain` |
| Reinstall dependencies  | `pip install -r requirements.txt` |
| Activate venv manually  | `venv\Scripts\activate`         |

---

## 🙋‍♂️ Author

**Ramanan Ramasamy**  
📍 Bengaluru, India  
🔧 QA Automation Engineer | Python | BDD | CI/CD 
