from bs4 import BeautifulSoup
import csv

def scrape_meesho():
    # File path to the local Meesho HTML file
    file_path = "meesho.html"  # Replace with your local file path

    # Read the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all product divs
    divs = soup.find_all("div", class_="sc-dkrFOg ProductList__GridCol-sc-8lnc8o-0 cokuZA eCJiSA")

    # Prepare data
    data = []
    for div in divs:
        # Extract Product Name
        try:
            product_name = div.find(
                "p",
                {
                    "font-size": "16px",
                    "font-weight": "book",
                    "color": "greyT2",
                    "class": "sc-eDvSVe gQDOBc NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU",
                },
            ).text.strip()
        except AttributeError:
            product_name = " "

        # Extract Product Price
        try:
            product_price_div = div.find(
                "div",
                class_="sc-ftTHYK ijCOEg NewProductCardstyled__PriceRow-sc-6y2tys-7 aLtVl NewProductCardstyled__PriceRow-sc-6y2tys-7 aLtVl",
                attrs={"color": "white"},
            )
            product_price = product_price_div.find("h5").text.strip()
        except AttributeError:
            product_price = " "

        # Extract Product Rating
        try:
            product_rating = div.find("span", class_="sc-eDvSVe laVOtN").text.strip()
        except AttributeError:
            product_rating = "No rating available"

        # Append extracted data
        data.append([product_name, product_price, product_rating])

    # Write data to CSV
    with open("MeeshoProducts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product_Name", "Product_Price", "Product_Rating"])  # Headers
        writer.writerows(data)

    print("Data successfully written to MeeshoProducts.csv")

# Run the scraper
scrape_meesho()
