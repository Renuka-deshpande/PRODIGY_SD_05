# PRODIGY_SD_05
Product Scraper 🛒
This project is a Python-based web scraper that parses an HTML file (Meesho.html) to extract product details, including the name, price, and rating of products listed on the Meesho website. The extracted data is saved into a CSV file for further analysis or usage.

FEATURES
1.HTML Parsing with BeautifulSoup: Reads a static Meesho HTML file and extracts relevant product details.
2.CSV Output: Saves extracted data into a neatly formatted CSV file for easy use.

REQUIREMENTS
To run this project, ensure you have the following installed:
1.Python 3.8+
2.Required Libraries:
----->BeautifulSoup4: For parsing HTML and extracting data.
Installation code:pip install beautifulsoup4
------>csv: For writing the extracted data into a CSV file.
This library is included in Python's standard library, so no installation is required.
------->lxml (Optional): For faster and more flexible parsing.
Installation:pip install lxml

HOW TO RUN THE PROJECT
1.Clone the Repository
2.Add the Meesho HTML File(given in the project):Place the Meesho.html file in the project directory
3.Run the Script:Execute the main Python script to extract product details:python main.py
4.Output:After running the script, the extracted data will be saved into a CSV file named MeeshoProducts.csv. Open this file to view the product details.



