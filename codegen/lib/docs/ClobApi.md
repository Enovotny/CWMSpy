# cda_client.ClobApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_clobs_with_clob_id**](ClobApi.md#delete_cwms_data_clobs_with_clob_id) | **DELETE** /cwms-data/clobs/{clob-id} | Delete cwmsData clobs with clobId
[**get_cwms_data_clobs**](ClobApi.md#get_cwms_data_clobs) | **GET** /cwms-data/clobs | Get cwmsData clobs
[**get_cwms_data_clobs_with_clob_id**](ClobApi.md#get_cwms_data_clobs_with_clob_id) | **GET** /cwms-data/clobs/{clob-id} | Get cwmsData clobs with clobId
[**patch_cwms_data_clobs_with_clob_id**](ClobApi.md#patch_cwms_data_clobs_with_clob_id) | **PATCH** /cwms-data/clobs/{clob-id} | Patch cwmsData clobs with clobId
[**post_cwms_data_clobs**](ClobApi.md#post_cwms_data_clobs) | **POST** /cwms-data/clobs | Post cwmsData clobs

# **delete_cwms_data_clobs_with_clob_id**
> delete_cwms_data_clobs_with_clob_id(clob_id, office)

Delete cwmsData clobs with clobId

Delete clob

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
api_instance = cda_client.ClobApi(cda_client.ApiClient(configuration))
clob_id = 'clob_id_example' # str | Specifies the id of the clob to be deleted
office = 'office_example' # str | Specifies the office of the clob.

try:
    # Delete cwmsData clobs with clobId
    api_instance.delete_cwms_data_clobs_with_clob_id(clob_id, office)
except ApiException as e:
    print("Exception when calling ClobApi->delete_cwms_data_clobs_with_clob_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clob_id** | **str**| Specifies the id of the clob to be deleted | 
 **office** | **str**| Specifies the office of the clob. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_clobs**
> Clobs get_cwms_data_clobs(office=office, page=page, cursor=cursor, page_size=page_size, page_size=page_size, include_values=include_values, include_values=include_values, like=like)

Get cwmsData clobs

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.ClobApi()
office = 'office_example' # str | Specifies the owning office. If this field is not specified, matching information from all offices shall be returned. (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
cursor = 'cursor_example' # str | Deprecated. Use 'page' instead. (optional)
page_size = 56 # int | How many entries per page returned. Default 20. (optional)
page_size = 56 # int | Deprecated, use 'page-size' instead. (optional)
include_values = true # bool | Do you want the value associated with this particular clob (default: false) (optional)
include_values = true # bool | Deprecated, use 'include-values' instead. (optional)
like = 'like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the id (optional)

try:
    # Get cwmsData clobs
    api_response = api_instance.get_cwms_data_clobs(office=office, page=page, cursor=cursor, page_size=page_size, page_size=page_size, include_values=include_values, include_values=include_values, like=like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClobApi->get_cwms_data_clobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office. If this field is not specified, matching information from all offices shall be returned. | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **cursor** | **str**| Deprecated. Use &#x27;page&#x27; instead. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 20. | [optional] 
 **page_size** | **int**| Deprecated, use &#x27;page-size&#x27; instead. | [optional] 
 **include_values** | **bool**| Do you want the value associated with this particular clob (default: false) | [optional] 
 **include_values** | **bool**| Deprecated, use &#x27;include-values&#x27; instead. | [optional] 
 **like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the id | [optional] 

### Return type

[**Clobs**](Clobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_clobs_with_clob_id**
> Clob get_cwms_data_clobs_with_clob_id(clob_id, office=office)

Get cwmsData clobs with clobId

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.ClobApi()
clob_id = 'clob_id_example' # str | 
office = 'office_example' # str | Specifies the owning office. (optional)

try:
    # Get cwmsData clobs with clobId
    api_response = api_instance.get_cwms_data_clobs_with_clob_id(clob_id, office=office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClobApi->get_cwms_data_clobs_with_clob_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clob_id** | **str**|  | 
 **office** | **str**| Specifies the owning office. | [optional] 

### Return type

[**Clob**](Clob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_clobs_with_clob_id**
> patch_cwms_data_clobs_with_clob_id(body, clob_id, ignore_nulls=ignore_nulls)

Patch cwmsData clobs with clobId

Update clob

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
api_instance = cda_client.ClobApi(cda_client.ApiClient(configuration))
body = cda_client.Clob() # Clob | 
clob_id = 'clob_id_example' # str | Specifies the id of the clob to be updated
ignore_nulls = true # bool | If true, null and empty fields in the provided clob will be ignored and the existing value of those fields left in place. Default: true (optional)

try:
    # Patch cwmsData clobs with clobId
    api_instance.patch_cwms_data_clobs_with_clob_id(body, clob_id, ignore_nulls=ignore_nulls)
except ApiException as e:
    print("Exception when calling ClobApi->patch_cwms_data_clobs_with_clob_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Clob**](Clob.md)|  | 
 **clob_id** | **str**| Specifies the id of the clob to be updated | 
 **ignore_nulls** | **bool**| If true, null and empty fields in the provided clob will be ignored and the existing value of those fields left in place. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json;version=2, application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_clobs**
> post_cwms_data_clobs(body, fail_if_exists=fail_if_exists)

Post cwmsData clobs

Create new Clob

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
api_instance = cda_client.ClobApi(cda_client.ApiClient(configuration))
body = cda_client.Clob() # Clob | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData clobs
    api_instance.post_cwms_data_clobs(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling ClobApi->post_cwms_data_clobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Clob**](Clob.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json;version=2, application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

