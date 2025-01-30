### 1. What is the difference between JDK, JRE, and JVM?
- **JDK (Java Development Kit)**: It is a full-featured software development kit for Java, including JRE and development tools like compilers, debuggers, etc.
- **JRE (Java Runtime Environment)**: It provides the libraries and other resources necessary to run Java programs. It includes JVM but not development tools.
- **JVM (Java Virtual Machine)**: It is the engine that runs Java bytecode. It’s responsible for converting bytecode into machine-specific code.



### 2. What is the use of the `static` keyword in Java?
The `static` keyword in Java is used for memory management. It can be applied to variables, methods, and blocks to denote that they belong to the class, rather than any particular instance.



### 3. What is the difference between `==` and `equals()` in Java?
- `==` is a reference comparison operator. It checks if two object references point to the same memory location.
- `equals()` is a method in the `Object` class that compares the contents of two objects, assuming the method is overridden in the class.



### 4. What are the different types of memory areas allocated by JVM?
The JVM allocates memory in the following areas:
- **Heap**: Stores objects and class instances.
- **Stack**: Stores method calls, local variables, and control flow.
- **Method Area**: Stores class definitions and metadata.
- **Program Counter Register**: Keeps track of the current instruction.



### 5. What are the key features of Java?
- **Object-Oriented**: Everything in Java is treated as an object.
- **Platform Independent**: Java code can run on any platform with the help of JVM.
- **Multithreaded**: Java supports multithreading, allowing multiple threads to run concurrently.
- **Robust**: Java has strong memory management and exception handling.



### 6. What is an abstract class in Java?
An **abstract class** is a class that cannot be instantiated. It is used to provide a common base for other classes. It can contain abstract methods (without implementation) and concrete methods (with implementation).



### 7. What is the difference between an interface and an abstract class in Java?
- **Abstract class** can have both abstract and concrete methods. It can also have member variables.
- **Interface** can only have abstract methods (until Java 8, after which it can have default and static methods). Interfaces cannot have instance variables, only constants.



### 8. What is the significance of `final` keyword in Java?
- **`final` variable**: Once assigned, its value cannot be changed.
- **`final method`**: The method cannot be overridden in subclasses.
- **`final class`**: The class cannot be subclassed.



### 9. Explain the concept of inheritance in Java.
**Inheritance** is a fundamental OOP concept where a new class (subclass) inherits properties and behaviors (methods) from an existing class (superclass). It allows for code reuse and method overriding.



### 10. What is polymorphism in Java?
**Polymorphism** allows objects of different classes to be treated as objects of a common superclass. It is of two types:
- **Compile-time polymorphism (Method Overloading)**: The method to be called is resolved at compile time.
- **Run-time polymorphism (Method Overriding)**: The method to be called is resolved at runtime.



### 11. What is method overloading in Java?
**Method overloading** occurs when two or more methods in the same class have the same name but different parameters (either in number, type, or both).



### 12. What is method overriding in Java?
**Method overriding** happens when a subclass provides its own implementation of a method that is already defined in its superclass.



### 13. What is the difference between `String`, `StringBuilder`, and `StringBuffer`?
- **String**: Immutable, i.e., its value cannot be changed once created.
- **StringBuilder**: Mutable, used for single-threaded environments.
- **StringBuffer**: Mutable, used for multi-threaded environments, synchronized for thread safety.



### 14. What is a constructor in Java?
A **constructor** is a special method used to initialize objects. It has the same name as the class and is called when an object of that class is created.



### 15. What is the difference between `ArrayList` and `LinkedList`?
- **ArrayList**: It is based on a dynamic array. It allows fast access (O(1)) but slower insertions/deletions (O(n)) at the beginning/middle.
- **LinkedList**: It is based on a doubly-linked list. It allows fast insertions/deletions (O(1)) but slower access (O(n)).



### 16. What is the purpose of the `super` keyword in Java?
The `super` keyword is used to refer to the superclass of the current object. It is used to:
- Access superclass methods.
- Access superclass constructors.
- Access superclass fields.



### 17. What are `try-catch` blocks in Java?
The `try-catch` block is used for handling exceptions. The code that might throw an exception is placed in the `try` block, and the code to handle the exception is placed in the `catch` block.



