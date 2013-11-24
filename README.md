Code Snippet
The getComponents() method provides means to get the components of an aspect.
               param params is an array for the components.
               param successCallback Success callback.
               
 RemoteDeviceStatusManager.prototype.getComponents = 
                function (params, successCallback) {
                        devicestatusmodule.devicestatus.getComponents(
                                params[0],
                                function (components) {
                                        successCallback(components);
                                }
                        );
                };

The isSupported() method checks if an aspect is supported and, optionally, if a property that would correspond to a component of that aspect is supported (e.g., a Battery aspect's batteryLevel property). Check for the device type, if we support it via config check the native implementation to return a Success Callback.
RemoteDeviceStatusManager.prototype.isSupported = 
                function (params, successCallback) {
                        if (params && params.length == 2 && params[0] == "Device" && params[1] == "type") 
                                successCallback({ aspect:params[0], property:params[1],isSupported:true});
                        else 
                                devicestatusmodule.devicestatus.isSupported(
                                        params[0],
                                        params[1],
                                        function (res) {
                                                successCallback(res);
                                        }
                                );
                };

The getPropertyValue() method asyncrhonously attemps to read the value of a given component. However, if no component is given, the user agent will default to the active component or the default component of a given aspect. Check for the device type, if we support it via config check the native implementation to return a Success Callback.
RemoteDeviceStatusManager.prototype.getPropertyValue = 
                function (params, successCallback, errorCallback) {
                        if (params && params[0] && params[0].aspect == "Device" && params[0].property == "type"){ 
                try
                {
                    var Pzp = require(require("path").join(require.main.paths[0], "..", "lib", "pzp_sessionHandling.js"));
                    successCallback(Pzp.getInstance().getMetaData("deviceType") || "Undefined");
                } catch(err){
                    successCallback("Undefined");
                }
                        }else 
                                devicestatusmodule.devicestatus.getPropertyValue(
                                        function (prop) {
                                                successCallback(prop);
                                        },
                                        function (err) {
                                                errorCallback(err);
                                        },
                                        params[0]
                                );
                };

