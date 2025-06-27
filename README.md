📊 Agmarknet-scraper

A Python automation project to extract agricultural market price data from [Agmarknet.gov.in](https://agmarknet.gov.in) and export it as structured Excel files.

This tool helps students, researchers, and analysts retrieve historical commodity prices by state, district, and market — ideal for agricultural economics and market studies.


🎥 Demo Video

▶️ [Watch here](https://drive.google.com/file/d/1VA7qpr_pNQp68gpPe7WWOdOmeD8ySC2Y/view?usp=sharing)



✅ Features

* 🌾 Scrapes market price data by selecting:
* Commodity
* State → District → Market
* Custom date range (From / To)
* 📄 Exports clean tabular data to Excel (.xlsx)
* ❌ Handles “No Records Found” and slow-loading dropdowns
* 🧠 Useful for analysis, research, and academic purposes



🛠 Technologies Used

* Python 3
* Selenium
* Pandas
* OpenPyXL
* Colorama (for colored CLI output)


📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/agmarknet-scraper.git
   cd agmarknet-scraper
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

🚀 How to Use

1. Run the script:

   ```bash
   python agmarknet_scraper.py
   ```

2. Provide input in the terminal:

   * Commodity: e.g., Tuberose
   * State: e.g., Tamil Nadu
   * District: e.g., Erode
   * Market: e.g., Sathyamangalam
   * From Date: e.g., 01-Jan-2024
   * To Date: e.g., 31-May-2024

3. Output:
   An Excel file will be saved in your project directory named like:

   ```
   Tuberose_Erode_Sathyamangalam_01-Jan-2024_to_31-May-2024.xlsx
   ```



🧾 Sample Output

| State      | District | Market         | Commodity | Variety | Grade | Min Price | Max Price | Modal Price | Date        |
| ---------- | -------- | -------------- | --------- | ------- | ----- | --------- | --------- | ----------- | ----------- |
| Tamil Nadu | Erode    | Sathyamangalam | Tuberose  | Local   | A     | ₹100      | ₹150      | ₹120        | 02-Jan-2024 |



📌 Use Cases

* 📈 Agricultural market analysis
* 📚 Academic research in agri-economics
* 🗂 Market trend studies for policy or farm management



👤 Author

Melvin Joshuva Seelan M  
📧 LinkedIn: [melvin-joshuva-seelan-m](https://www.linkedin.com/in/melvin-joshuva-seelan-m-590287297)