### 18. What is a `finally` block in Java?
The `finally` block is used for code that must execute after the `try-catch` blocks, regardless of whether an exception was thrown or not. It is commonly used for resource cleanup (like closing file streams).



### 19. What is an exception in Java? What are the types of exceptions?
An **exception** is an event that disrupts the normal flow of the program. Exceptions in Java are categorized into two types:
- **Checked exceptions**: These are exceptions that are checked at compile-time, e.g., `IOException`.
- **Unchecked exceptions**: These are exceptions that are not checked at compile-time, e.g., `NullPointerException`, `ArithmeticException`.



### 20. What is the difference between `throw` and `throws` in Java?
- **`throw`** is used to explicitly throw an exception.
- **`throws`** is used in a method signature to declare that the method might throw an exception.



### 21. What is the use of `this` keyword in Java?
The `this` keyword refers to the current instance of the class. It is used to distinguish between instance variables and local variables with the same name and to call the current object’s methods.



### 22. What is a `lambda` expression in Java?
A **lambda expression** is a concise way to express instances of single-method interfaces (functional interfaces). It provides a clear and compact syntax for writing anonymous methods (or functions).



### 23. What is the difference between `HashMap` and `TreeMap`?
- **HashMap**: It stores key-value pairs and provides constant-time performance (O(1)) for get and put operations. It does not maintain any order of keys.
- **TreeMap**: It stores key-value pairs in a sorted order based on the natural ordering of keys or a custom comparator.



### 24. What is the use of `synchronized` keyword in Java?
The `synchronized` keyword ensures that a method or block of code is accessed by only one thread at a time, providing thread safety.



### 25. What are the different access modifiers in Java?
Java has four access modifiers:
- **`public`**: Accessible from anywhere.
- **`private`**: Accessible only within the same class.
- **`protected`**: Accessible within the same package and by subclasses.
- **`default`**: Accessible only within the same package.



### 26. What is the difference between `final`, `finally`, and `finalize` in Java?
- **`final`**: Used to declare constants, prevent method overriding, and prevent class inheritance.
- **`finally`**: Block that executes after `try-catch`, regardless of exception occurrence.
- **`finalize`**: A method called by the garbage collector before an object is destroyed.



### 27. What is the difference between `==` and `equals()` for `String` comparison in Java?
- `==` checks if two references point to the same object in memory.
- `equals()` compares the actual contents of two `String` objects.



### 28. What is the role of `Garbage Collection` in Java?
Garbage collection in Java is the process of automatically reclaiming memory by removing objects that are no longer reachable or in use.



### 29. What is a `HashSet` in Java?
A **HashSet** is a collection class that implements the **Set** interface. It does not allow duplicate elements and does not maintain any order.



### 30. What is a `LinkedHashSet` in Java?
A **LinkedHashSet** is a collection class that implements the **Set** interface, like `HashSet`, but it maintains the insertion order of the elements.



### 31. What is the difference between `Iterator` and `ListIterator`?
- **Iterator**: Used to iterate over any collection (Set, List, etc.) but allows only forward traversal.
- **ListIterator**: Used to iterate specifically over lists and allows both forward and backward traversal.



### 32. What is the `transient` keyword in Java?
The `transient` keyword prevents a field from being serialized. If an object is being serialized and contains a transient field, that field will not be included in the serialization.



### 33. What is the `volatile` keyword in Java?
The `volatile` keyword ensures that a variable’s value is always read from and written to the main memory, rather than being cached locally by threads.



### 34. What is the difference between `StringBuilder` and `StringBuffer`?
- **StringBuilder**: Not synchronized, faster in single-threaded environments.
- **StringBuffer**: Synchronized, slower but thread-safe.



### 35. What are `default` methods in interfaces (Java 8)?
Java 8 introduced **default methods** in interfaces, allowing you to define concrete methods in interfaces with the `default` keyword. This helps maintain backward compatibility when interfaces are extended.



### 36. What is the difference between `Collection` and `Collections`?
- **Collection**: It is a root interface in the Java Collections Framework.
- **Collections**: It is a utility class that provides static methods to operate on or return collections (e.g., sorting, shuffling).



### 37. What are `Streams` in Java 8?
Streams in Java 8 represent a sequence of elements supporting sequential and parallel aggregate operations. They allow functional-style programming for processing collections of objects.



