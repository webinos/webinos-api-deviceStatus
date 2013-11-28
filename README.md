# webinos device status API #

**Service Type**: http://webinos.org/api/devicestatus

The main concept of device status API is to !TODO!


## Installation ##

To install the device status API you will need to npm the node module inside the webinos pzp.

For end users, you can simply open a command prompt in the root of your webinos-pzp and do: 

	npm install https://github.com/webinos/webinos-api-deviceStatus.git

For developers that want to tweak the API, you should fork this repository and clone your fork inside the node_module of your pzp.

	cd node_modules
	git clone https://github.com/<your GitHub account>/webinos-api-deviceStatus.git
	cd webinos-api-deviceStatus
	npm install


## Getting a reference to the service ##

To discover the service you will have to search for the "http://webinos.org/api/devicestatus" type. Example:

	var serviceType = "http://webinos.org/api/devicestatus";
	webinos.discovery.findServices( new ServiceType(serviceType), 
		{ 
			onFound: serviceFoundFn, 
			onError: handleErrorFn
		}
	);
	function serviceFoundFn(service){
		// Do something with the service
	};
	function handleErrorFn(error){
		// Notify user
		console.log(error.message);
	}

Alternatively you can use the webinos dashboard to allow the user choose the device status API to use. Example:
 	
	webinos.dashboard.open({
         module:'explorer',
	     data:{
         	service:[
            	'http://webinos.org/api/devicestatus'
         	],
            select:"services"
         }
     }).onAction(function successFn(data){
		  if (data.result.length > 0){
			// User selected some services
		  }
	 });

## Methods ##

Once you have a reference to an instance of a service you can use the following methods:

###getComponents (aspect, successCallback, errorCallback)

The getComponents() method provides means to get the components of an aspect.

###isSupported (aspect, property, successCallback)

The isSupported() method checks if an aspect is supported and, optionally, if a property that would correspond to a component of that aspect is supported (e.g., a Battery aspect's batteryLevel property).

###getPropertyValue (successCallback, errorCallback, prop)

The getPropertyValue() method asyncrhonously attemps to read the value of a given component. However, if no component is given, the user agent will default to the active component or the default component of a given aspect.


## Links ##

- [Specifications](http://dev.webinos.org/specifications/api/devicestatus.html)
- [Examples](https://github.com/webinos/webinos-api-deviceStatus/wiki/Examples)

