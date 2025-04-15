### Programming Paradigms
---------------------
- Object-Oriented Programming - Java, Python 
- Functional Programming - JavaScript
- Event-Driven Programming - JavaScript, Python (Asyncio), Java (Spring Event Handling), Go (goroutines)
- Concurrent/Parallel Programming - Go (with goroutines), Java, Python (with threading)

### Programing Concepts
-------------------
- Hash Table
- Greedy
- Binary Search
- Matrix
- Tree
- Breadth-First Search
- Heap (Priority Queue)
- Prefix Sum
- Simulation
- Graph
- Sliding Window
- Backtracking
- Enumeration
- Number Theory
- Monotonic Stack
- Segment Tree
- Trie
- Bitmask
- Divide and Conquer
- Combinatorics
- Queue
- Recursion
- Binary Indexed Tree
- Geometry
- Binary Search Tree
- Hash Function
- Bit Manipulation
- Two Pointers
- Stack

### Data
----
- SQL - MySQL
- NoSQL - MongoDB
- GraphSQL - Neo4j
- LDAP - Microsoft Active Directory
- Redis

### Java
----
- Logger
- Exception
- Validation
- JUnit
- Multithreading
- OOP
- Stream
- Collections

Go
--

JavaScript
----------

Python
------

Shell Script
------------



### Digital Resume
---------------
QR to Resume Link
Resume Page







- HTTP Methods - GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
- HTTP Headers - Caching Headers (Cache-Control, Expires, ETag, Request Headers (User-Agent, Accept, Content-Type, etc.), Response Headers (Location, Set-Cookie, Content-Length, etc.)
- Cookies & Sessions - Setting and reading cookies
- HTTPS and SSL/TLS
- URL Encoding - URL encoding/decoding (UTF-8, percent-encoding)
- Query Parameters - Structure of a URL (Scheme, Host, Path, Query, Fragment)
- Cross-Origin Resource Sharing
- Content-Type and MIME Types
- WebSockets 
- Optimization - HTTP Keep-Alive, GZIP compression, Browser caching strategies
- Proxy Servers
- Load Balancers
- HTTP/3 and QUIC - QUIC protocol for faster web connections
- Authentication and Authorization - Basic Authentication, Bearer Tokens, OAuth, HTTP Authentication headers (Authorization, WWW-Authenticate)


How DI and IoC Work Together in Spring Boot:
Spring Context Initialization: When Spring Boot starts, it initializes the ApplicationContext (IoC container), scanning the classpath for annotated beans (e.g., @Service, @Component, etc.).

Bean Creation: The ApplicationContext creates instances of all beans it finds during its scan. For example, it creates instances of Engine, CarService, etc., and manages their lifecycles.

Dependency Injection: When a bean, like CarService, needs a dependency, such as Engine, Spring will inject the Engine instance into the CarService bean. This can happen through constructor injection, setter injection, or field injection.

Bean Usage: After all the beans are created and dependencies injected, Spring makes them available for use. For instance, when the CarService is used in your application, it will automatically have its dependencies (like Engine) injected and be ready to perform its tasks.

![image](https://github.com/user-attachments/assets/9943af9f-ecc9-4eb9-a169-e7d2c6eadf95)


For DevOps:
1. Cloud
	- AWS
2. CI/CD
	- CircleCI
	- GitLab CI
	- Jenkins
3. Containers
	- Docker
4. Container Orchestration
	- Kubernetes
5. Monitoring
	- Prometheus
	- Grafana

For SOC:
1. SIEM
2. SOAR
3. EDR
4. Firewalls & Next-Generation Firewalls
5. IAM(for IAM jobs)
