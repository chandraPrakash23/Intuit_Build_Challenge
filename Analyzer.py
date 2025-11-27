import csv
from functools import reduce
from itertools import groupby
from operator import itemgetter
from typing import List, Dict, Any

class SalesAnalyzer:
    """Analyzes sales data using functional programming and stream operations."""
    
    def __init__(self, csv_file: str):
        """Initialize with CSV file path."""
        self.csv_file = csv_file
        self.data = []
    
    def load_data(self) -> List[Dict[str, Any]]:
        """Load and parse CSV data into a list of dictionaries."""
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)
            # Convert numeric fields
            self.data = list(map(lambda row: {
                'product': row['product'],
                'category': row['category'],
                'quantity': int(row['quantity']),
                'price': float(row['price']),
                'region': row['region']
            }, self.data))
        return self.data
    
    def total_sales(self) -> float:
        """Calculate total sales revenue using reduce."""
        return reduce(
            lambda acc, row: acc + (row['quantity'] * row['price']),
            self.data,
            0
        )
    
    def sales_by_category(self) -> Dict[str, float]:
        """Group sales by category and calculate totals."""
        # Sort by category for groupby
        sorted_data = sorted(self.data, key=itemgetter('category'))
        
        # Group and aggregate
        result = {}
        for category, items in groupby(sorted_data, key=itemgetter('category')):
            total = reduce(
                lambda acc, item: acc + (item['quantity'] * item['price']),
                items,
                0
            )
            result[category] = round(total, 2)
        return result
    
    def sales_by_region(self) -> Dict[str, float]:
        """Group sales by region and calculate totals."""
        sorted_data = sorted(self.data, key=itemgetter('region'))
        
        result = {}
        for region, items in groupby(sorted_data, key=itemgetter('region')):
            total = reduce(
                lambda acc, item: acc + (item['quantity'] * item['price']),
                items,
                0
            )
            result[region] = round(total, 2)
        return result
    
    def top_products(self, n: int = 5) -> List[tuple]:
        """Find top N products by revenue using functional operations."""
        # Calculate revenue for each product
        product_revenues = map(
            lambda row: (row['product'], row['quantity'] * row['price']),
            self.data
        )
        
        # Group by product and sum revenues
        sorted_revenues = sorted(product_revenues, key=itemgetter(0))
        product_totals = {}
        for product, items in groupby(sorted_revenues, key=itemgetter(0)):
            total = reduce(lambda acc, item: acc + item[1], items, 0)
            product_totals[product] = round(total, 2)
        
        # Sort and return top N
        return sorted(product_totals.items(), key=itemgetter(1), reverse=True)[:n]
    
    def filter_high_value_sales(self, threshold: float = 500) -> List[Dict]:
        """Filter sales where revenue exceeds threshold."""
        return list(filter(
            lambda row: (row['quantity'] * row['price']) > threshold,
            self.data
        ))
    
    def average_price_by_category(self) -> Dict[str, float]:
        """Calculate average price by category."""
        sorted_data = sorted(self.data, key=itemgetter('category'))
        
        result = {}
        for category, items in groupby(sorted_data, key=itemgetter('category')):
            items_list = list(items)
            avg = reduce(lambda acc, item: acc + item['price'], items_list, 0) / len(items_list)
            result[category] = round(avg, 2)
        return result
    
    def quantity_statistics(self) -> Dict[str, int]:
        """Calculate quantity statistics using functional operations."""
        quantities = list(map(lambda row: row['quantity'], self.data))
        
        return {
            'total': reduce(lambda acc, q: acc + q, quantities, 0),
            'max': reduce(lambda acc, q: max(acc, q), quantities, 0),
            'min': reduce(lambda acc, q: min(acc, q), quantities, quantities[0]),
            'count': len(quantities)
        }


def create_sample_csv(filename: str = 'sales_data.csv'):
    """Create a sample CSV file for testing."""
    sample_data = [
        ['product', 'category', 'quantity', 'price', 'region'],
        ['Laptop', 'Electronics', '5', '999.99', 'North'],
        ['Mouse', 'Electronics', '20', '29.99', 'South'],
        ['Desk', 'Furniture', '3', '349.99', 'East'],
        ['Chair', 'Furniture', '8', '199.99', 'West'],
        ['Monitor', 'Electronics', '10', '299.99', 'North'],
        ['Keyboard', 'Electronics', '15', '79.99', 'South'],
        ['Bookshelf', 'Furniture', '4', '149.99', 'East'],
        ['Lamp', 'Furniture', '12', '49.99', 'West'],
        ['Tablet', 'Electronics', '7', '499.99', 'North'],
        ['Webcam', 'Electronics', '25', '89.99', 'South']
    ]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    print(f"Sample CSV file '{filename}' created successfully!")


def main():
    """Main execution function."""
    csv_filename = 'sales_data.csv'
    
    # Create sample CSV
    create_sample_csv(csv_filename)
    
    # Initialize analyzer
    analyzer = SalesAnalyzer(csv_filename)
    analyzer.load_data()
    
    print("\n" + "="*60)
    print("SALES DATA ANALYSIS - FUNCTIONAL PROGRAMMING")
    print("="*60)
    
    # Total Sales
    total = analyzer.total_sales()
    print(f"\n1. Total Sales Revenue: ${total:,.2f}")
    
    # Sales by Category
    print("\n2. Sales by Category:")
    for category, amount in analyzer.sales_by_category().items():
        print(f"   {category}: ${amount:,.2f}")
    
    # Sales by Region
    print("\n3. Sales by Region:")
    for region, amount in analyzer.sales_by_region().items():
        print(f"   {region}: ${amount:,.2f}")
    
    # Top Products
    print("\n4. Top 5 Products by Revenue:")
    for i, (product, revenue) in enumerate(analyzer.top_products(5), 1):
        print(f"   {i}. {product}: ${revenue:,.2f}")
    
    # High Value Sales
    high_value = analyzer.filter_high_value_sales(1000)
    print(f"\n5. High Value Sales (>$1000): {len(high_value)} transactions")
    for sale in high_value:
        revenue = sale['quantity'] * sale['price']
        print(f"   {sale['product']}: ${revenue:,.2f}")
    
    # Average Price by Category
    print("\n6. Average Price by Category:")
    for category, avg in analyzer.average_price_by_category().items():
        print(f"   {category}: ${avg:,.2f}")
    
    # Quantity Statistics
    print("\n7. Quantity Statistics:")
    stats = analyzer.quantity_statistics()
    for key, value in stats.items():
        print(f"   {key.capitalize()}: {value}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()