# cda_client.ParametersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_parameters**](ParametersApi.md#get_cwms_data_parameters) | **GET** /cwms-data/parameters | Get cwmsData parameters

# **get_cwms_data_parameters**
> get_cwms_data_parameters(format=format)

Get cwmsData parameters

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.ParametersApi()
format = 'format_example' # str | Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) (optional)

try:
    # Get cwmsData parameters
    api_instance.get_cwms_data_parameters(format=format)
except ApiException as e:
    print("Exception when calling ParametersApi->get_cwms_data_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

