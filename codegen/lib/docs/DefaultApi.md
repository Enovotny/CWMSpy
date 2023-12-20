# cda_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data**](DefaultApi.md#get_cwms_data) | **GET** /cwms-data | Get cwmsData
[**get_cwms_data_levels_with_level_id_timeseries**](DefaultApi.md#get_cwms_data_levels_with_level_id_timeseries) | **GET** /cwms-data/levels/{level-id}/timeseries | Get cwmsData levels with levelId timeseries
[**get_cwms_data_timeseries_recent_with_group_id**](DefaultApi.md#get_cwms_data_timeseries_recent_with_group_id) | **GET** /cwms-data/timeseries/recent/{group-id} | Get cwmsData timeseries recent with groupId

# **get_cwms_data**
> get_cwms_data()

Get cwmsData

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.DefaultApi()

try:
    # Get cwmsData
    api_instance.get_cwms_data()
except ApiException as e:
    print("Exception when calling DefaultApi->get_cwms_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_levels_with_level_id_timeseries**
> get_cwms_data_levels_with_level_id_timeseries(level_id)

Get cwmsData levels with levelId timeseries

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.DefaultApi()
level_id = 'level_id_example' # str | 

try:
    # Get cwmsData levels with levelId timeseries
    api_instance.get_cwms_data_levels_with_level_id_timeseries(level_id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cwms_data_levels_with_level_id_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_recent_with_group_id**
> get_cwms_data_timeseries_recent_with_group_id(group_id)

Get cwmsData timeseries recent with groupId

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.DefaultApi()
group_id = 'group_id_example' # str | 

try:
    # Get cwmsData timeseries recent with groupId
    api_instance.get_cwms_data_timeseries_recent_with_group_id(group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cwms_data_timeseries_recent_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

