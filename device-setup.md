# How to Connect your Devices to Labstep

This guide will take you step-by-step through the process of setting up a new data-enabled device to send data automatically to Labstep.

## Creating a Labstep Resource for the Device.

If the device you want to connect is not already on Labstep (through Discover Resources) you will need to create a new resource to represent it on Labstep. 

This can be done with an API request of the following form:

```
curl -X POST "https://api.labstep.com/api/generic/resource" 
-H "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    "name": "NAME_OF_DEVICE",
    "resource_category_id": "99",
    "metadata": "{
       ...
    }"
}
```
In the metadata you can include specifics about the device such as the manufacturer and model number. For a full list of the allowed metadata fields see ____.

The response should contain an `id` field. Make a note of this `id`. You will need it later.

## Creating a Protocol to use with the Device.

### Create a new protocol.

First create an empty protocol with the following request.

```
curl -X POST "https://api.labstep.com/api/generic/protocol" 
-H  "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    "name": "MY_NEW_PROTOCOL"
}
```
The response should contain an `id` field. Make a note of this `id`. You will need it later.

### Add a data field to the protocol.

Next you need to specify that this protocol involves data collection. This is done with the `protocol_value` entity.  

When you add a `protocol_value` to your protocol, you have to give it a `name` to describe what the data is and specify a `type`. Currently the only supported type is `Number`, however in the future we hope to support other data-types.

To populate the `protocol_value` with some data from your device, specify the `resource_id` of the device. 

```
curl -X POST "https://api.labstep.com/api/generic/protocol-value" 
-H  "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    "protocol_id": "YOUR_PROTOCOL_ID",
    "resource_id": "YOUR_RESOURCE_ID",
    "type": "Number",
    "name": "MY_DATA_FIELD"
}
```

## Adding an instance of your device to your inventory.

In order to use the device to send data you need to add it to your inventory. You can add as many instances of the same device to your inventory as you want, for example if you have two or three of the same machine. 

Using the resource id obtained previously, send the following request...

```
curl -X POST "https://api.labstep.com/api/generic/inventory-item" 
-H  "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    resource_id: YOUR_RESOURCE_ID
    metadata:{
        ...
    }
}
```
In the metadata field you can include extra information specific to each instance i.e. serial number, last service date etc. For a full list of allowed metadata fields see ____.

You should recieve a response with a field `device_key`. Make a note of this, you will need it for the next step.

## Setting up your plugin.

Set up your device to make a request of the following form when it makes a measurement.

```
curl -X POST "https://api.labstep.com/api/generic/device-data" 
-H  "Content-Type: application/json"
-H "device_key: YOUR_DEVICE_KEY"
{
   "label": "YOUR_LABEL",
   "type": "Number"
   "data": "{
       value: 23,
       unit: "oC"
   }" 
}
```
To see the full accepted data schema for different data types see ___.

If your data is a file, you have to upload it to labstep using a request of the form...

```
curl -X POST "https://api.labstep.com/api/generic/file/upload" 
-H Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVPoOA1MymxABBQmh
-H "device_key: YOUR_DEVICE_KEY"

------WebKitFormBoundaryVPoOA1MymxABBQmh
Content-Disposition: form-data; name="label"

YOUR_LABEL

------WebKitFormBoundaryVPoOA1MymxABBQmh
Content-Disposition: form-data; name="file"; filename="figure1.png"
Content-Type: image/png


------WebKitFormBoundaryVPoOA1MymxABBQmh--
```

## Creating an experiment from your protocol.

To run your protocol make the following request:

```
curl -X POST "https://api.labstep.com/api/generic/experiment" 
-H  "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    protocol_id: YOUR_PROTOCOL_ID,
    name: 'My First Protocol Run'
}
```

You will see that an `experiment_value` has been created based on the `protocol_value` you created above. Note the `id` of this `experiment_value` as you will need it for the next step.

## Load data from the device. 

Next you need to point your new `experiment_value` to data that has been sent by the device.

### Search for data from your device.

Find all data sent by your device.

```
curl -X POST "https://api.labstep.com/api/generic/device-data" 
-H  "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    inventory_item_id: YOUR_INVENTORY_ITEM_ID,
}
```
Pick the correct one based on `label`, `type` and `created_at`. Make a note of the `id`.

For files use this instead...



### Update the `experiment_value`.

Finally, point the `experiment_value` to the `device_data`.

```
curl -X PUT "https://api.labstep.com/api/generic/experiment-value" 
-H  "Content-Type: application/json"
-H "apikey: YOUR_API_KEY"
{
    device_data_id: DEVICE_DATA_ID
}
```


