# 🧠 Smart Office Personnel & Inventory Model

This module simulates an object-oriented representation of staff members, users, and digital equipment within a fictional smart office infrastructure. It integrates concepts like inheritance (`Person`), polymorphism (`display_info()`), and data encapsulation to reflect real-world operations — from salary adjustments and email verification to inventory assignment and user expense tracking.

## 📌 Key Features
- Defines `Equipment` items with encapsulated pricing and descriptive fields  
- Represents employees (`StaffMember`) and platform users (`WorkspaceUser`) via shared base class (`Person`)  
- Validates email formats  
- Tracks product stock and triggers alerts for low availability  
- Applies salary increments and exposes encapsulated salary data  
- Calculates user expenses based on assigned equipment  
- Demonstrates polymorphism with `display_info()` behavior across user types

## 🛠️ Technologies Used
- Python 3  
- Object-Oriented Programming (OOP)  
- Class inheritance and polymorphic methods  
- Encapsulation with private and protected attributes  
- Abstract base classes (`abc.ABC`)  
- Formatted string outputs for data reporting

## ▶️ How to Run
1. Make sure Python 3 is installed  
2. Ensure all files are in the same directory:  
   - `smart_office_orchestrator.py`  
   - `equipment_module.py`  
   - `staff_member.py`  
   - `workspace_user.py`  
   - `person_base.py`  
3. Run using:

   `python smart_office_orchestrator.py`

4. View inventory checks, salary updates, and user interaction summaries

## 📁 Project Structure
smart_office_oop_module/  
├── smart_office_orchestrator.py *(runs full logic)*  
├── equipment_module.py *(defines item logic)*  
├── person_base.py *(abstract parent class)*  
├── staff_member.py *(models employee behavior)*  
├── workspace_user.py *(models user behavior)*  
├── README.md  
└── .gitignore

## 💡 Skills Showcased
- Multi-class system integration  
- Abstract base class design  
- Encapsulation and visibility modifiers  
- Polymorphic data output  
- Modular code and professional naming conventions

## 🧾 Conceptual Entities
- `DeskStation Pro`, `ErgoMouse X`, `FlexiBoard 5` – examples of tracked smart office items  
- Staff and user profiles structured with clear data access boundaries  
- Expense tracking via assigned equipment prices

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)

## ⚖️ License
This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/). Provided solely for educational and portfolio purposes. Commercial usage or modifications are prohibited without author consent.