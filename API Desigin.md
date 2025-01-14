## Web API Desigin Best practices 
### Status 201

For example, the 201 Created status code should always be paired 
with a Location header that provides the URL of the newly-created resource.

```
HTTP/1.1 201 Created 
Location: https://dogtracker.com/dogs/1234567
```

### Status 200
the response to a successful 
GET is not just a 200 status code and some data, it includes a standard package of headers, like this:
Note: Content-Location is an optional header that servers often include only if the ‘canonical’ URL of the 
resource is different from the one that was used in the GET request. We think it makes sense to always include 
this header.

```
HTTP/1.1 200 OK 
Content-Location: https://dogtracker.com/dogs/1234567 
Content-Type: application/json 
ETag: 1437080173827 
Content-Length: nnnn 
// body goes here /
```

### Status 405
the 405 error code indicating that the client tried to use a method that the server 
does not support for the given resource must be paired with an Allow header saying which methods are 
supported for the resource.
```
HTTP/1.1 405 Method Not Allowed 
Allow: GET, DELETE, PATCH
```

### PATCH rather than PUT for updating
Another thing you can do is to use PATCH rather than PUT for updating. The semantics of PUT are that it 
completely replaces the state of the resource. This means that clients have to include all the properties of 
any resource they are updating, even properties that didn’t exist at the time the client was written. This 
puts a burden on clients and makes the server itself vulnerable to client errors. PATCH, on the other hand, 
only changes the data explicitly referenced by the client. The server takes responsibility for the merge, 
which is safer9. Of course, you should never implement a PUT operation that has PATCH semantics


----------
### Include Links
A change in recent years has been the realization that the use of links brings a significant 
improvement to the usability and learnability of all APIs, not just those that are designed to be consumed 
by completely general-purpose clients
Reprising the example introduced in the Foreword, assume that there is a relationship between a dog and 
its owner. A popular way to represent relationship information in JSON looks like the following:

```
{
  "id": "12345678",
  "name": "Lassie",
  "furColor": "brown",
  "ownerID": "98765432"
}

```
The ownerID field expresses the relationship. A better way to express relationships is to use links. If your 
web APIs do not include links today, a first step is simply to add some links without making other changes, 
like this:
```
{
  "id": "12345678",
  "kind": "Dog",
  "name": "Lassie",
  "furColor": "brown",
  "ownerID": "98765432",
  "ownerLink": "https://dogtracker.com/persons/98765432"
}

```

### Include self-reference and kind properties
Including a `self` property makes it explicit what web resource’s properties we are talking about 
without requiring contextual knowledge—like what URL did you perform a GET on to retrieve this 
representation—or application-specific knowledge.

Including a `kind` property helps clients recognize whether or not this is an object they know how to 
process.


### How should I represent collections?
```
{
  "self": "https://dogtracker.com/dogs",
  "kind": "Collection",
  "contents": [
    {
      "self": "https://dogtracker.com/dogs/12344",
      "kind": "Dog",
      "name": "Fido",
      "furColor": "white"
    },
    {
      "self": "https://dogtracker.com/dogs/12345",
      "kind": "Dog",
      "name": "Rover",
      "furColor": "brown"
    }
  ]
}


```

### Paginated collections
 It is not a good idea for either the client or the server to try to return very large 
collections, so what we would expect to happen is that the collection would be paginated. Here is an 
HTTP message exchange that illustrates.

Request:
```
GET /dogs HTTP/1.1 
Host: dogtracker.com 
Accept: application/json
```

Response:
```
HTTP/1.1 303 See Other 
Location: https://dogtracker.com/dogs?limit=25,offset=0
```

Request:
```
GET /dogs?limit=25,offset=0 HTTP/1.1 
Host: dogtracker.com 
Accept: application/json
```

Response:
```
HTTP/1.1 200 OK 
Content-Type: application/json 
Content-Location: https://dogtracker.com/dogs?limit=25,offset=0 
Content-Length: 23456
{
  "self": "https://dogtracker.com/dogs?limit=25&offset=0",
  "kind": "Page",
  "pageOf": "https://dogtracker.com/dogs",
  "next": "https://dogtracker.com/dogs?limit=25&offset=25",
  "contents": [
    {
      "self": "https://dogtracker.com/dogs/12344",
      "kind": "Dog",
      "name": "Fido",
      "furColor": "white"
    },
    {
      "self": "https://dogtracker.com/dogs/12345",
      "kind": "Dog",
      "name": "Rover",
      "furColor": "brown"
    }
    // Add the other 23 dog objects here
  ]
}

```

The client followed the redirect, which returned the first page. The first page contains a subset of the collection 
contents, references the original collection in the `pageOf` property, and also references the subsequent 
page in the `next` property (unless there is no next page). There is also a `previous` property that is missing 
in this case because there is no page before the first one.

### What about property names?
You have an object with data attributes on it. How should you name the attributes?
Here are API responses from a few leading APIs:
Twitter:
```
"created_at": "Thu Nov 03 05:19;38 +0000 2011"
```
Bing:
```
"DateTime": "2011-10-29T09:35:00Z"
```
Foursquare:
```
"createdAt": 1475795458
```
Arguments over whether snake_case (Twitter) or camelCase (Foursquare) is better have raged for 
decades (there has even been some scientific research to see which works better). The science is 
inconclusive, and opinions vary, so pick the one that pleases your customers better. JavaScript, Java, 
and Objective-C programmers tend to favor camelCase, while Python and Ruby programmers tend to 
favor snake_case, with PHP being split by sub-communities.