### 38. What is the difference between `ArrayList` and `Vector` in Java?
- **ArrayList**: It is not synchronized and is generally faster.
- **Vector**: It is synchronized and thus thread-safe but slower than `ArrayList`.



### 39. What are `Optional` and its use in Java 8?
`Optional` is a container object that may or may not contain a value. It is used to avoid `NullPointerException` and provides methods to safely handle the absence of a value.



### 40. What is `java.nio`?
`java.nio` (New I/O) is a package introduced in Java 1.4 that provides a more efficient way to handle I/O operations, including support for non-blocking I/O, buffers, channels, and selectors.



### 41. What is the `Comparator` interface?
`Comparator` is an interface used for defining custom sorting logic. It is used in methods like `Collections.sort()` to compare objects of a class.



### 42. What is the `Comparable` interface?
`Comparable` is an interface used to define the natural ordering of objects of a class. It has a single method `compareTo()` that is used for sorting objects.



### 43. What is the `Proxy` class in Java?
The **Proxy** class in Java provides a way to create dynamic proxy instances that implement one or more interfaces at runtime.



### 44. What are `default` and `static` methods in interfaces (Java 8)?
- **default** methods allow interfaces to have concrete methods with a default implementation.
- **static** methods allow interfaces to have static methods with an implementation.



### 45. What is `String.intern()` in Java?
The `intern()` method in the `String` class ensures that if a string with the same value already exists in the string pool, the reference to that string is returned.



### 46. What is `ThreadLocal` in Java?
`ThreadLocal` is a class that provides thread-local variables. Each thread accessing a `ThreadLocal` variable has its own independent copy of the variable.



### 47. What is `java.util.function` package in Java 8?
The **`java.util.function`** package contains functional interfaces that are used for lambdas and method references. Examples include `Function`, `Predicate`, `Consumer`, and `Supplier`.



### 48. What are the advantages of using `Stream` in Java?
- **Concise and readable**: You can express complex operations on collections in a declarative way.
- **Lazy evaluation**: Operations are only performed when a terminal operation is executed.
- **Parallelism**: Streams support parallel operations to speed up computations.



### 49. What is `ForkJoinPool` in Java?
`ForkJoinPool` is a framework that is used to implement parallelism in a divide-and-conquer approach. It splits tasks into smaller ones and processes them in parallel.



### 50. What is `CopyOnWriteArrayList`?
`CopyOnWriteArrayList` is a thread-safe variant of `ArrayList`. It ensures that no modification will affect the iteration, by creating a new copy of the array when changes are made.



### 51. What is the `default` keyword used for in interfaces (Java 8)?
The `default` keyword allows interfaces to have concrete methods with default implementations. This was introduced in Java 8 to provide backward compatibility when adding methods to interfaces.



### 52. What is `@FunctionalInterface` in Java?
The `@FunctionalInterface` annotation is used to define interfaces with exactly one abstract method. These interfaces can be implemented using lambda expressions.



### 53. What is the purpose of the `this()` constructor call in Java?
The `this()` constructor call is used to call another constructor from the same class. It is often used to provide multiple constructors with different parameters.



### 54. What is the `super()` constructor call in Java?
The `super()` constructor call is used to call the constructor of the superclass. It must be the first statement in the subclass constructor.



### 55. What is the difference between `wait()` and `sleep()` in Java?
- **`wait()`**: It is used to pause the execution of the current thread and release the lock, allowing other threads to acquire the lock.
- **`sleep()`**: It pauses the current thread for a specified time but does not release the lock.



### 56. What is the role of `volatile` keyword in Java?
The `volatile` keyword ensures that a variable is directly read from and written to main memory, preventing the thread from caching it locally. It helps maintain thread safety in a multi-threaded environment.



### 57. What is the difference between `StringBuilder` and `StringBuffer` in Java?
- **StringBuilder**: Not synchronized, and thus, faster for single-threaded use cases.
- **StringBuffer**: Synchronized, making it thread-safe, but slower due to synchronization overhead.



### 58. What are the two types of memory areas in JVM?
- **Heap Memory**: Used for dynamic memory allocation of objects.
- **Stack Memory**: Used for method calls, local variables, and control flow during method execution.



### 59. What is the difference between `ArrayList` and `LinkedList` when it comes to memory usage?
- **ArrayList**: Uses a dynamic array for storage, which can lead to wasted space if the array is not full. The memory usage is contiguous.
- **LinkedList**: Uses a doubly linked list, which requires extra memory for pointers (next/previous) to other elements.



