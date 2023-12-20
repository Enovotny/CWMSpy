# cda_client.TimeZonesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_timezones**](TimeZonesApi.md#get_cwms_data_timezones) | **GET** /cwms-data/timezones | Get cwmsData timezones

# **get_cwms_data_timezones**
> get_cwms_data_timezones(format=format)

Get cwmsData timezones

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeZonesApi()
format = 'format_example' # str | Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) (optional)

try:
    # Get cwmsData timezones
    api_instance.get_cwms_data_timezones(format=format)
except ApiException as e:
    print("Exception when calling TimeZonesApi->get_cwms_data_timezones: %s\n" % e)
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

