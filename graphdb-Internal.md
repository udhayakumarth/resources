Graph DB Internal
-----------------
#### Entity:
An Entity is a Entity that is persisted in the database, and identified by an getElementId()
Nodes and Relationships are Entities. Entities are attached to transaction in which they were accessed. 

#### Node:
A node in the graph with properties and relationships to other entities.

#### Relationship:
A relationship between two nodes in the graph. A relationship has a start node, an end node and a type.

#### Transaction:
A programmatically handled transaction.
All database operations that access the graph, indexes, or the schema must be performed in a transaction.
If you attempt to access the graph outside of a transaction, those operations will throw NotInTransactionException.

#### Path:
Represents a path in the graph. 
A path starts with a node followed by pairs of Relationship and Node objects. 
The shortest path is of length 0. Such a path contains only one node and no relationships. 
During a traversal Path instances are emitted where the current position of the traverser is represented by each such path. 
The current node in such a traversal is reached via endNode().

#### Result:
#### Label:
#### Lock:

#### GraphDatabaseService:
GraphDatabaseService represents a graph database and is used to create new transactions with beginTx().
