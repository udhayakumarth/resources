### 1. Serialization and Deserialization
- **Serialization** is a mechanism of converting the state of an object into a byte stream.
- **Deserialization** is the reverse process where the byte stream is used to recreate the actual Java object in memory. This mechanism is used to persist the object.

### 2. Authentication and Authorization

- **Authentication**:
  - Authentication is the process of verifying the identity of a user or entity. In web applications, users typically provide credentials (such as username/password) to prove their identity.
  
- **Authorization**:
  - Authorization is the process of determining whether an authenticated user has permission to access a particular resource or perform a specific action within the application.

### 3. JAVA 8 Features

- Lambda Expression
- Method Reference
- Functional Interface
- Stream API
- Default Method in Interface

### 4. What is Lambda Expression?

- Lambda expression helps us to write our code in functional style.
- It provides a clear and concise way to implement SAM (Single Abstract Method) interface using an expression.
- It is very useful in the collection library, where it helps to iterate, filter, and extract data.
  
**Syntax**:  
```java
(parameter) -> expression
```

### 5. Method Reference
Java 8 Method Reference is used to refer to a method of a functional interface.
It is a compact and easy form of lambda expression.
Each time when you are using a lambda expression to just refer to a method, you can replace the lambda expression with method reference.

**Types of Method References**:
1. Static Method Reference
2. Instance Method Reference of a particular object
3. Instance Method Reference of an arbitrary object of a particular type
4. Constructor Reference

### 6. Functional Interface
- An Interface that contains only one abstract method is known as a functional interface.
- It can have any number of default and static methods.
- It can also declare methods of the Object class.
**Common Functional Interfaces**:
- Consumer: Represents an operation that accepts a single input argument and returns no result.
- Supplier: Represents a supplier of results. It doesn't take any arguments but produces a result of a given type.
- Predicate: Represents a predicate (boolean-valued function) of one argument.
- Function: Represents a function that takes an argument and returns a result.

### 7. Define Streams
- Stream API is introduced in Java 8 and is used to process collections of objects with a functional style of coding using the lambda expression.

**Three types of operations that are carried over streams**:
1. Intermediate Operations
2. Terminal Operations
3. Short-circuit Operations

**Intermediate Operations**:
- Intermediate operations transform a stream into another stream.
- Common intermediate operations include:
  - `filter()`: Filters elements based on a specified condition.
  - `map()`: Transforms each element in a stream to another value.
  - `sorted()`: Sorts the elements of a stream.

**Terminal Operations**:
- Terminal operations are the operations that, on execution, return a final result as an absolute value.
  - `collect()`: It is used to return the result of the intermediate operations performed on the stream.
  - `forEach()`: It iterates all the elements in a stream.
  - `reduce()`: It is used to reduce the elements of a stream to a single value.
  - `count()`, `match()`

**Short-circuit Operations**:
- Short-circuit operations provide performance benefits by avoiding unnecessary computations when the desired result can be obtained early. They are particularly useful when working with large or infinite streams.
  - `anyMatch()`: It checks if the stream satisfies the given condition.
  - `findFirst()`: It checks the element that matches a given condition and stops processing when it finds it.
 
### 8. Default Methods

- Java provides a facility to create default methods inside the interface.
- Methods defined inside the interface and tagged with the `default` keyword are known as default methods.
- These methods are non-abstract and can have a method body.

### 9. Difference Between Collection and Stream

- **Collections** are used to store and manage data.
- **Streams** are used to process data in a functional style, enabling concise and expressive code for operations like filtering, mapping, and reducing.

### 10. String and String Pool

- The **String Pool** is a storage area in the Java heap where string literals are stored.
- By default, the string pool is empty and is privately maintained by the Java String class.
- When a string literal is created, the JVM first checks the pool to see if the literal is already present. If it is, it returns a reference to the pooled instance; if not, a new string object is placed in the pool.

### 11. JSP Elements

- **Scriptlets (`<% ... %>`)**: Scriptlets are used to embed Java code within the JSP page.
- **Directives (`<%@ ... %>`)**: Directives give special instructions to the JSP container during the translation phase. There are three types of directives:
  - `page`: Defines page-level attributes such as language, error handling, session handling, etc.
  - `include`: Includes a file (JSP or HTML) in the current JSP page during translation.
  - `taglib`: Declares that the JSP page uses custom tag libraries.