### 60. What is a `HashMap` in Java?
A **HashMap** is a collection class that stores key-value pairs, where each key is unique. It provides constant-time performance (O(1)) for basic operations like `get()` and `put()`, and does not guarantee any order of the elements.



### 61. What is the `clone()` method in Java?
The `clone()` method is used to create and return a copy of the current object. It performs a shallow copy by default, meaning it copies primitive fields but references the same objects for non-primitive fields.



### 62. What is the difference between shallow copy and deep copy?
- **Shallow copy**: Creates a new object but does not copy the objects referenced by the original object. The references are copied as they are.
- **Deep copy**: Creates a new object and recursively copies all objects referenced by the original object, ensuring independent objects.



### 63. What is the `Comparable` interface in Java?
The **Comparable** interface is used to define the natural order of objects in Java. It contains a method `compareTo()`, which compares the current object with another object of the same type.



### 64. What is `Comparator` in Java?
A **Comparator** is used to define a custom order for objects. Unlike `Comparable`, it can compare objects of different types, and it allows for multiple ways of sorting (using `compare()` method).



### 65. What is a `weak reference` in Java?
A **weak reference** in Java is a reference type that does not prevent its referent from being garbage collected. If an object is only weakly reachable, it can be collected by the garbage collector.



### 66. What is the purpose of the `interface` keyword in Java?
An **interface** is a reference type in Java, similar to a class, that can contain only constants, method signatures, default methods, static methods, and nested types. It is used to define the contract that a class must adhere to.



### 67. Can you explain `java.util.Date` class and its usage?
The **`java.util.Date`** class represents a specific point in time (i.e., date and time). It has been largely replaced by the **java.time** package (introduced in Java 8) for better date-time handling.



### 68. What are `enum` types in Java?
An **enum** in Java is a special class that represents a group of constants (unchangeable variables). Enum types are used to define variables with a limited set of possible values.



### 69. What is the `instanceof` operator in Java?
The `instanceof` operator is used to test whether an object is an instance of a particular class or interface. It returns `true` if the object is an instance of the specified type.



### 70. What is `throw` in Java?
The `throw` keyword is used to explicitly throw an exception from within a method or block of code.



### 71. What is `throws` in Java?
The `throws` keyword is used in a method signature to declare that the method might throw certain exceptions during its execution. It indicates that the caller of the method should handle or propagate the exception.



### 72. What is the purpose of the `finalize()` method in Java?
The `finalize()` method is called by the garbage collector before an object is destroyed. It can be overridden to release resources (e.g., closing a file or network connection).



### 73. What is a `ListIterator` in Java?
A **ListIterator** is an interface that allows traversal of a list in both forward and backward directions. It also provides methods to modify the list during iteration.



### 74. What are the differences between `synchronized` block and `synchronized` method?
- **Synchronized block**: Synchronizes only a portion of the method, making it more efficient when only part of the method needs synchronization.
- **Synchronized method**: Synchronizes the entire method, ensuring that only one thread can execute it at a time.



### 75. What is the purpose of `Thread.join()` in Java?
The `join()` method allows one thread to wait for the completion of another thread. When `join()` is called, the current thread pauses its execution until the thread it was called on has finished.



### 76. What is the `ExecutorService` in Java?
The **ExecutorService** is an interface in Java that provides a higher-level replacement for the traditional thread management. It manages a pool of threads and schedules tasks for execution asynchronously.



### 77. What are `Callable` and `Runnable` interfaces?
- **Runnable**: Represents a task that can be executed by a thread. It has a `run()` method.
- **Callable**: Similar to `Runnable`, but it can return a result and throw exceptions. Its method is `call()`.



### 78. What is `java.util.concurrent` package in Java?
The **`java.util.concurrent`** package provides classes and interfaces for concurrent programming, including thread pools, atomic variables, and utilities for synchronizing thread execution.



### 79. What is the purpose of `ReentrantLock` in Java?
A **ReentrantLock** is a synchronization primitive that allows threads to lock and unlock resources. It is more flexible than `synchronized` blocks, providing features like timed locks and the ability to interrupt a thread waiting for a lock.



