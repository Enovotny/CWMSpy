# cda_client.TimeSeriesCategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_timeseries_category_with_category_id**](TimeSeriesCategoriesApi.md#delete_cwms_data_timeseries_category_with_category_id) | **DELETE** /cwms-data/timeseries/category/{category-id} | Delete cwmsData timeseries category with categoryId
[**get_cwms_data_timeseries_category**](TimeSeriesCategoriesApi.md#get_cwms_data_timeseries_category) | **GET** /cwms-data/timeseries/category | Get cwmsData timeseries category
[**get_cwms_data_timeseries_category_with_category_id**](TimeSeriesCategoriesApi.md#get_cwms_data_timeseries_category_with_category_id) | **GET** /cwms-data/timeseries/category/{category-id} | Get cwmsData timeseries category with categoryId
[**post_cwms_data_timeseries_category**](TimeSeriesCategoriesApi.md#post_cwms_data_timeseries_category) | **POST** /cwms-data/timeseries/category | Post cwmsData timeseries category

# **delete_cwms_data_timeseries_category_with_category_id**
> delete_cwms_data_timeseries_category_with_category_id(category_id, office, cascade_delete=cascade_delete)

Delete cwmsData timeseries category with categoryId

Deletes requested time series category

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
api_instance = cda_client.TimeSeriesCategoriesApi(cda_client.ApiClient(configuration))
category_id = 'category_id_example' # str | The time series category to be deleted
office = 'office_example' # str | Specifies the owning office of the time series category to be deleted
cascade_delete = true # bool | Specifies whether to delete any time series groups in this time series category. Default: false (optional)

try:
    # Delete cwmsData timeseries category with categoryId
    api_instance.delete_cwms_data_timeseries_category_with_category_id(category_id, office, cascade_delete=cascade_delete)
except ApiException as e:
    print("Exception when calling TimeSeriesCategoriesApi->delete_cwms_data_timeseries_category_with_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The time series category to be deleted | 
 **office** | **str**| Specifies the owning office of the time series category to be deleted | 
 **cascade_delete** | **bool**| Specifies whether to delete any time series groups in this time series category. Default: false | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_category**
> list[TimeSeriesCategory] get_cwms_data_timeseries_category(office=office)

Get cwmsData timeseries category

Returns CWMS timeseries category Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeSeriesCategoriesApi()
office = 'office_example' # str | Specifies the owning office of the timeseries category(ies) whose data is to be included in the response. If this field is not specified, matching timeseries category information from all offices shall be returned. (optional)

try:
    # Get cwmsData timeseries category
    api_response = api_instance.get_cwms_data_timeseries_category(office=office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesCategoriesApi->get_cwms_data_timeseries_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the timeseries category(ies) whose data is to be included in the response. If this field is not specified, matching timeseries category information from all offices shall be returned. | [optional] 

### Return type

[**list[TimeSeriesCategory]**](TimeSeriesCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries_category_with_category_id**
> TimeSeriesCategory get_cwms_data_timeseries_category_with_category_id(category_id, office)

Get cwmsData timeseries category with categoryId

Retrieves requested timeseries category

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeSeriesCategoriesApi()
category_id = 'category_id_example' # str | Specifies the Category whose data is to be included in the response.
office = 'office_example' # str | Specifies the owning office of the timeseries category whose data is to be included in the response.

try:
    # Get cwmsData timeseries category with categoryId
    api_response = api_instance.get_cwms_data_timeseries_category_with_category_id(category_id, office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesCategoriesApi->get_cwms_data_timeseries_category_with_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| Specifies the Category whose data is to be included in the response. | 
 **office** | **str**| Specifies the owning office of the timeseries category whose data is to be included in the response. | 

### Return type

[**TimeSeriesCategory**](TimeSeriesCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_timeseries_category**
> post_cwms_data_timeseries_category(body, fail_if_exists=fail_if_exists)

Post cwmsData timeseries category

Create new TimeSeriesCategory

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
api_instance = cda_client.TimeSeriesCategoriesApi(cda_client.ApiClient(configuration))
body = cda_client.TimeSeriesCategory() # TimeSeriesCategory | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData timeseries category
    api_instance.post_cwms_data_timeseries_category(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling TimeSeriesCategoriesApi->post_cwms_data_timeseries_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeriesCategory**](TimeSeriesCategory.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

