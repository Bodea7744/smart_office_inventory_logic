# 🧠 Smart Office – Staff & Access Management System

This module offers a professional-grade simulation of staff members, internal users, and equipment tracking within a fictional smart office environment. Leveraging object-oriented principles such as inheritance, encapsulation, and polymorphism, the system orchestrates email validation, login processes, purchase history, and employee work analysis — all integrated into a clean digital infrastructure.

## 📌 Key Features
- Abstract base class `Entity` for consistent staff/user behavior
- Equipment tracking through `Equipment` class:
  - Private pricing
  - Stock validation
- User types:
  - `WorkspaceUser`: base user profile
  - `StandardWorkspaceUser`: discount logic based on spending
- Staff roles:
  - `Staff`: full-time employee with salary and work tracking
  - `ContractStaff`: includes contract expiry date
  - `FreelanceStaff`: tracks active projects
- Support for:
  - Email validation and login
  - Salary increases and attendance logging
  - Dynamic assignment and tracking of purchased equipment

## 🛠️ Technologies Used
- Python 3  
- Object-Oriented Programming (OOP)  
- Class Inheritance + Polymorphism  
- Private and protected attributes  
- Abstract base class from `abc`  
- Date/time calculations with `datetime`  
- List and dictionary handling  
- Conditionals and exception management

## ▶️ How to Run
1. Ensure Python 3 is installed  
2. Place all `.py` files into the same folder:
   - `workspace_logic_executor.py`  
   - `equipment_module.py`  
   - `entity_base.py`  
   - `staff_roles.py`  
   - `workspace_user_roles.py`  
3. Run with:

   `python workspace_logic_executor.py`

4. Observe login simulation, purchasing flow, staff analysis and equipment additions

## 📁 Project Structure
smart_office_staff_module/  
├── workspace_logic_executor.py *(system orchestrator)*  
├── equipment_module.py *(defines item logic)*  
├── entity_base.py *(abstract base for users/staff)*  
├── staff_roles.py *(subclasses for staff types)*  
├── workspace_user_roles.py *(subclasses for user types)*  
├── README.md  
└── .gitignore

## 💡 Skills Showcased
- Modular OOP architecture  
- Realistic user and staff behaviors (login, salary, working hours)  
- Tiered discounts based on internal spending  
- Abstract class inheritance and method enforcement  
- Runtime analytics: total spending, top performer detection

## 🧾 Conceptual Entities
- Equipment: `Wi-Fi Router`, `USB Keyboard`, `Optical Mouse`  
- Staff Types: Permanent, Contractual, Freelance  
- User Tiers: Standard, Base  
- Account operations: password setting, validation, purchase history

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)

## ⚖️ License
This project is covered under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
Shared exclusively for portfolio demonstration. Commercial usage or modification requires author consent.