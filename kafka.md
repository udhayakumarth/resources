- Cluster
- Brokers 
- Topics
- Partitions
- Event/Message
- Producers 
- Consumers 



An event has a key, value, timestamp, and optional metadata headers.
Topics are partitioned, meaning a topic is spread over a number of "buckets" located on different Kafka brokers. 

Kafka APIs
----------
Admin API
Producer API 
Consumer API 
Kafka Streams API 
Kafka Connect API

Kafka protocol
--------
- Network
	Kafka uses a binary protocol over TCP.
- Batching
	Our APIs encourage batching small things together for efficiency.
	
	
- Write a program that can make a TCP connection to a server and maintain the connection for long time.

Design
--------
- Kafka relies heavily on the filesystem for storing and caching messages. 
- Linear reads and writes are the most predictable of all usage patterns. and are heavily optimized by the operating system. A modern operating system provides read-ahead and write-behind techniques that prefetch data in large block multiples and group smaller logical writes into large physical writes

From source code:
- Node.java
- MetadataSnapshot.java
- Metadata.java
- NetworkClient.java 