### 80. What is a `CountDownLatch` in Java?
A **CountDownLatch** is a synchronization aid that allows one or more threads to wait until a set of operations being performed by other threads completes.



### 81. What is the difference between `ArrayList` and `Vector` in terms of synchronization?
- **ArrayList**: Not synchronized, making it faster but not thread-safe.
- **Vector**: Synchronized, making it thread-safe but slower due to synchronization overhead.



### 82. What is the difference between `String` and `StringBuilder` in Java?
- **String**: Immutable, meaning that any operation on a `String` creates a new object.
- **StringBuilder**: Mutable, meaning that it allows modification of the same object without creating new instances.



### 83. How do you handle exceptions in Java?
Exceptions in Java are handled using `try-catch` blocks. You can also use `finally` to ensure that code executes after the try-catch block, regardless of whether an exception occurred.



### 84. What is a `Stack` in Java?
A **Stack** is a data structure that follows the Last-In-First-Out (LIFO) principle. It is used to store a collection of objects where the last added object is the first one to be removed.



### 85. What is a `Queue` in Java?
A **Queue** is a data structure that follows the First-In-First-Out (FIFO) principle. It is used to store elements where the first element added is the first one to be removed.



### 86. What is a `BlockingQueue` in Java?
A **BlockingQueue** is a type of Queue that supports operations like `put()` and `take()` that block the thread when the queue is empty or full.



### 87. What is the `System.currentTimeMillis()` method used for in Java?
The **`System.currentTimeMillis()`** method returns the current time in milliseconds since January 1, 1970, 00:00:00 GMT. It is commonly used for measuring elapsed time.



### 88. What are `final`, `finally`, and `finalize` in Java?
- **`final`**: Used to define constants, prevent method overriding, and prevent class inheritance.
- **`finally`**: A block that executes after `try-catch` to clean up resources.
- **`finalize()`**: A method called by the garbage collector before an object is destroyed.



### 89. What is the role of `ClassLoader` in Java?
A **ClassLoader** in Java is responsible for loading class files into memory. It is part of the JVM and helps dynamically load classes at runtime.



### 90. What are `annotations` in Java?
Annotations in Java provide metadata about the code. They do not affect the logic of the program but are used for configuration, compile-time checks, or to provide additional information to the compiler or runtime.



### 91. What is the `@Override` annotation used for in Java?
The **`@Override`** annotation is used to indicate that a method is overriding a method from a superclass. It helps catch errors at compile-time if the method does not actually override a superclass method.



### 92. What is the `@SuppressWarnings` annotation in Java?
The **`@SuppressWarnings`** annotation is used to suppress specific compiler warnings in Java, such as unused variables or unchecked type casts.



### 93. What is a `BitSet` in Java?
A **BitSet** is a class that represents a set of bits or boolean values. It is used to efficiently store large numbers of `true`/`false` values with minimal memory usage.



### 94. What is the purpose of `UUID` in Java?
A **UUID** (Universally Unique Identifier) is used to generate unique identifiers for objects, typically used for distributed systems, databases, or sessions.



### 95. What is `Optional` in Java 8?
**Optional** is a container object used to represent the presence or absence of a value. It helps avoid `NullPointerException` by providing methods to handle values that may be `null`.



### 96. What is `java.nio.file` package used for in Java?
The **`java.nio.file`** package provides efficient file and file system operations using the **NIO** (New I/O) API, introduced in Java 7. It offers better performance and flexibility than the older `java.io` package.



### 97. What is the purpose of `Path` and `Files` classes in Java?
- **Path**: Represents the file or directory path in the file system.
- **Files**: Provides utility methods to work with files and directories, such as reading, writing, and checking file attributes.



### 98. What is a `Callable` interface in Java?
A **Callable** is similar to a `Runnable` but can return a result and throw an exception. Its method `call()` returns a value, making it more flexible than `Runnable`.



### 99. What is the use of `ForkJoinPool` in Java?
The **ForkJoinPool** is a pool of worker threads that can be used to divide and execute tasks in parallel. It is designed for tasks that can be recursively broken down into smaller sub-tasks.



### 100. What is `java.util.concurrent.locks` package in Java?
The **`java.util.concurrent.locks`** package provides lock implementations for multithreading that offer more control over synchronization than the `synchronized` keyword, such as **ReentrantLock** and **ReadWriteLock**.



