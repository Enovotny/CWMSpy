# cda_client.BlobApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_blobs**](BlobApi.md#get_cwms_data_blobs) | **GET** /cwms-data/blobs | Get cwmsData blobs
[**get_cwms_data_blobs_with_blob_id**](BlobApi.md#get_cwms_data_blobs_with_blob_id) | **GET** /cwms-data/blobs/{blob-id} | Get cwmsData blobs with blobId

# **get_cwms_data_blobs**
> Blobs get_cwms_data_blobs(office=office, page=page, cursor=cursor, page_size=page_size, page_size=page_size, like=like)

Get cwmsData blobs

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.BlobApi()
office = 'office_example' # str | Specifies the owning office. If this field is not specified, matching information from all offices shall be returned. (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
cursor = 'cursor_example' # str | Deprecated. Use 'page' instead. (optional)
page_size = 56 # int | Deprecated.  Use page-size instead. (optional)
page_size = 56 # int | How many entries per page returned. Default 20. (optional)
like = 'like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> describing the blob id's you want (optional)

try:
    # Get cwmsData blobs
    api_response = api_instance.get_cwms_data_blobs(office=office, page=page, cursor=cursor, page_size=page_size, page_size=page_size, like=like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobApi->get_cwms_data_blobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office. If this field is not specified, matching information from all offices shall be returned. | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **cursor** | **str**| Deprecated. Use &#x27;page&#x27; instead. | [optional] 
 **page_size** | **int**| Deprecated.  Use page-size instead. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 20. | [optional] 
 **like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; describing the blob id&#x27;s you want | [optional] 

### Return type

[**Blobs**](Blobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_blobs_with_blob_id**
> get_cwms_data_blobs_with_blob_id(blob_id, office=office)

Get cwmsData blobs with blobId

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.BlobApi()
blob_id = 'blob_id_example' # str | 
office = 'office_example' # str | Specifies the owning office. (optional)

try:
    # Get cwmsData blobs with blobId
    api_instance.get_cwms_data_blobs_with_blob_id(blob_id, office=office)
except ApiException as e:
    print("Exception when calling BlobApi->get_cwms_data_blobs_with_blob_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_id** | **str**|  | 
 **office** | **str**| Specifies the owning office. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

