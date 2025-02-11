from django.shortcuts import render
from .scrapper import scrape_merolagani  # Import the scraper function

def stock_market_view(request):
    # Call the scraper function to get the data
    data = scrape_merolagani()

    # Process the data: Replace '.' with '_' in keys and convert 'Qty' to integers
    for stock in data:
        # Handle the 'Qty.' key and clean its value
        if 'Qty.' in stock:
            stock['Qty'] = int(stock.pop('Qty.', '0').replace(',', ''))  # Replace 'Qty.' with 'Qty', convert to int

    # Sort the entire data in descending order of 'Qty'
    sorted_data = sorted(data, key=lambda x: x.get('Qty', 0), reverse=True)

    # Render the sorted data to the template
    return render(request, 'stock.html', {'new': sorted_data})
