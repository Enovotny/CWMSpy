# cda_client.TimeseriesGroupsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_timeseries_group_with_group_id**](TimeseriesGroupsApi.md#delete_cwms_data_timeseries_group_with_group_id) | **DELETE** /cwms-data/timeseries/group/{group-id} | Delete cwmsData timeseries group with groupId
[**get_cwms_data_timeseries_group**](TimeseriesGroupsApi.md#get_cwms_data_timeseries_group) | **GET** /cwms-data/timeseries/group | Get cwmsData timeseries group
[**get_cwms_data_timeseries_group_with_group_id**](TimeseriesGroupsApi.md#get_cwms_data_timeseries_group_with_group_id) | **GET** /cwms-data/timeseries/group/{group-id} | Get cwmsData timeseries group with groupId
[**patch_cwms_data_timeseries_group_with_group_id**](TimeseriesGroupsApi.md#patch_cwms_data_timeseries_group_with_group_id) | **PATCH** /cwms-data/timeseries/group/{group-id} | Patch cwmsData timeseries group with groupId
[**post_cwms_data_timeseries_group**](TimeseriesGroupsApi.md#post_cwms_data_timeseries_group) | **POST** /cwms-data/timeseries/group | Post cwmsData timeseries group

# **delete_cwms_data_timeseries_group_with_group_id**
> delete_cwms_data_timeseries_group_with_group_id(group_id, category_id, office)

Delete cwmsData timeseries group with groupId

Deletes requested time series group

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.TimeseriesGroupsApi(cda_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The time series group to be deleted
category_id = 'category_id_example' # str | Specifies the time series category of the time series group to be deleted
office = 'office_example' # str | Specifies the owning office of the time series group to be deleted

try:
    # Delete cwmsData timeseries group with groupId
    api_instance.delete_cwms_data_timeseries_group_with_group_id(group_id, category_id, office)
except ApiException as e:
    print("Exception when calling TimeseriesGroupsApi->delete_cwms_data_timeseries_group_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The time series group to be deleted | 
 **category_id** | **str**| Specifies the time series category of the time series group to be deleted | 
 **office** | **str**| Specifies the owning office of the time series group to be deleted | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_group**
> list[TimeSeriesGroup] get_cwms_data_timeseries_group(office=office)

Get cwmsData timeseries group

Returns CWMS Timeseries Groups Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeseriesGroupsApi()
office = 'office_example' # str | Specifies the owning office of the timeseries group(s) whose data is to be included in the response. If this field is not specified, matching timeseries groups information from all offices shall be returned. (optional)

try:
    # Get cwmsData timeseries group
    api_response = api_instance.get_cwms_data_timeseries_group(office=office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeseriesGroupsApi->get_cwms_data_timeseries_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the timeseries group(s) whose data is to be included in the response. If this field is not specified, matching timeseries groups information from all offices shall be returned. | [optional] 

### Return type

[**list[TimeSeriesGroup]**](TimeSeriesGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_group_with_group_id**
> TimeSeriesGroup get_cwms_data_timeseries_group_with_group_id(group_id, office, category_id)

Get cwmsData timeseries group with groupId

Retrieves requested timeseries group

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeseriesGroupsApi()
group_id = 'group_id_example' # str | Specifies the timeseries group whose data is to be included in the response
office = 'office_example' # str | Specifies the owning office of the timeseries group whose data is to be included in the response.
category_id = 'category_id_example' # str | Specifies the category containing the timeseries group whose data is to be included in the response.

try:
    # Get cwmsData timeseries group with groupId
    api_response = api_instance.get_cwms_data_timeseries_group_with_group_id(group_id, office, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeseriesGroupsApi->get_cwms_data_timeseries_group_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Specifies the timeseries group whose data is to be included in the response | 
 **office** | **str**| Specifies the owning office of the timeseries group whose data is to be included in the response. | 
 **category_id** | **str**| Specifies the category containing the timeseries group whose data is to be included in the response. | 

### Return type

[**TimeSeriesGroup**](TimeSeriesGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_timeseries_group_with_group_id**
> patch_cwms_data_timeseries_group_with_group_id(body, office, group_id, replace_assigned_ts=replace_assigned_ts)

Patch cwmsData timeseries group with groupId

Update existing TimeSeriesGroup

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.TimeseriesGroupsApi(cda_client.ApiClient(configuration))
body = cda_client.TimeSeriesGroup() # TimeSeriesGroup | 
office = 'office_example' # str | Specifies the owning office of the time series group to be updated
group_id = 'group_id_example' # str | 
replace_assigned_ts = true # bool | Specifies whether to unassign all existing time series before assigning new time series specified in the content body Default: false (optional)

try:
    # Patch cwmsData timeseries group with groupId
    api_instance.patch_cwms_data_timeseries_group_with_group_id(body, office, group_id, replace_assigned_ts=replace_assigned_ts)
except ApiException as e:
    print("Exception when calling TimeseriesGroupsApi->patch_cwms_data_timeseries_group_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeriesGroup**](TimeSeriesGroup.md)|  | 
 **office** | **str**| Specifies the owning office of the time series group to be updated | 
 **group_id** | **str**|  | 
 **replace_assigned_ts** | **bool**| Specifies whether to unassign all existing time series before assigning new time series specified in the content body Default: false | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_timeseries_group**
> post_cwms_data_timeseries_group(body, fail_if_exists=fail_if_exists)

Post cwmsData timeseries group

Create new TimeSeriesGroup

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.TimeseriesGroupsApi(cda_client.ApiClient(configuration))
body = cda_client.TimeSeriesGroup() # TimeSeriesGroup | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData timeseries group
    api_instance.post_cwms_data_timeseries_group(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling TimeseriesGroupsApi->post_cwms_data_timeseries_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeriesGroup**](TimeSeriesGroup.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

