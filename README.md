#  Password Strength Checker

A professional Python terminal utility designed to evaluate password security by analyzing complexity, length, and common/leaked credentials, providing real-time privacy-masked feedback.

---

## Features

* **Interactive CLI Loop:** Runs continuously to let users test multiple passwords in one session until they choose to quit by typing `q`.
* **Privacy-First Masking:** Automatically conceals the analyzed password in the output report using asterisks (`************`) to prevent shoulder-surfing.
* **Leak & Commonality Check:** Instantly verifies if the password is a known common or leaked credential (`Common/Leaked` detection).
* **Granular Criteria Checklist:** Explicitly tracks and displays whether the password satisfies:
  * Length requirements
  * Uppercase letters
  * Lowercase letters
  * Numerical digits
  * Special symbols
* **6-Point Scoring Metric:** Provides a precise mathematical score (`X / 6`) alongside a final strength rating (e.g., *Strong*).

---

##  How to Run

1. Download or clone `password_strength_checker.py`.
2. Open your terminal or command prompt in the project folder.
3. Run the script using Python:
   ```bash
   python password_strength_checker.py
