# cda_client.PoolsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_pools**](PoolsApi.md#get_cwms_data_pools) | **GET** /cwms-data/pools | Get cwmsData pools
[**get_cwms_data_pools_with_pool_id**](PoolsApi.md#get_cwms_data_pools_with_pool_id) | **GET** /cwms-data/pools/{pool-id} | Get cwmsData pools with poolId

# **get_cwms_data_pools**
> Pools get_cwms_data_pools(office=office, id_mask=id_mask, name_mask=name_mask, bottom_mask=bottom_mask, top_mask=top_mask, include_explicit=include_explicit, include_implicit=include_implicit, page=page, cursor=cursor, page_size=page_size, page_size=page_size)

Get cwmsData pools

Returns Pools Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.PoolsApi()
office = 'office_example' # str | Specifies the owning office of the data in the response. If this field is not specified, matching items from all offices shall be returned. (optional)
id_mask = 'id_mask_example' # str | Project Id mask. Default value:* (optional)
name_mask = 'name_mask_example' # str | Name mask. Default value:* (optional)
bottom_mask = 'bottom_mask_example' # str | Bottom level mask. Default value:* (optional)
top_mask = 'top_mask_example' # str | Top level mask. Default value:* (optional)
include_explicit = 'include_explicit_example' # str | Specifies if the results should include explicit Pools. Default value:false (optional)
include_implicit = 'include_implicit_example' # str | Specifies if the results should include implicit Pools. Default value:true (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
cursor = 'cursor_example' # str | Deprecated. Use 'page' instead. (optional)
page_size = 56 # int | How many entries per page returned. Default 100. (optional)
page_size = 56 # int | Deprecated. Use 'page-size' instead. (optional)

try:
    # Get cwmsData pools
    api_response = api_instance.get_cwms_data_pools(office=office, id_mask=id_mask, name_mask=name_mask, bottom_mask=bottom_mask, top_mask=top_mask, include_explicit=include_explicit, include_implicit=include_implicit, page=page, cursor=cursor, page_size=page_size, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->get_cwms_data_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the data in the response. If this field is not specified, matching items from all offices shall be returned. | [optional] 
 **id_mask** | **str**| Project Id mask. Default value:* | [optional] 
 **name_mask** | **str**| Name mask. Default value:* | [optional] 
 **bottom_mask** | **str**| Bottom level mask. Default value:* | [optional] 
 **top_mask** | **str**| Top level mask. Default value:* | [optional] 
 **include_explicit** | **str**| Specifies if the results should include explicit Pools. Default value:false | [optional] 
 **include_implicit** | **str**| Specifies if the results should include implicit Pools. Default value:true | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **cursor** | **str**| Deprecated. Use &#x27;page&#x27; instead. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 100. | [optional] 
 **page_size** | **int**| Deprecated. Use &#x27;page-size&#x27; instead. | [optional] 

### Return type

[**Pools**](Pools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_pools_with_pool_id**
> Pool get_cwms_data_pools_with_pool_id(pool_id, office, project_id, bottom_mask=bottom_mask, top_mask=top_mask, include_explicit=include_explicit, include_implicit=include_implicit)

Get cwmsData pools with poolId

Retrieves requested Pool

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.PoolsApi()
pool_id = 'pool_id_example' # str | Specifies the pool whose data is to be included in the response.
office = 'office_example' # str | Specifies the owning office of the Pool whose data is to be included in the response.
project_id = 'project_id_example' # str | Specifies the project-id of the Pool whose data is to be included in the response.
bottom_mask = 'bottom_mask_example' # str | Bottom level mask. Default value:* (optional)
top_mask = 'top_mask_example' # str | Top level mask. Default value:* (optional)
include_explicit = 'include_explicit_example' # str | Specifies if the results should include explicit Pools. Default value:false (optional)
include_implicit = 'include_implicit_example' # str | Specifies if the results should include implicit Pools. Default value:true (optional)

try:
    # Get cwmsData pools with poolId
    api_response = api_instance.get_cwms_data_pools_with_pool_id(pool_id, office, project_id, bottom_mask=bottom_mask, top_mask=top_mask, include_explicit=include_explicit, include_implicit=include_implicit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->get_cwms_data_pools_with_pool_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Specifies the pool whose data is to be included in the response. | 
 **office** | **str**| Specifies the owning office of the Pool whose data is to be included in the response. | 
 **project_id** | **str**| Specifies the project-id of the Pool whose data is to be included in the response. | 
 **bottom_mask** | **str**| Bottom level mask. Default value:* | [optional] 
 **top_mask** | **str**| Top level mask. Default value:* | [optional] 
 **include_explicit** | **str**| Specifies if the results should include explicit Pools. Default value:false | [optional] 
 **include_implicit** | **str**| Specifies if the results should include implicit Pools. Default value:true | [optional] 

### Return type

[**Pool**](Pool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