- **Declarations (`<%! ... %>`)**: Declarations declare variables and methods that are available to the entire JSP page.
- **Expressions (`<%= ... %>`)**: Expressions embed Java expressions or variables directly into the HTML output.
- **Comments (`<%-- ... --%>`)**: Comments in JSP are similar to HTML comments but can be used anywhere within the JSP file.

### 12. How the Servlet Lifecycle Works?

- **init()**, **service()**, **destroy()** methods:
  - When a request is made to the servlet for the first time, the container loads the servlet class and creates an instance of it.
  - **Initialization**: The container initializes the servlet by calling its `init()` method.
  - **Servicing Requests**: The `service()` method is called for each request, and the appropriate method (`doGet()`, `doPost()`) is invoked.
  - **Destroying**: When the servlet is no longer needed, the container calls the `destroy()` method to clean up resources.

### 13. Difference Between JDBC and Hibernate

- **JDBC** is a lower-level API that requires developers to write SQL queries and handle database operations manually.
- **Hibernate** is a higher-level ORM framework that simplifies database interaction by mapping Java objects to database tables and providing automatic CRUD operations.

### 14. What are the Layers in Struts?

- In the Struts framework, the typical application architecture follows the Model-View-Controller (MVC) pattern.
  - **Model**: Handles the business logic and data.
  - **View**: Handles the presentation logic.
  - **Controller**: Manages the flow of the application.
  - **Struts Configuration Layer**: Provides the necessary configuration to tie everything together.

### 15. Difference Between Map and Filter in Stream API

- **Map**: Used to transform each element in the stream into another object.
- **Filter**: Used to select elements based on a condition.

### 16. Platform Independent

- **Java** is platform-independent because it is compiled into bytecode, which can be run on any device that has a Java Virtual Machine (JVM).

### 17. JVM

- **JVM** stands for **Java Virtual Machine**.
- It is a Java interpreter responsible for loading, verifying, and executing the bytecode created in Java.

### 18. JRE

- **JRE** stands for **Java Runtime Environment**.
- It is a set of software tools used for developing Java applications.
- It contains libraries and other files that the JVM uses at runtime and provides an environment to run Java programs.

### 19. JDK

- **JDK** stands for **Java Development Kit**.
- It is a software development environment used to develop Java applications and applets.
- It contains the JRE and development tools.

### 20. JIT

- **JIT** stands for **Just In Time Compiler**.
- It is a part of the JVM that is responsible for compiling bytecode into native machine code at runtime.

### 21. Garbage Collector (GC)

- The **Garbage Collector (GC)** is a part of the JVM responsible for automatically managing memory by deallocating memory for objects that are no longer needed.

### 22. What is a Classloader?

- The **Classloader** is a part of the JRE responsible for dynamically loading Java classes and interfaces into the JVM during runtime.
- It allows Java to load classes and files without knowing about files and file systems.

### 22. Data Types in Java

**Primitive Data Type**

Primitive data types are single values with no special capabilities. There are 8 primitive data types:
- **boolean**: stores value true or false
- **byte**: stores an 8-bit signed two’s complement integer
- **char**: stores a single 16-bit Unicode character
- **short**: stores a 16-bit signed two’s complement integer
- **int**: stores a 32-bit signed two’s complement integer
- **long**: stores a 64-bit two’s complement integer
- **float**: stores a single-precision 32-bit IEEE 754 floating-point
- **double**: stores a double-precision 64-bit IEEE 754 floating-point

**Non-Primitive Data Type or Object Data Type**

Non-primitive data types are objects, arrays, or instances of classes. They store references to data and have more complex behaviors.


### 23. Wrapper Class

The wrapper class is an object class that provides the way to use primitive data types as objects.
- Wrapper classes are final and immutable.
- They provide autoboxing and unboxing.
- They provide methods for performing operations.

Wrapper classes for primitive types:
- Integer
- Byte
- Boolean
- Double


### 24. Singleton Class

A Singleton class in Java allows only one instance of itself to be created and provides a global point of access to that instance.

Example:

```java
public class Singleton {
    private static Singleton instance;

    // Private constructor to prevent instantiation from outside the class
    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

### 25. Static and Final
- **Static**: If a variable is declared as static, it is shared among all instances of the class, and only one copy of the variable is created.
- **Final**: A final variable can be assigned a value only once. Once initialized, it cannot be changed.


### 26. OOPS (Object-Oriented Programming)
Object-Oriented Programming is a methodology or paradigm for designing a program using classes and objects. The four main pillars of OOPS are:

1. Inheritance
2. Polymorphism
3. Abstraction
4. Encapsulation


### 27. Inheritance
Inheritance is a mechanism where a new class inherits the properties and behaviors of an existing class. It creates a parent-child relationship, allowing the child class to access methods and properties of the parent class. It is mainly used for code reusability.

Types of inheritance:
1. Single inheritance
2. Multi-level inheritance
3. Multiple inheritance
4. Hierarchical inheritance


### 28. Encapsulation
Encapsulation is the mechanism of wrapping data (variables) and code (methods) together as a single unit. It hides sensitive data from users by declaring the variables as private and providing access to those variables via getter and setter methods.


### 29. Polymorphism
Polymorphism in Java is a concept where a single action can be performed in different ways. It includes:
1. **Compile-time polymorphism** (method overloading)
2. **Run-time polymorphism** (method overriding)


### 30. Abstraction
Data abstraction is the process of hiding certain details and showing only essential information to the user. You cannot create an object of an abstract class.

Example:

```java
// Abstract class
abstract class Animal {
    // Abstract method (does not have a body)
    public abstract void animalSound();

    // Regular method
    public void sleep() {
        System.out.println("Zzz");
    }
}

// Subclass (inherit from Animal)
class Pig extends Animal {
    public void animalSound() {
        System.out.println("The pig says: wee wee");
    }
}

class Main {
    public static void main(String[] args) {
        Pig myPig = new Pig(); // Create a Pig object
        myPig.animalSound();
        myPig.sleep();
    }
}
```

### 31. Access Modifiers in Java
- **private**: Accessible only within the class.
- **protected**: Accessible within the class and its subclasses.
- **public**: Accessible by all classes.
- **default**: Accessible within the class and the package. No access modifier is specified.


### 32. Difference Between Collection and Collections
- **Collection**: An interface that provides the foundational structure for various types of collections (e.g., List, Set, Queue). It defines methods that all collections must implement.
- **Collections**: A utility class with static methods to manipulate and interact with collections. Provides functionalities like sorting, searching, and synchronizing collections.


### 33. Difference Between ArrayList and LinkedList

- **ArrayList**:
    - Uses a dynamic array to store elements.
    - Maintains insertion order.
    - Accepts duplicates and null values.
    - Manipulation is slower due to array resizing when elements are removed.
    - Mainly used for storing and accessing elements.

- **LinkedList**:
    - Uses a doubly linked list to store elements.
    - Maintains insertion order.
    - Accepts duplicates and null values.
    - Manipulation is faster as no shifting is required when elements are removed.
    - Mainly used for manipulating data.


### 34. Difference Between HashMap and TreeMap

- **HashMap**:
    - Contains values based on the key.
    - Contains only unique keys.
    - May have one null key and multiple null values.
    - Is non-synchronized.
    - Maintains no order.

- **LinkedHashMap**:
    - Contains values based on the key.
    - Contains unique keys.
    - May have one null key and multiple null values.
    - Is non-synchronized.
    - Maintains insertion order.

- **TreeMap**:
    - Contains values based on the key and implements the NavigableMap interface.
    - Contains unique keys.
    - Cannot have a null key, but can have multiple null values.
    - Is non-synchronized.
    - Maintains ascending order.

- **Hashtable**:
    - Contains values based on the key.
    - Does not allow null key or value.
    - Is synchronized.


### 35. Stack Memory and Heap Memory

- **Stack Memory**:
    - Used for the execution of a thread.
    - Stores local variables, method call information, and reference variables (not the objects themselves).
    - Each thread has its own stack.

- **Heap Memory**:
    - Used for dynamic memory allocation.
    - Stores objects and instances of classes.
    - Shared among all threads.
    - Managed by the garbage collector for dynamic memory management.


### 36. Comparable and Comparator Interface

- **Comparable**: Defines the natural order of objects by implementing the `compareTo()` method.

Example:

```java
class Employee implements Comparable<Employee> {
    private int id;
    private String name;

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public int compareTo(Employee other) {
        return this.id - other.id; // Sorting by id
    }

    // Getters and setters
}
```
Comparator: Defines custom ordering of objects by implementing the `compare()` method

```
class EmployeeNameComparator implements Comparator<Employee> {
    @Override
    public int compare(Employee e1, Employee e2) {
        return e1.getName().compareTo(e2.getName()); // Sorting by name
    }
}
```
