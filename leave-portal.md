API Desigin
-----------
Participents: Employee

Activities: user register, user login, Apply Leave, View Applied Leave

User
-----
- `createUser()`
- `loginUser()`

Leave
-----
- `applyLeave()`
- `viewLeave()`

Resources
------------
`POST` - /api/users - to create user

`GET` - /api/users/{id} - to get user 

`POST` - /api/auth - to authenticate user

`POST` - /api/leave - to create leave request

`GET` - /api/leave - to get all leaves

`GET` - /api/leave/{id} - to get details of a leave
