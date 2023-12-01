# Hash Table
* A hash table is a data structure that utilizes a hash function to map keys to indices in an array. Each slot in the array is commonly referred to as a "bucket." While one common implementation uses linked lists for buckets, other methods such as arrays or alternative data structures can be employed to handle collisions.

## Key Components
### Array
* The primary storage structure where elements are stored. Each element is placed in a location determined by a hash function.

### Hash Function
* A function that takes a key as input and produces an index (hash code) in the array where the corresponding value can be found. It's crucial that the hash function distributes keys relatively uniformly to avoid clustering.

### Bucket
* A slot or cell in the array. When multiple keys hash to the same index (a collision), a bucket is used to store all these keys and their associated values. IDEALLY YOU WANT A PRIME NUMBER OF BUCKETS TO INCREASE RANDOMNESS AND DECREASE THE NUMBER OF COLLISIONS

### Linked List (or other collision resolution method)
* When a collision occurs (i.e., two keys hash to the same index), a linked list (or another method like open addressing or separate chaining with other data structures) is often used to manage multiple key-value pairs in the same bucket.

<br> <br> <br>

# Advantages and Big-O of Hash Tables

Hash tables offer several advantages in terms of efficiency and performance:

## Advantages

### 1. Fast Retrieval

Hash tables provide constant-time average-case complexity for key lookup, insertion, and deletion operations. This makes them ideal for scenarios where quick access to data is crucial.

### 2. Dynamic Size

Hash tables can dynamically resize to accommodate varying numbers of elements efficiently. This adaptability ensures that they can handle changes in the dataset size without a significant impact on performance.

### 3. Uniform Distribution

When implemented correctly, hash functions distribute keys uniformly across the array, minimizing collisions and optimizing search times.

### 4. Versatility

Hash tables can be used in various applications, ranging from caching mechanisms to symbol tables, providing a versatile solution for different problem domains.

## Big-O Complexity

The average-case time complexity of fundamental hash table operations is O(1), making them highly efficient for scenarios where constant-time performance is crucial. However, in the worst case, especially in the presence of frequent collisions, the time complexity can degrade to O(n), where n is the number of elements.

It's essential to choose an appropriate hash function and handle collisions effectively to maintain the optimal performance of a hash table.


<br> <br>

# Worst-Case Scenarios for Hash Table Operations

1. **Worst Case for Lookup (Search):**
   - Time Complexity: O(n)
   - Array: O(1) <-- with direct access to index else O(n)
   - Scenario: When there are frequent collisions, and many keys hash to the same index, causing a linear search within a bucket.

2. **Worst Case for Insertion:**
   - Time Complexity: O(n)
   - Array: O(n)
   - Scenario: Similar to lookup, when there are significant collisions, and the hash table needs to handle a large number of elements in a single bucket, resulting in a linear search for insertion.

3. **Worst Case for Deletion:**
   - Time Complexity: O(n)
   - Array: O(n)
   - Scenario: In the presence of collisions, especially when a large number of keys hash to the same index, deletion may involve searching within a bucket, resulting in a linear time complexity.
