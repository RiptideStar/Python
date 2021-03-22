# Shorten URL with Python

## Basic Concepts

We use this project to strengthen our understanding of these concepts:

1. What is API
2. What is WEB API
3. What is REST API
4. Why API is important? 
5. What is HTTP? What are the main methods? 
6. Relationship of HTTP & REST API? 
7. What is IP address? and DNS?
8. What is HTTP call headers, query parameters, payload (body)?
9. What is cookie ? 
10. What is html, xml, and json?

## Key Points:

* The programming interface ([API](API.png)) has penetrated into every corner of your life like air and water. For example, all apps on your mobile phone, like Youtube, communicate with the server through APIs.
* Each URL is actually a REST API. REST API is the most common and most widely used [WEB API](http.jpeg).
* Every web page browse is an [HTTP request](CRUD_diagram.png). Every HTTP request calls a REST API.
* Leaving the WEB API, you can’t make any progress: You can’t shop online, you can’t transfer money online, you can’t watch Youtube videos, you can’t take a Uber/Grubhub...

These are some important concepts that this project will involve. In fact, you use these things every day. You just don’t notice that they are happening around you all the time. After understanding these concepts, you will clearly know what happens behind scene every time you browse the web or operate the mobile App.
- Not only knowing what, but also knowing why.

## Project background and use case scenarios
1. Everyone may have encountered: The URL to be shared is very long and it is inconvenient to put on social media (Youtube, Twitter).
2. Some programs or websites need to provide services to shorten URLs, such as Twitter, which cannot exceed 140 characters.

For example: You have such a URL: too long, hard to remember, hard to share
https://docs.google.com/document/d/e/2PACX-1vSGOa_JPD28lJBVwxM7eaoXVJz-wkGsYXiiTe7rnnxCRs6SJwMdqaOeYLup9W-6nmG6y7jb6_BehI4K/pub

You definitely want to shorten it to a memorable URL
You have two approaches:
1. Go to the website that provides the service, manually enter your website address, and then let this website shorten your website address for you.
2. Call the API provided by the service website, and realize it by your own programming method.
   
If you need to process a lot or get this service in a program, then programming to achieve it is your only choice.


## Call the third-party WEB API to shorten the URL service

A search reveals that there are many websites that provide such services. Let's discuss two more common websites together today -
1. cutt.ly
2. bit.ly

### Cutt.ly website and API

1. Registration
2. Check the API documentation: https://cutt.ly/api-documentation/cuttly-links-api
3. API Key: 123456789123456789123456789 (fake key! replace this API key with your own, find yours in your profile in cuttly)
4. Python is divided into four steps:
   1. Get parameters
   2. Construct REST API URL: `--- api_url: https://cutt.ly/api/api.php?key=123456789123456789123456789&short=https://docs.google.com/document/d/e/2PACX-1vSGOa_JPD28lJBVwxM7eaoXVJz-wkGsYXiiTe7rnnxCRs6SJwMdqaOeYLup9W-6nmG6y7jb6_BehI4K/pub&name=pythonWEB`
   3. Call REST API (GET) shorten URL
   4. Analyze the return value
   
Example:
```
python3 ex1-cutt.ly.py https://docs.google.com/document/d/e/2PACX-1vSGOa_JPD28lJBVwxM7eaoXVJz-wkGsYXiiTe7rnnxCRs6SJwMdqaOeYLup9W-6nmG6y7jb6_BehI4K/pub pythonShort

--- Command Line: ['ex1-cutt.ly.py', 'https://docs.google.com/document/d/e/2PACX-1vSGOa_JPD28lJBVwxM7eaoXVJz-wkGsYXiiTe7rnnxCRs6SJwMdqaOeYLup9W-6nmG6y7jb6_BehI4K/pub', 'pythonShort']

--- api_url:  https://cutt.ly/api/api.php?key=123456789123456789123456789&short=https://docs.google.com/document/d/e/2PACX-1vSGOa_JPD28lJBVwxM7eaoXVJz-wkGsYXiiTe7rnnxCRs6SJwMdqaOeYLup9W-6nmG6y7jb6_BehI4K/pub&name=pythonShort

--- data:  {'status': 7, 'fullLink': 'https://docs.google.com/document/d/e/2PACX-1vSGOa_JPD28lJBVwxM7eaoXVJz-wkGsYXiiTe7rnnxCRs6SJwMdqaOeYLup9W-6nmG6y7jb6_BehI4K/pub', 'date': '2021-03-22', 'shortLink': 'https://cutt.ly/pythonShort', 'title': 'Python Web Crawler'}

--- Shortened URL: https://cutt.ly/pythonShort
```
