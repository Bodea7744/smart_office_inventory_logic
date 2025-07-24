# 📊 Smart Office Supply Monitor

This Python script acts as the central execution point for tracking and validating internal inventory in a fictional digital workspace. It leverages functions from the `stock_metrics.py` module to evaluate product performance, correct anomalies, and generate actionable insights — all within a clean, modular framework designed for office supply management.

## 📌 Key Features
- Integrates with `stock_metrics.py` for inventory analysis  
- Automatically adds missing products (`WebVision Cam`) if absent  
- Applies corrections to tracked items (`ViewPanel HD` adjustment)  
- Performs full inventory validation for negative or oversized entries  
- Tests product access for non-existing items (`AirScan Pro`)  
- Generates summaries:
  - Total stock sold
  - Top and lowest-performing items
  - Stock below critical threshold

## 🛠️ Technologies Used
- Python 3  
- Modular script design via import statements  
- Dictionary manipulation (`sum()`, `max()`, `min()`)  
- Logical validation and exception handling  
- Structured print outputs for inventory reporting

## ▶️ How to Run
1. Make sure Python 3 is installed  
2. Ensure `stock_metrics.py` is present in the same folder  
3. Run the script using:

   `python supply_monitor.py`

4. View the validation messages and inventory summaries

## 📁 Project Structure
smart_office_supply_monitor/  
├── supply_monitor.py  
├── stock_metrics.py  
├── README.md  
└── .gitignore  

## 💡 Skills Showcased
- Importing and orchestrating functions across modules  
- Modular inventory control logic  
- Data validation and correction  
- Testing edge cases for missing and faulty entries  
- Output structuring and error reporting

## 🧾 Inventory Items Used
Fictional office supplies reflecting internal stock use:
- `DeskStation Pro`  
- `ErgoMouse X`  
- `FlexiBoard 5`  
- `ViewPanel HD`  
- `CableConnect Plus`  
- `WebVision Cam` *(added dynamically)*  
- `AirScan Pro` *(tested for access handling)*

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)

## ⚖️ License
This project is distributed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/) license. It is intended solely for educational and portfolio demonstration purposes. Modification or commercial reuse is prohibited without written permission.