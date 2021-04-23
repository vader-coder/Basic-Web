BasicServerlet extracts data from requests, converts it to a data structure, 
and passes it to a function in ResponseHandler. <br/>
The idea is to call whatever functions you want inside ResponseHandler to generate a response. <br/>
The point behind doing it this way is to separate the basic web api from the application logic or the math. <br/>
Ex. For a dictionary, the serverlet may receive a request containing a word. The ResponseHandler will access a dictionary app for the definition and the serverlet will return it. </br>
For a math related application, it may pass in a string representing a question. ResponseHandler will call another program to compute the answer, which the serverlet will return. </br>
This package means we won't have to rewrite the basic server code every single time.  