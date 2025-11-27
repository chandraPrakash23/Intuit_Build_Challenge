import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;


//Shared buffer with thread-safe operations using wait/notify mechanism

class SharedBuffer<T> {
    private final Queue<T> queue;
    private final int capacity;
    
    public SharedBuffer(int capacity) {
        this.queue = new LinkedList<>();
        this.capacity = capacity;
    }
    
    // Producer adds item to the buffer,Blocks if buffer is full

    public synchronized void produce(T item) throws InterruptedException {
        while (queue.size() == capacity) {
            System.out.println(Thread.currentThread().getName() + 
                             " - Buffer full, waiting...");
            wait(); // Release lock and wait
        }
        
        queue.add(item);
        System.out.println(Thread.currentThread().getName() + 
                         " - Produced: " + item + " | Buffer size: " + queue.size());
        
        notifyAll(); // Wake up waiting consumers
    }
    
    //Consumer removes item from the buffer, Blocks if buffer is empty

    public synchronized T consume() throws InterruptedException {
        while (queue.isEmpty()) {
            System.out.println(Thread.currentThread().getName() + 
                             " - Buffer empty, waiting...");
            wait(); // Release lock and wait
        }
        
        T item = queue.poll();
        System.out.println(Thread.currentThread().getName() + 
                         " - Consumed: " + item + " | Buffer size: " + queue.size());
        
        notifyAll(); // Wake up waiting producers
        return item;
    }
    
    public synchronized int size() {
        return queue.size();
    }
}

//Producer thread that reads from source and puts items into shared buffer

class Producer<T> implements Runnable {
    private final List<T> source;
    private final SharedBuffer<T> buffer;
    private final long delayMs;
    
    public Producer(List<T> source, SharedBuffer<T> buffer, long delayMs) {
        this.source = source;
        this.buffer = buffer;
        this.delayMs = delayMs;
    }
    
    @Override
    public void run() {
        try {
            for (T item : source) {
                buffer.produce(item);
                Thread.sleep(delayMs); // Simulate processing time
            }
            System.out.println(Thread.currentThread().getName() + " - Finished producing");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println(Thread.currentThread().getName() + " interrupted");
        }
    }
}


// Consumer thread that reads from shared buffer and stores in destination

class Consumer<T> implements Runnable {
    private final SharedBuffer<T> buffer;
    private final List<T> destination;
    private final int itemsToConsume;
    private final long delayMs;
    
    public Consumer(SharedBuffer<T> buffer, List<T> destination, 
                   int itemsToConsume, long delayMs) {
        this.buffer = buffer;
        this.destination = destination;
        this.itemsToConsume = itemsToConsume;
        this.delayMs = delayMs;
    }
    
    @Override
    public void run() {
        try {
            for (int i = 0; i < itemsToConsume; i++) {
                T item = buffer.consume();
                destination.add(item);
                Thread.sleep(delayMs); // Simulate processing time
            }
            System.out.println(Thread.currentThread().getName() + " - Finished consuming");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println(Thread.currentThread().getName() + " interrupted");
        }
    }
}


//Main class

public class ProducerConsumerDemo {
    public static void main(String[] args) throws InterruptedException {
        // Configuration
        final int BUFFER_CAPACITY = 5;
        final int TOTAL_ITEMS = 20;
        final long PRODUCER_DELAY = 100; // ms
        final long CONSUMER_DELAY = 150; // ms (slower than producer)
        
        // Setup
        List<String> sourceData = new ArrayList<>();
        for (int i = 1; i <= TOTAL_ITEMS; i++) {
            sourceData.add("Item-" + i);
        }
        
        SharedBuffer<String> sharedBuffer = new SharedBuffer<>(BUFFER_CAPACITY);
        List<String> destinationData = new ArrayList<>();
        
        // Create producer and consumer threads
        Thread producerThread = new Thread(
            new Producer<>(sourceData, sharedBuffer, PRODUCER_DELAY),
            "Producer-1"
        );
        
        Thread consumerThread = new Thread(
            new Consumer<>(sharedBuffer, destinationData, TOTAL_ITEMS, CONSUMER_DELAY),
            "Consumer-1"
        );
        
        // Start threads
        System.out.println("=== Starting Producer-Consumer Demo ===\n");
        producerThread.start();
        consumerThread.start();
        
        // Wait for completion
        producerThread.join();
        consumerThread.join();
        
        // Display results
        System.out.println("\n=== Demo Complete ===");
        System.out.println("Total items produced: " + TOTAL_ITEMS);
        System.out.println("Total items consumed: " + destinationData.size());
        System.out.println("Final buffer size: " + sharedBuffer.size());
        System.out.println("\nDestination data (first 10): ");
        destinationData.stream().limit(10).forEach(System.out::println);
        
        // Demonstrate with multiple producers and consumers
        demonstrateMultipleThreads();
    }
    
    //Demonstrates multiple producers and consumers working concurrently

    private static void demonstrateMultipleThreads() throws InterruptedException {
        System.out.println("\n\n=== Multiple Producers & Consumers Demo ===\n");
        
        final int BUFFER_CAPACITY = 10;
        final int ITEMS_PER_PRODUCER = 15;
        
        SharedBuffer<Integer> buffer = new SharedBuffer<>(BUFFER_CAPACITY);
        List<Integer> destination = new ArrayList<>();
        
        // Created source data for two producers
        List<Integer> source1 = new ArrayList<>();
        List<Integer> source2 = new ArrayList<>();
        for (int i = 1; i <= ITEMS_PER_PRODUCER; i++) {
            source1.add(i * 100);
            source2.add(i * 200);
        }
        
        // Created threads
        Thread producer1 = new Thread(new Producer<>(source1, buffer, 80), "Producer-A");
        Thread producer2 = new Thread(new Producer<>(source2, buffer, 120), "Producer-B");
        Thread consumer1 = new Thread(new Consumer<>(buffer, destination, 15, 100), "Consumer-X");
        Thread consumer2 = new Thread(new Consumer<>(buffer, destination, 15, 100), "Consumer-Y");
        
        // Starting all threads
        producer1.start();
        producer2.start();
        consumer1.start();
        consumer2.start();
        
        // Waiting for completion
        producer1.join();
        producer2.join();
        consumer1.join();
        consumer2.join();
        
        System.out.println("\n=== Multiple Threads Demo Complete ===");
        System.out.println("Total items consumed: " + destination.size());
        System.out.println("Final buffer size: " + buffer.size());
    }
}