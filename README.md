API Call for the movies.


Before run this application you should set up neccessery information:

The information which you need to provide is the API Token whcih you can get it from the url: http://www.omdbapi.com/apikey.aspx

the key you need to past in to the variable api_token you can find it in the top of the file 

```
#!/usr/bin/env python3

import os
import json;
import requests

api_token = 'api_token_key'
```

You can set this up as a container see below steps:

##########################################################################
pre-requisity:
1. Install docer and docker-engine (See below)
How to install it you can find in the documentation (See link below):

https://docs.docker.com/engine/install/ubuntu/

2. Modify The execution for this application/script via command:

sudo chmod +x <path_to_file>/api_book_call.py
##########################################################################


Build the image and Start the container

1. Go to the application path:
2. Run the command: 
```docker image build -t api_book_call . ```
3 Run the app:
```docker run -it api_book_call```


##########################################################################
Run the script as a normal script not the container.

1. Set up python3.7 or higher in you machine.

install all requirements via command:
 ```python3 -m pip install requests```


2. Run it via comamnd ```./api_book_call.py```

##########################################################################

Script options:

What you need to provide at the first step is that you are choosing that you will by searching the movie via name or ID

for the name: you need to put the
```1``` in your terminal
for the option with the ID you need to put the:
```2``` in your terminal

And also you need to specify in the second step the plot information 

 which can be 'short' or 'full'.

 after setting this up you will recive the output about the movie.
 

