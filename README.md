# Producer-Consumer Pattern & Sales Data Analysis

A collection of Python applications demonstrating concurrent programming patterns and functional programming with data analysis.

## 📋 Quick Navigation

### 🔗 Jump to Projects
- **[Project 1: Producer-Consumer Pattern](#project-1-producer-consumer-pattern)** ⚡
- **[Project 2: Sales Data Analysis](#project-2-sales-data-analysis)** 📊

### 🔗 Other Sections
- [Projects Overview](#projects-overview)
- [Installation](#installation)
- [Requirements](#requirements)
- [Key Concepts](#key-concepts)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Projects Overview

### 1. Producer-Consumer Pattern
Implements the classic producer-consumer concurrency pattern using threads, queues, and synchronization mechanisms for efficient multi-threaded data processing.

### 2. Sales Data Analysis with Functional Programming
Demonstrates proficiency with functional programming paradigms including stream operations, lambda expressions, and data aggregation on CSV data.

---

## 💻 Installation

### Prerequisites
- Python 3.7 or higher
- Standard library (no external dependencies required)
- Java

### Setup
```bash
# Clone or download the project files
git clone <repository-url>
cd <file-name>

# No additional installation needed - uses Python standard library
```

---

## 🔄 Project 1: Producer-Consumer Pattern

### Description
Implements the classic producer-consumer concurrency pattern using Python's threading and queue modules, demonstrating thread synchronization and inter-thread communication.

### Features
- **Multi-threaded Production** - Multiple producer threads generating data
- **Multi-threaded Consumption** - Multiple consumer threads processing data
- **Thread-safe Queue** - Synchronized data exchange between threads
- **Graceful Shutdown** - Proper termination of all threads
- **Configurable Parameters** - Adjustable thread counts and production rates
- **Real-time Monitoring** - Track production and consumption in real-time

🚀 Setup Instructions
1. Clone the Repository
bashgit clone https://github.com/yourusername/producer-consumer-pattern.git
cd producer-consumer-pattern
2. Compile the Code
Option A: Using javac (without build tool)
bash# Compile all source files
javac -d bin src/main/java/*.java

# Compile with source and target compatibility
javac -source 8 -target 8 -d bin src/main/java/*.java
Option B: Using Maven
bashmvn clean compile
Option C: Using Gradle
bashgradle build
3. Set Up IDE (Optional)
IntelliJ IDEA:

File → Open → Select project directory
IDE will auto-detect Java project

Eclipse:

File → Import → Existing Projects into Workspace
Select project directory

VS Code:

Install "Extension Pack for Java"
Open project folder

▶️ Running the Application
Method 1: Command Line
bash# Run from compiled classes
java -cp bin ProducerConsumerDemo

# Or compile and run in one step
javac src/main/java/*.java && java -cp src/main/java ProducerConsumerDemo
Method 2: Using Maven
bashmvn exec:java -Dexec.mainClass="ProducerConsumerDemo"
Method 3: Using Gradle
bashgradle run
Method 4: IDE

Right-click on ProducerConsumerDemo.java
Select "Run ProducerConsumerDemo.main()"

🧪 Running Unit Tests
Using Maven
bash# Run all tests
mvn test

# Run specific test class
mvn test -Dtest=SharedBufferTest

# Run with verbose output
mvn test -X
Using Gradle
bash# Run all tests
gradle test

# Run specific test
gradle test --tests SharedBufferTest
Using JUnit Console Launcher
bash# Compile tests
javac -cp .:junit-platform-console-standalone.jar -d bin src/test/java/*.java

# Run tests
java -jar junit-platform-console-standalone.jar --class-path bin 

### Sample Output
```
=== Starting Producer-Consumer Demo ===

Consumer-1 - Buffer empty, waiting...
Producer-1 - Produced: Item-1 | Buffer size: 1
Consumer-1 - Consumed: Item-1 | Buffer size: 0
Producer-1 - Produced: Item-2 | Buffer size: 1
Consumer-1 - Consumed: Item-2 | Buffer size: 0
Producer-1 - Produced: Item-3 | Buffer size: 1
Consumer-1 - Consumed: Item-3 | Buffer size: 0
Producer-1 - Produced: Item-4 | Buffer size: 1
Producer-1 - Produced: Item-5 | Buffer size: 2
Consumer-1 - Consumed: Item-4 | Buffer size: 1
Producer-1 - Produced: Item-6 | Buffer size: 2
Consumer-1 - Consumed: Item-5 | Buffer size: 1
Producer-1 - Produced: Item-7 | Buffer size: 2
Producer-1 - Produced: Item-8 | Buffer size: 3
Consumer-1 - Consumed: Item-6 | Buffer size: 2
Producer-1 - Produced: Item-9 | Buffer size: 3
Consumer-1 - Consumed: Item-7 | Buffer size: 2
Producer-1 - Produced: Item-10 | Buffer size: 3
Consumer-1 - Consumed: Item-8 | Buffer size: 2
Producer-1 - Produced: Item-11 | Buffer size: 3
Producer-1 - Produced: Item-12 | Buffer size: 4
Consumer-1 - Consumed: Item-9 | Buffer size: 3
Producer-1 - Produced: Item-13 | Buffer size: 4
Consumer-1 - Consumed: Item-10 | Buffer size: 3
Producer-1 - Produced: Item-14 | Buffer size: 4
Producer-1 - Produced: Item-15 | Buffer size: 5
Consumer-1 - Consumed: Item-11 | Buffer size: 4
Producer-1 - Produced: Item-16 | Buffer size: 5
Consumer-1 - Consumed: Item-12 | Buffer size: 4
Producer-1 - Produced: Item-17 | Buffer size: 5
Producer-1 - Buffer full, waiting...
Consumer-1 - Consumed: Item-13 | Buffer size: 4
Producer-1 - Produced: Item-18 | Buffer size: 5
Producer-1 - Buffer full, waiting...
Consumer-1 - Consumed: Item-14 | Buffer size: 4
Producer-1 - Produced: Item-19 | Buffer size: 5
Producer-1 - Buffer full, waiting...
Consumer-1 - Consumed: Item-15 | Buffer size: 4
Producer-1 - Produced: Item-20 | Buffer size: 5
Producer-1 - Finished producing
Consumer-1 - Consumed: Item-16 | Buffer size: 4
Consumer-1 - Consumed: Item-17 | Buffer size: 3
Consumer-1 - Consumed: Item-18 | Buffer size: 2
Consumer-1 - Consumed: Item-19 | Buffer size: 1
Consumer-1 - Consumed: Item-20 | Buffer size: 0
Consumer-1 - Finished consuming

=== Demo Complete ===
Total items produced: 20
Total items consumed: 20
Final buffer size: 0

Destination data (first 10):
Item-1
Item-2
Item-3
Item-4
Item-5
Item-6
Item-7
Item-8
Item-9
Item-10


=== Multiple Producers & Consumers Demo ===

Producer-B - Produced: 200 | Buffer size: 1
Consumer-Y - Consumed: 200 | Buffer size: 0
Consumer-X - Buffer empty, waiting...
Producer-A - Produced: 100 | Buffer size: 1
Consumer-X - Consumed: 100 | Buffer size: 0
Producer-A - Produced: 200 | Buffer size: 1
Consumer-Y - Consumed: 200 | Buffer size: 0
Consumer-X - Buffer empty, waiting...
Producer-B - Produced: 400 | Buffer size: 1
Consumer-X - Consumed: 400 | Buffer size: 0
Producer-A - Produced: 300 | Buffer size: 1
Consumer-Y - Consumed: 300 | Buffer size: 0
Consumer-X - Buffer empty, waiting...
Producer-B - Produced: 600 | Buffer size: 1
Consumer-X - Consumed: 600 | Buffer size: 0
Producer-A - Produced: 400 | Buffer size: 1
Consumer-Y - Consumed: 400 | Buffer size: 0
Consumer-X - Buffer empty, waiting...
Producer-A - Produced: 500 | Buffer size: 1
Consumer-X - Consumed: 500 | Buffer size: 0
Producer-B - Produced: 800 | Buffer size: 1
Consumer-Y - Consumed: 800 | Buffer size: 0
Producer-A - Produced: 600 | Buffer size: 1
Consumer-X - Consumed: 600 | Buffer size: 0
Producer-B - Produced: 1000 | Buffer size: 1
Consumer-Y - Consumed: 1000 | Buffer size: 0
Producer-A - Produced: 700 | Buffer size: 1
Consumer-X - Consumed: 700 | Buffer size: 0
Producer-B - Produced: 1200 | Buffer size: 1
Consumer-Y - Consumed: 1200 | Buffer size: 0
Producer-A - Produced: 800 | Buffer size: 1
Consumer-X - Consumed: 800 | Buffer size: 0
Producer-A - Produced: 900 | Buffer size: 1
Consumer-Y - Consumed: 900 | Buffer size: 0
Producer-B - Produced: 1400 | Buffer size: 1
Consumer-X - Consumed: 1400 | Buffer size: 0
Producer-A - Produced: 1000 | Buffer size: 1
Consumer-Y - Consumed: 1000 | Buffer size: 0
Producer-B - Produced: 1600 | Buffer size: 1
Consumer-X - Consumed: 1600 | Buffer size: 0
Producer-A - Produced: 1100 | Buffer size: 1
Consumer-Y - Consumed: 1100 | Buffer size: 0
Producer-B - Produced: 1800 | Buffer size: 1
Producer-A - Produced: 1200 | Buffer size: 2
Consumer-X - Consumed: 1800 | Buffer size: 1
Consumer-Y - Consumed: 1200 | Buffer size: 0
Producer-A - Produced: 1300 | Buffer size: 1
Producer-B - Produced: 2000 | Buffer size: 2
Consumer-X - Consumed: 1300 | Buffer size: 1
Consumer-Y - Consumed: 2000 | Buffer size: 0
Producer-A - Produced: 1400 | Buffer size: 1
Consumer-X - Consumed: 1400 | Buffer size: 0
Producer-B - Produced: 2200 | Buffer size: 1
Producer-A - Produced: 1500 | Buffer size: 2
Consumer-Y - Consumed: 2200 | Buffer size: 1
Consumer-X - Consumed: 1500 | Buffer size: 0
Producer-A - Finished producing
Producer-B - Produced: 2400 | Buffer size: 1
Consumer-Y - Consumed: 2400 | Buffer size: 0
Consumer-X - Buffer empty, waiting...
Producer-B - Produced: 2600 | Buffer size: 1
Consumer-X - Consumed: 2600 | Buffer size: 0
Consumer-Y - Buffer empty, waiting...
Consumer-X - Buffer empty, waiting...
Producer-B - Produced: 2800 | Buffer size: 1
Consumer-Y - Consumed: 2800 | Buffer size: 0
Consumer-X - Buffer empty, waiting...
Consumer-Y - Finished consuming
Producer-B - Produced: 3000 | Buffer size: 1
Consumer-X - Consumed: 3000 | Buffer size: 0
Consumer-X - Finished consuming
Producer-B - Finished producing

=== Multiple Threads Demo Complete ===
Total items consumed: 30
Final buffer size: 0
============================================
```

### Key Concepts Demonstrated

1. **Thread Synchronization**
   - Queue-based synchronization
   - Lock-free communication
   - Thread-safe operations

2. **Concurrency Patterns**
   - Multiple producers, multiple consumers
   - Shared resource management
   - Graceful shutdown mechanisms

3. **Queue Management**
   - Bounded buffer implementation
   - Blocking operations (put/get)
   - Queue full/empty handling

4. **Thread Lifecycle**
   - Thread creation and startup
   - Thread joining and cleanup
   - Daemon vs non-daemon threads

### Architecture Diagram
```
┌─────────────┐
│ Producer 1  │─┐
└─────────────┘ │
┌─────────────┐ │    ┌──────────────┐    ┌─────────────┐
│ Producer 2  │─┼───→│ Thread-Safe  │───→│ Consumer 1  │
└─────────────┘ │    │    Queue     │    └─────────────┘
┌─────────────┐ │    │  (Size: 10)  │    ┌─────────────┐
│ Producer 3  │─┘    └──────────────┘───→│ Consumer 2  │
└─────────────┘                           └─────────────┘
```

**[⬆ Back to Top](#-quick-navigation)**

---

## 📊 Project 2: Sales Data Analysis

### Description
Analyzes sales data from CSV files using functional programming techniques including map, filter, reduce, and groupby operations.

### Features
- **Total Sales Calculation** - Aggregates total revenue using reduce
- **Category Analysis** - Groups and sums sales by product category
- **Regional Analysis** - Groups and sums sales by region
- **Top Products** - Identifies highest revenue generating products
- **High-Value Filtering** - Filters transactions exceeding threshold
- **Statistical Analysis** - Calculates averages and statistics
- **Automatic CSV Generation** - Creates sample data for testing

### File Structure
```
sales_analyzer.py          # Main analysis application
sales_data.csv            # Generated sample data (auto-created)
```

### Usage

#### Running the Analysis
```bash
python sales_analyzer.py
```

#### Using as a Module
```python
from sales_analyzer import SalesAnalyzer

# Initialize with CSV file
analyzer = SalesAnalyzer('sales_data.csv')
analyzer.load_data()

# Perform analysis
total = analyzer.total_sales()
by_category = analyzer.sales_by_category()
top_5 = analyzer.top_products(5)
high_value = analyzer.filter_high_value_sales(1000)

print(f"Total Sales: ${total:,.2f}")
print(f"Sales by Category: {by_category}")
print(f"Top Products: {top_5}")
```

#### Creating Custom CSV Data
```python
import csv

data = [
    ['product', 'category', 'quantity', 'price', 'region'],
    ['Laptop', 'Electronics', '5', '999.99', 'North'],
    ['Desk', 'Furniture', '3', '349.99', 'East'],
    ['Mouse', 'Electronics', '20', '29.99', 'South']
]

with open('custom_sales.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Analyze custom data
analyzer = SalesAnalyzer('custom_sales.csv')
analyzer.load_data()
results = analyzer.sales_by_category()
```

#### Batch Analysis Example
```python
import glob

# Analyze multiple CSV files
csv_files = glob.glob('sales_*.csv')
total_revenue = 0

for csv_file in csv_files:
    analyzer = SalesAnalyzer(csv_file)
    analyzer.load_data()
    total_revenue += analyzer.total_sales()
    print(f"{csv_file}: ${analyzer.total_sales():,.2f}")

print(f"\nGrand Total: ${total_revenue:,.2f}")
```

### Sample Output
```

============================================================
SALES DATA ANALYSIS - FUNCTIONAL PROGRAMMING
============================================================

1. Total Sales Revenue: $19,398.91

2. Sales by Category:
   Electronics: $15,549.18
   Furniture: $3,849.73

3. Sales by Region:
   East: $1,649.93
   North: $11,499.78
   South: $4,049.40
   West: $2,199.80

4. Top 5 Products by Revenue:
   1. Laptop: $4,999.95
   2. Tablet: $3,499.93
   3. Monitor: $2,999.90
   4. Webcam: $2,249.75
   5. Chair: $1,599.92

5. High Value Sales (>$1000): 7 transactions
   Laptop: $4,999.95
   Desk: $1,049.97
   Chair: $1,599.92
   Monitor: $2,999.90
   Keyboard: $1,199.85
   Tablet: $3,499.93
   Webcam: $2,249.75

6. Average Price by Category:
   Electronics: $333.32
   Furniture: $187.49

7. Quantity Statistics:
   Total: 109
   Max: 25
   Min: 3
   Count: 10
============================================================
```

### Functional Programming Techniques Used

1. **Lambda Expressions**
   ```python
   lambda row: row['quantity'] * row['price']
   lambda acc, row: acc + (row['quantity'] * row['price'])
   ```

2. **Map Operations**
   ```python
   map(lambda row: (row['product'], row['quantity'] * row['price']), data)
   ```

3. **Filter Operations**
   ```python
   filter(lambda row: (row['quantity'] * row['price']) > threshold, data)
   ```

4. **Reduce Operations**
   ```python
   reduce(lambda acc, row: acc + (row['quantity'] * row['price']), data, 0)
   reduce(lambda acc, q: max(acc, q), quantities, 0)
   ```

5. **GroupBy Operations**
   ```python
   groupby(sorted_data, key=itemgetter('category'))
   groupby(sorted_data, key=itemgetter('region'))
   ```

### CSV Data Format
```csv
product,category,quantity,price,region
Laptop,Electronics,5,999.99,North
Mouse,Electronics,20,29.99,South
Desk,Furniture,3,349.99,East
```

**Required Fields:**
- `product` - Product name (string)
- `category` - Product category (string)
- `quantity` - Units sold (integer)
- `price` - Unit price (float)
- `region` - Sales region (string)

**[⬆ Back to Top](#-quick-navigation)**

---

## 📦 Requirements

### Python Standard Library Modules Used

#### Producer-Consumer Pattern
```python
threading              # Thread management
queue                  # Thread-safe queue
time                   # Sleep and timing
random                 # Random delays (optional)
```

#### Sales Data Analysis
```python
csv                    # CSV file reading/writing
functools.reduce       # Functional aggregation
itertools.groupby      # Data grouping
operator.itemgetter    # Key extraction
typing                 # Type hints
```

### System Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: 3.7+
- **Memory**: 50MB+ available RAM
- **Disk**: 10MB+ available space

---

## 🔑 Key Concepts

### Functional Programming (Project 2)
- **Immutability** - Working with immutable data structures
- **Pure Functions** - Functions without side effects
- **Higher-Order Functions** - Functions that take/return functions
- **Lazy Evaluation** - Deferred computation with iterators
- **Function Composition** - Combining simple functions

### Concurrent Programming (Project 1)
- **Thread Safety** - Protecting shared resources
- **Synchronization** - Coordinating thread execution
- **Deadlock Prevention** - Avoiding circular dependencies
- **Race Conditions** - Managing concurrent access
- **Producer-Consumer Pattern** - Decoupling production from consumption

---

## 🐛 Troubleshooting

### Common Issues

#### Issue 1: CSV File Not Found
```
Error: FileNotFoundError: [Errno 2] No such file or directory: 'sales_data.csv'
```
**Solution**: Run the script once to auto-generate sample data, or create your own CSV file.

#### Issue 2: Thread Deadlock
```
Problem: Program hangs and doesn't complete
```
**Solution**: Ensure producers send sentinel values and consumers properly exit on sentinel.

#### Issue 3: Import Errors
```
Error: ModuleNotFoundError: No module named 'X'
```
**Solution**: All modules used are from Python standard library. Ensure Python 3.7+ is installed.

#### Issue 4: Queue Full/Empty Errors
```
Problem: Queue blocks indefinitely
```
**Solution**: Adjust `queue_size` parameter or implement timeout handling.

---

## 📝 License

This project is provided as-is for educational purposes.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

**[⬆ Back to Top](#-quick-navigation)**
