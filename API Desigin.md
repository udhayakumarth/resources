## Web API Desigin Best practices 
### Status 201

For example, the 201 Created status code should always be paired 
with a Location header that provides the URL of the newly-created resource.

```
HTTP/1.1 201 Created 
Location: https://dogtracker.com/dogs/1234567
```
****
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
****
### Status 405
the 405 error code indicating that the client tried to use a method that the server 
does not support for the given resource must be paired with an Allow header saying which methods are 
supported for the resource.
```
HTTP/1.1 405 Method Not Allowed 
Allow: GET, DELETE, PATCH
```
