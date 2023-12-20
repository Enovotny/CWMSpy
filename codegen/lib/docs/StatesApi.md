# cda_client.StatesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_states**](StatesApi.md#get_cwms_data_states) | **GET** /cwms-data/states | Get cwmsData states

# **get_cwms_data_states**
> list[State] get_cwms_data_states()

Get cwmsData states

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.StatesApi()

try:
    # Get cwmsData states
    api_response = api_instance.get_cwms_data_states()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatesApi->get_cwms_data_states: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[State]**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

