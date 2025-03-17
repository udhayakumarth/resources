users table
-----------
id
name
number
bio
image
isOnline
lastSeen
status
createdAt
updatedAt


groups table
------------
id
name
bio
image
isAdminMessagesOnly
status
createdBy
createdAt
updatedAt


group_members table
-------------------
id
groupId
userId
isAdmin
status
createdAt
updatedAt


blocked table
-----------
id
userId
blockedId
status
createdAt
updatedAt








### Deleted
messages table
--------------
id
sender
receiver
content
contentType
status
createdAt
updatedAt


group_messages table
--------------------
id
sender
groupId
content
contentType
status
createdAt
updatedAt



#𝑠𝑒𝑟𝑣𝑒𝑟𝑠 𝑖𝑛 𝑐ℎ𝑎𝑡 𝑚𝑖𝑐𝑟𝑜𝑠𝑒𝑟𝑣𝑖𝑐𝑒= (#chat messages per second∗ Latency)/ #concurrent connections per server






