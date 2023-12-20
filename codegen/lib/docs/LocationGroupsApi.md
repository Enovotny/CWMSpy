# cda_client.LocationGroupsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_location_group_with_group_id**](LocationGroupsApi.md#delete_cwms_data_location_group_with_group_id) | **DELETE** /cwms-data/location/group/{group-id} | Delete cwmsData location group with groupId
[**get_cwms_data_location_group**](LocationGroupsApi.md#get_cwms_data_location_group) | **GET** /cwms-data/location/group | Get cwmsData location group
[**get_cwms_data_location_group_with_group_id**](LocationGroupsApi.md#get_cwms_data_location_group_with_group_id) | **GET** /cwms-data/location/group/{group-id} | Get cwmsData location group with groupId
[**patch_cwms_data_location_group_with_group_id**](LocationGroupsApi.md#patch_cwms_data_location_group_with_group_id) | **PATCH** /cwms-data/location/group/{group-id} | Patch cwmsData location group with groupId
[**post_cwms_data_location_group**](LocationGroupsApi.md#post_cwms_data_location_group) | **POST** /cwms-data/location/group | Post cwmsData location group

# **delete_cwms_data_location_group_with_group_id**
> delete_cwms_data_location_group_with_group_id(group_id, category_id, office, cascade_delete=cascade_delete)

Delete cwmsData location group with groupId

Deletes requested location group

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
api_instance = cda_client.LocationGroupsApi(cda_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The location group to be deleted
category_id = 'category_id_example' # str | Specifies the location category of the location group to be deleted
office = 'office_example' # str | Specifies the owning office of the location group to be deleted
cascade_delete = true # bool | Specifies whether to specifies whether to unassign any location assignments. Default: false (optional)

try:
    # Delete cwmsData location group with groupId
    api_instance.delete_cwms_data_location_group_with_group_id(group_id, category_id, office, cascade_delete=cascade_delete)
except ApiException as e:
    print("Exception when calling LocationGroupsApi->delete_cwms_data_location_group_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The location group to be deleted | 
 **category_id** | **str**| Specifies the location category of the location group to be deleted | 
 **office** | **str**| Specifies the owning office of the location group to be deleted | 
 **cascade_delete** | **bool**| Specifies whether to specifies whether to unassign any location assignments. Default: false | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_location_group**
> list[LocationGroup] get_cwms_data_location_group(office=office, include_assigned=include_assigned, include_assigned=include_assigned, location_category_like=location_category_like)

Get cwmsData location group

Returns CWMS Location Groups Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LocationGroupsApi()
office = 'office_example' # str | Specifies the owning office of the location group(s) whose data is to be included in the response. If this field is not specified, matching location groups information from all offices shall be returned. (optional)
include_assigned = true # bool | Include the assigned locations in the returned location groups. (default: false) (optional)
include_assigned = true # bool | Deprecated. Use include-assigned instead. (optional)
location_category_like = 'location_category_like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the location category id (optional)

try:
    # Get cwmsData location group
    api_response = api_instance.get_cwms_data_location_group(office=office, include_assigned=include_assigned, include_assigned=include_assigned, location_category_like=location_category_like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationGroupsApi->get_cwms_data_location_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the location group(s) whose data is to be included in the response. If this field is not specified, matching location groups information from all offices shall be returned. | [optional] 
 **include_assigned** | **bool**| Include the assigned locations in the returned location groups. (default: false) | [optional] 
 **include_assigned** | **bool**| Deprecated. Use include-assigned instead. | [optional] 
 **location_category_like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the location category id | [optional] 

### Return type

[**list[LocationGroup]**](LocationGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_location_group_with_group_id**
> LocationGroup get_cwms_data_location_group_with_group_id(group_id, office, category_id)

Get cwmsData location group with groupId

Retrieves requested Location Group

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LocationGroupsApi()
group_id = 'group_id_example' # str | Specifies the location_group whose data is to be included in the response
office = 'office_example' # str | Specifies the owning office of the location group whose data is to be included in the response.
category_id = 'category_id_example' # str | Specifies the category containing the location group whose data is to be included in the response.

try:
    # Get cwmsData location group with groupId
    api_response = api_instance.get_cwms_data_location_group_with_group_id(group_id, office, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationGroupsApi->get_cwms_data_location_group_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Specifies the location_group whose data is to be included in the response | 
 **office** | **str**| Specifies the owning office of the location group whose data is to be included in the response. | 
 **category_id** | **str**| Specifies the category containing the location group whose data is to be included in the response. | 

### Return type

[**LocationGroup**](LocationGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/geo+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_location_group_with_group_id**
> patch_cwms_data_location_group_with_group_id(body, office, group_id, replace_assigned_locs=replace_assigned_locs)

Patch cwmsData location group with groupId

Update existing LocationGroup

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
api_instance = cda_client.LocationGroupsApi(cda_client.ApiClient(configuration))
body = cda_client.LocationGroup() # LocationGroup | 
office = 'office_example' # str | Specifies the owning office of the location group to be updated
group_id = 'group_id_example' # str | 
replace_assigned_locs = true # bool | Specifies whether to unassign all existing locations before assigning new locations specified in the content body Default: false (optional)

try:
    # Patch cwmsData location group with groupId
    api_instance.patch_cwms_data_location_group_with_group_id(body, office, group_id, replace_assigned_locs=replace_assigned_locs)
except ApiException as e:
    print("Exception when calling LocationGroupsApi->patch_cwms_data_location_group_with_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationGroup**](LocationGroup.md)|  | 
 **office** | **str**| Specifies the owning office of the location group to be updated | 
 **group_id** | **str**|  | 
 **replace_assigned_locs** | **bool**| Specifies whether to unassign all existing locations before assigning new locations specified in the content body Default: false | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_location_group**
> post_cwms_data_location_group(body)

Post cwmsData location group

Create new LocationGroup

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
api_instance = cda_client.LocationGroupsApi(cda_client.ApiClient(configuration))
body = cda_client.LocationGroup() # LocationGroup | 

try:
    # Post cwmsData location group
    api_instance.post_cwms_data_location_group(body)
except ApiException as e:
    print("Exception when calling LocationGroupsApi->post_cwms_data_location_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationGroup**](LocationGroup.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

