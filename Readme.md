
- 🔭 Enjoy the Falcon Testing Automation.

## This Testing Boilerplate code Test any Falcon Service.


## Follow Below steps to getting started with Instabot and automate your commenting and like.
</br>
<b>Step 1: </b>  modify services.py for name of the services you are going to test. 
<br/>
<b>Step 2: </b> Test case can be placed inside cases folder.
<br />
<b> Step 4: </b> Open bot.py and change some required information.
<br />
<b> Step 4: </b> Open terminal and start run.sh file ($ ./run.sh)



## Note:

Falcon req.stream behaviour:-

As detailed in the docs about req.stream.read() method and we are using it, is very dependent upon the WSGI server implementation. 

When emulating requests with the Falcon testing framework, the server is effectively Python standard wsgiref, with some Falcon wrappers around.

If you are concerned with the req.stream behaviour and don't mind a slight performance penalty, req.bounded_stream could be used to normalize the behaviour across WSGI servers.

## Production:
	body = json.loads(req.stream.read())
## Testing:
	body = json.loads(req.bounded_stream.read().decode())


## you are Done......