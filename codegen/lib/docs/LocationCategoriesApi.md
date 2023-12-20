# cda_client.LocationCategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_location_category_with_category_id**](LocationCategoriesApi.md#delete_cwms_data_location_category_with_category_id) | **DELETE** /cwms-data/location/category/{category-id} | Delete cwmsData location category with categoryId
[**get_cwms_data_location_category**](LocationCategoriesApi.md#get_cwms_data_location_category) | **GET** /cwms-data/location/category | Get cwmsData location category
[**get_cwms_data_location_category_with_category_id**](LocationCategoriesApi.md#get_cwms_data_location_category_with_category_id) | **GET** /cwms-data/location/category/{category-id} | Get cwmsData location category with categoryId
[**post_cwms_data_location_category**](LocationCategoriesApi.md#post_cwms_data_location_category) | **POST** /cwms-data/location/category | Post cwmsData location category

# **delete_cwms_data_location_category_with_category_id**
> delete_cwms_data_location_category_with_category_id(category_id, office, cascade_delete=cascade_delete)

Delete cwmsData location category with categoryId

Deletes requested location category

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
api_instance = cda_client.LocationCategoriesApi(cda_client.ApiClient(configuration))
category_id = 'category_id_example' # str | The location category to be deleted
office = 'office_example' # str | Specifies the owning office of the location category to be deleted
cascade_delete = true # bool | Specifies whether to delete any location groups in this location category. Default: false (optional)

try:
    # Delete cwmsData location category with categoryId
    api_instance.delete_cwms_data_location_category_with_category_id(category_id, office, cascade_delete=cascade_delete)
except ApiException as e:
    print("Exception when calling LocationCategoriesApi->delete_cwms_data_location_category_with_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The location category to be deleted | 
 **office** | **str**| Specifies the owning office of the location category to be deleted | 
 **cascade_delete** | **bool**| Specifies whether to delete any location groups in this location category. Default: false | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_location_category**
> list[LocationCategory] get_cwms_data_location_category(office=office)

Get cwmsData location category

Returns CWMS Location Category Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LocationCategoriesApi()
office = 'office_example' # str | Specifies the owning office of the location category(ies) whose data is to be included in the response. If this field is not specified, matching location category information from all offices shall be returned. (optional)

try:
    # Get cwmsData location category
    api_response = api_instance.get_cwms_data_location_category(office=office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationCategoriesApi->get_cwms_data_location_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the location category(ies) whose data is to be included in the response. If this field is not specified, matching location category information from all offices shall be returned. | [optional] 

### Return type

[**list[LocationCategory]**](LocationCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_location_category_with_category_id**
> LocationCategory get_cwms_data_location_category_with_category_id(category_id, office)

Get cwmsData location category with categoryId

Retrieves requested Location Category

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LocationCategoriesApi()
category_id = 'category_id_example' # str | Specifies the Category whose data is to be included in the response.
office = 'office_example' # str | Specifies the owning office of the Location Category whose data is to be included in the response.

try:
    # Get cwmsData location category with categoryId
    api_response = api_instance.get_cwms_data_location_category_with_category_id(category_id, office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationCategoriesApi->get_cwms_data_location_category_with_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| Specifies the Category whose data is to be included in the response. | 
 **office** | **str**| Specifies the owning office of the Location Category whose data is to be included in the response. | 

### Return type

[**LocationCategory**](LocationCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_location_category**
> post_cwms_data_location_category(body)

Post cwmsData location category

Create new LocationCategory

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
api_instance = cda_client.LocationCategoriesApi(cda_client.ApiClient(configuration))
body = cda_client.LocationCategory() # LocationCategory | 

try:
    # Post cwmsData location category
    api_instance.post_cwms_data_location_category(body)
except ApiException as e:
    print("Exception when calling LocationCategoriesApi->post_cwms_data_location_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationCategory**](LocationCategory.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

