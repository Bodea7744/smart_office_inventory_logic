# 🧠 Smart Office Workspace Manager

This module represents a functional management system for handling staff, digital inventory, and internal users within a fictional smart office environment. It combines object-oriented logic with inventory simulation and personnel operations — providing a unified orchestration script (`workspace_manager.py`) that interacts with class modules representing employees, equipment, and platform users.

## 📌 Key Features
- Defines realistic equipment objects with prices, quantities, and descriptions
- Validates item stock levels (`check_stock()`)
- Represents office staff with location, salary, and email validation methods
- Allows dynamic salary increase using `increase_salary()` method
- Models workspace users with purchase history and expenditure tracking
- Supports runtime product assignment and spending analysis
- Centralized summary of all operations in `workspace_manager.py`

## 🛠️ Technologies Used
- Python 3  
- Object-Oriented Programming (OOP)  
- Custom classes with fields and instance methods  
- List handling and comprehension  
- String formatting and basic conditionals

## ▶️ How to Run
1. Make sure Python 3 is installed  
2. Ensure all module files (`equipment_class.py`, `staff_class.py`, `workspace_user_class.py`) are present  
3. Run the script using:

   `python workspace_manager.py`

4. View summary outputs in the console

## 📁 Project Structure
smart_office_workspace_manager/  
├── workspace_manager.py *(orchestrates full logic)*  
├── equipment_class.py *(models office inventory items)*  
├── staff_class.py *(represents internal employees)*  
├── workspace_user_class.py *(tracks user profiles and purchases)*  
├── README.md  
└── .gitignore

## 💡 Skills Showcased
- OOP principles: encapsulation, modularity, and class composition  
- Custom method design across independent entities  
- Cross-object interaction (users accessing products, employees receiving salary updates)  
- Runtime data validation and logical branching  
- Reusable class structure for expansion in later modules

## 🧾 Item Overview
Fictional smart office components:
- `DeskStation Pro` – high-performance workstation  
- `ErgoMouse X`, `FlexiBoard 5` – ergonomic peripherals  
- `ViewPanel HD` – visual equipment  
- `SoundBeam Headset` – audio unit for hybrid work setups

Staff members and platform users interact with this inventory dynamically, enabling realistic workspace simulations.

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)

## ⚖️ License
This project is distributed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/). It is provided strictly for portfolio and educational demonstration. Modification or commercial reuse requires prior consent.