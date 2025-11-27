# Producer-Consumer Pattern Implementation

A comprehensive Java implementation of the classic producer-consumer pattern demonstrating thread synchronization, concurrent programming, and inter-thread communication using wait/notify mechanisms.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Running Unit Tests](#running-unit-tests)
- [Output](#sample-output)
- [Technical Details](#technical-details)
- [Testing Objectives](#testing-objectives)

## 🎯 Overview

This project implements the producer-consumer pattern, a classic concurrency problem where:
- **Producer threads** generate data and place it into a shared buffer
- **Consumer threads** retrieve data from the shared buffer and process it
- **Shared buffer** acts as a bounded queue with thread-safe operations

The implementation demonstrates proper thread synchronization to prevent race conditions and ensures efficient coordination between producers and consumers.

## ✨ Features

- **Thread-Safe Shared Buffer**: Bounded queue with synchronized access
- **Wait/Notify Mechanism**: Proper thread coordination without busy-waiting
- **Multiple Producers & Consumers**: Support for concurrent multiple threads

## 📁 Project Structure

```
producer-consumer-demo/
├── ProducerConsumerDemo.java    # Main file containing all classes
├── README.md                     # This file
└── .gitignore                    # Git ignore file
```

**Note**: All classes (SharedBuffer, Producer, Consumer, ProducerConsumerDemo) are contained in a single file `ProducerConsumerDemo.java` for simplicity.

## 🔧 Prerequisites

- **Java Development Kit (JDK)**: Version 8 or higher
- **Maven** (optional): Version 3.6+ for dependency management and testing
- **JUnit**: Version 5.x (for running unit tests)
- **Git**: For cloning the repository

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/producer-consumer-demo.git
cd producer-consumer-demo
```

### 2. Compile the Code

**Simple compilation:**

```bash
# Compile the main file
javac ProducerConsumerDemo.java

# This creates .class files for all inner classes
```

### 3. Set Up IDE (Optional)

**IntelliJ IDEA:**
- File → Open → Select project directory
- IDE will auto-detect Java project

**Eclipse:**
- File → Import → Existing Projects into Workspace
- Select project directory

**VS Code:**
- Install "Extension Pack for Java"
- Open project folder

## ▶️ Running the Application

### Method 1: Command Line (Recommended)

```bash
# Compile
javac ProducerConsumerDemo.java

# Run
java ProducerConsumerDemo
```

### Method 2: Compile and Run in One Step

```bash
javac ProducerConsumerDemo.java && java ProducerConsumerDemo
```

### Method 3: Using IDE

- Open `ProducerConsumerDemo.java` in your IDE
- Right-click on the file
- Select "Run ProducerConsumerDemo.main()"

## 🧪 Running Unit Tests

### If you add ProducerConsumerTest.java:

**Compile tests:**
```bash
# Download JUnit if needed
# Then compile with JUnit in classpath
javac -cp .:junit-5.jar ProducerConsumerTest.java

# Run tests
java -cp .:junit-5.jar org.junit.runner.JUnitCore ProducerConsumerTest
```

### Simple Manual Testing

The main file includes two demo scenarios that serve as integration tests:
1. Single producer and consumer
2. Multiple producers and consumers

Simply run the program to see all test scenarios execute automatically.

## 📊 Output

### Basic Producer-Consumer Demo

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
Producer-1 - Produced: Item-11 | Buffer size: 4
Consumer-1 - Consumed: Item-8 | Buffer size: 3
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
```
```
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
Producer-A - Produced: 800 | Buffer size: 2
Consumer-Y - Consumed: 1200 | Buffer size: 1
Consumer-X - Consumed: 800 | Buffer size: 0
Producer-A - Produced: 900 | Buffer size: 1
Producer-B - Produced: 1400 | Buffer size: 2
Consumer-Y - Consumed: 900 | Buffer size: 1
Consumer-X - Consumed: 1400 | Buffer size: 0
Producer-A - Produced: 1000 | Buffer size: 1
Consumer-Y - Consumed: 1000 | Buffer size: 0
Producer-B - Produced: 1600 | Buffer size: 1
Producer-A - Produced: 1100 | Buffer size: 2
Consumer-X - Consumed: 1600 | Buffer size: 1
Consumer-Y - Consumed: 1100 | Buffer size: 0
Producer-A - Produced: 1200 | Buffer size: 1
Producer-B - Produced: 1800 | Buffer size: 2
Consumer-X - Consumed: 1200 | Buffer size: 1
Producer-A - Produced: 1300 | Buffer size: 2
Consumer-Y - Consumed: 1800 | Buffer size: 1
Consumer-X - Consumed: 1300 | Buffer size: 0
Producer-B - Produced: 2000 | Buffer size: 1
Producer-A - Produced: 1400 | Buffer size: 2
Consumer-Y - Consumed: 2000 | Buffer size: 1
Consumer-X - Consumed: 1400 | Buffer size: 0
Producer-B - Produced: 2200 | Buffer size: 1
Producer-A - Produced: 1500 | Buffer size: 2
Consumer-Y - Consumed: 2200 | Buffer size: 1
Producer-A - Finished producing
Consumer-X - Consumed: 1500 | Buffer size: 0
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
```

## 🔬 Technical Details

### Thread Synchronization Mechanisms

1. **Synchronized Methods**: Ensures mutual exclusion for critical sections
2. **Wait/Notify**: Efficient thread coordination without busy-waiting
3. **Bounded Buffer**: Fixed-size queue to test blocking scenarios
4. **Generic Implementation**: Type-safe operations using Java generics

### Key Classes

**SharedBuffer**
- Thread-safe bounded buffer implementation
- Methods: `produce()`, `consume()`, `size()`
- Uses `wait()` and `notifyAll()` for coordination

**Producer**
- Reads from source container
- Places items into shared buffer
- Blocks when buffer is full

**Consumer**
- Reads from shared buffer
- Stores items in destination container
- Blocks when buffer is empty

### Configuration Parameters

```java
BUFFER_CAPACITY = 5;           // Maximum buffer size
TOTAL_ITEMS = 20;              // Items to produce
PRODUCER_DELAY = 100;          // Producer delay in ms
CONSUMER_DELAY = 150;          // Consumer delay in ms
```

## ✅ Testing Objectives

The implementation thoroughly tests:

- ✓ **Thread Synchronization**: Proper locking and mutual exclusion
- ✓ **Concurrent Programming**: Multiple threads working simultaneously
- ✓ **Blocking Queues**: Correct blocking behavior when full/empty
- ✓ **Wait/Notify Mechanism**: Efficient thread coordination
- ✓ **Race Condition Prevention**: No data corruption
- ✓ **Deadlock Prevention**: Threads don't get stuck
- ✓ **Data Integrity**: All produced items are consumed correctly

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📥 Download Instructions

To use this README:
1. Click the copy icon (📋) in the top-right corner of this artifact
2. Create a file named `README.md` in your project root directory
3. Paste the content and save
4. Update the author section with your information
5. Replace `yourusername` with your actual GitHub username

## 🙏 Acknowledgments

- Classic producer-consumer pattern from operating systems literature
- Java concurrency best practices
- Thread synchronization patterns

---

**Note**: Replace `yourusername` with your actual GitHub username before publishing.
