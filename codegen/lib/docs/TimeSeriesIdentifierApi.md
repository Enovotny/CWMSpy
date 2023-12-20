# cda_client.TimeSeriesIdentifierApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_timeseries_identifier_descriptor_with_timeseries_id**](TimeSeriesIdentifierApi.md#delete_cwms_data_timeseries_identifier_descriptor_with_timeseries_id) | **DELETE** /cwms-data/timeseries/identifier-descriptor/{timeseries-id} | Delete cwmsData timeseries identifierDescriptor with timeseriesId
[**get_cwms_data_timeseries_identifier_descriptor**](TimeSeriesIdentifierApi.md#get_cwms_data_timeseries_identifier_descriptor) | **GET** /cwms-data/timeseries/identifier-descriptor | Get cwmsData timeseries identifierDescriptor
[**get_cwms_data_timeseries_identifier_descriptor_with_timeseries_id**](TimeSeriesIdentifierApi.md#get_cwms_data_timeseries_identifier_descriptor_with_timeseries_id) | **GET** /cwms-data/timeseries/identifier-descriptor/{timeseries-id} | Get cwmsData timeseries identifierDescriptor with timeseriesId
[**patch_cwms_data_timeseries_identifier_descriptor_with_timeseries_id**](TimeSeriesIdentifierApi.md#patch_cwms_data_timeseries_identifier_descriptor_with_timeseries_id) | **PATCH** /cwms-data/timeseries/identifier-descriptor/{timeseries-id} | Patch cwmsData timeseries identifierDescriptor with timeseriesId
[**post_cwms_data_timeseries_identifier_descriptor**](TimeSeriesIdentifierApi.md#post_cwms_data_timeseries_identifier_descriptor) | **POST** /cwms-data/timeseries/identifier-descriptor | Post cwmsData timeseries identifierDescriptor

# **delete_cwms_data_timeseries_identifier_descriptor_with_timeseries_id**
> delete_cwms_data_timeseries_identifier_descriptor_with_timeseries_id(timeseries_id, office, method)

Delete cwmsData timeseries identifierDescriptor with timeseriesId

Deletes requested timeseries identifier

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
api_instance = cda_client.TimeSeriesIdentifierApi(cda_client.ApiClient(configuration))
timeseries_id = 'timeseries_id_example' # str | The timeseries-id of the timeseries to be deleted. 
office = 'office_example' # str | Specifies the owning office of the timeseries to be deleted.
method = cda_client.DeleteMethod() # DeleteMethod | Specifies the delete method used.

try:
    # Delete cwmsData timeseries identifierDescriptor with timeseriesId
    api_instance.delete_cwms_data_timeseries_identifier_descriptor_with_timeseries_id(timeseries_id, office, method)
except ApiException as e:
    print("Exception when calling TimeSeriesIdentifierApi->delete_cwms_data_timeseries_identifier_descriptor_with_timeseries_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeseries_id** | **str**| The timeseries-id of the timeseries to be deleted.  | 
 **office** | **str**| Specifies the owning office of the timeseries to be deleted. | 
 **method** | [**DeleteMethod**](.md)| Specifies the delete method used. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_identifier_descriptor**
> TimeSeriesIdentifierDescriptors get_cwms_data_timeseries_identifier_descriptor(office=office, timeseries_id_regex=timeseries_id_regex, page=page, page_size=page_size)

Get cwmsData timeseries identifierDescriptor

Returns CWMS timeseries identifier descriptorData

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeSeriesIdentifierApi()
office = 'office_example' # str | Specifies the owning office of the timeseries identifier(s) whose data is to be included in the response. If this field is not specified, matching timeseries identifier information from all offices shall be returned. (optional)
timeseries_id_regex = 'timeseries_id_regex_example' # str | A case insensitive RegExp that will be applied to the timeseries-id field. If this field is not specified the results will not be constrained by timeseries-id. (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
page_size = 56 # int | How many entries per page returned. Default 500. (optional)

try:
    # Get cwmsData timeseries identifierDescriptor
    api_response = api_instance.get_cwms_data_timeseries_identifier_descriptor(office=office, timeseries_id_regex=timeseries_id_regex, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesIdentifierApi->get_cwms_data_timeseries_identifier_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the timeseries identifier(s) whose data is to be included in the response. If this field is not specified, matching timeseries identifier information from all offices shall be returned. | [optional] 
 **timeseries_id_regex** | **str**| A case insensitive RegExp that will be applied to the timeseries-id field. If this field is not specified the results will not be constrained by timeseries-id. | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 500. | [optional] 

### Return type

[**TimeSeriesIdentifierDescriptors**](TimeSeriesIdentifierDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_identifier_descriptor_with_timeseries_id**
> TimeSeriesIdentifierDescriptor get_cwms_data_timeseries_identifier_descriptor_with_timeseries_id(timeseries_id, office)

Get cwmsData timeseries identifierDescriptor with timeseriesId

Retrieves requested timeseries identifier descriptor

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeSeriesIdentifierApi()
timeseries_id = 'timeseries_id_example' # str | Specifies the identifier of the timeseries to be included in the response.
office = 'office_example' # str | Specifies the owning office of the timeseries identifier to be included in the response.

try:
    # Get cwmsData timeseries identifierDescriptor with timeseriesId
    api_response = api_instance.get_cwms_data_timeseries_identifier_descriptor_with_timeseries_id(timeseries_id, office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesIdentifierApi->get_cwms_data_timeseries_identifier_descriptor_with_timeseries_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeseries_id** | **str**| Specifies the identifier of the timeseries to be included in the response. | 
 **office** | **str**| Specifies the owning office of the timeseries identifier to be included in the response. | 

### Return type

[**TimeSeriesIdentifierDescriptor**](TimeSeriesIdentifierDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_timeseries_identifier_descriptor_with_timeseries_id**
> patch_cwms_data_timeseries_identifier_descriptor_with_timeseries_id(timeseries_id, timeseries_id, office, interval_offset=interval_offset, snap_forward=snap_forward, snap_backward=snap_backward, active=active)

Patch cwmsData timeseries identifierDescriptor with timeseriesId

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
api_instance = cda_client.TimeSeriesIdentifierApi(cda_client.ApiClient(configuration))
timeseries_id = 'timeseries_id_example' # str | 
timeseries_id = 'timeseries_id_example' # str | A new timeseries-id.  If specified a rename operation will be performed and snap-forward, snap-backward, and active must not be provided
office = 'office_example' # str | Specifies the owning office of the timeseries identifier to be updated
interval_offset = 789 # int | The offset into the data interval in minutes.  If specified and a new timeseries-id is also specified both will be passed to a rename operation.  May also be passed to update operation. (optional)
snap_forward = 789 # int | The new snap forward tolerance in minutes. This specifies how many minutes before the expected data time that data will be considered to be on time. (optional)
snap_backward = 789 # int | The new snap backward tolerance in minutes. This specifies how many minutes after the expected data time that data will be considered to be on time. (optional)
active = true # bool | 'True' or 'true' if the time series is active (optional)

try:
    # Patch cwmsData timeseries identifierDescriptor with timeseriesId
    api_instance.patch_cwms_data_timeseries_identifier_descriptor_with_timeseries_id(timeseries_id, timeseries_id, office, interval_offset=interval_offset, snap_forward=snap_forward, snap_backward=snap_backward, active=active)
except ApiException as e:
    print("Exception when calling TimeSeriesIdentifierApi->patch_cwms_data_timeseries_identifier_descriptor_with_timeseries_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeseries_id** | **str**|  | 
 **timeseries_id** | **str**| A new timeseries-id.  If specified a rename operation will be performed and snap-forward, snap-backward, and active must not be provided | 
 **office** | **str**| Specifies the owning office of the timeseries identifier to be updated | 
 **interval_offset** | **int**| The offset into the data interval in minutes.  If specified and a new timeseries-id is also specified both will be passed to a rename operation.  May also be passed to update operation. | [optional] 
 **snap_forward** | **int**| The new snap forward tolerance in minutes. This specifies how many minutes before the expected data time that data will be considered to be on time. | [optional] 
 **snap_backward** | **int**| The new snap backward tolerance in minutes. This specifies how many minutes after the expected data time that data will be considered to be on time. | [optional] 
 **active** | **bool**| &#x27;True&#x27; or &#x27;true&#x27; if the time series is active | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_timeseries_identifier_descriptor**
> post_cwms_data_timeseries_identifier_descriptor(body, fail_if_exists=fail_if_exists)

Post cwmsData timeseries identifierDescriptor

Create new TimeSeriesIdentifierDescriptor

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
api_instance = cda_client.TimeSeriesIdentifierApi(cda_client.ApiClient(configuration))
body = cda_client.TimeSeriesIdentifierDescriptor() # TimeSeriesIdentifierDescriptor | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData timeseries identifierDescriptor
    api_instance.post_cwms_data_timeseries_identifier_descriptor(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling TimeSeriesIdentifierApi->post_cwms_data_timeseries_identifier_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeriesIdentifierDescriptor**](TimeSeriesIdentifierDescriptor.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json;version=2, application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

