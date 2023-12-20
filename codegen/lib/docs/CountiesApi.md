# cda_client.CountiesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_counties**](CountiesApi.md#get_cwms_data_counties) | **GET** /cwms-data/counties | Get cwmsData counties

# **get_cwms_data_counties**
> list[County] get_cwms_data_counties()

Get cwmsData counties

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.CountiesApi()

try:
    # Get cwmsData counties
    api_response = api_instance.get_cwms_data_counties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountiesApi->get_cwms_data_counties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[County]**](County.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

