# cda_client.CatalogApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_catalog_with_dataset**](CatalogApi.md#get_cwms_data_catalog_with_dataset) | **GET** /cwms-data/catalog/{dataset} | Get cwmsData catalog with dataset

# **get_cwms_data_catalog_with_dataset**
> Catalog get_cwms_data_catalog_with_dataset(dataset, page=page, cursor=cursor, page_size=page_size, page_size=page_size, unit_system=unit_system, unit_system=unit_system, office=office, like=like, timeseries_category_like=timeseries_category_like, timeseries_category_like=timeseries_category_like, timeseries_group_like=timeseries_group_like, timeseries_group_like=timeseries_group_like, location_category_like=location_category_like, location_category_like=location_category_like, location_group_like=location_group_like, location_group_like=location_group_like, bounding_office_like=bounding_office_like)

Get cwmsData catalog with dataset

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.CatalogApi()
dataset = cda_client.CatalogableEndpoint() # CatalogableEndpoint | A list of what data? E.g. Timeseries, Locations, Ratings, etc
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. (optional)
cursor = 'cursor_example' # str | Deprecated. Use 'page' instead. (optional)
page_size = 56 # int | How many entires per page returned. Default 500. (optional)
page_size = 56 # int | Deprecated. Use page-size. (optional)
unit_system = cda_client.UnitSystem() # UnitSystem | Deprecated. Use unit-system. (optional)
unit_system = cda_client.UnitSystem() # UnitSystem | Unit System desired in response. Can be SI (International Scientific) or EN (Imperial.) If unspecified, defaults to SI. (optional)
office = 'office_example' # str | 3-4 letter office name representing the district you want to isolate data to. (optional)
like = 'like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the id (optional)
timeseries_category_like = 'timeseries_category_like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the timeseries category id (optional)
timeseries_category_like = 'timeseries_category_like_example' # str | Deprecated. Use timeseries-category-like. (optional)
timeseries_group_like = 'timeseries_group_like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the timeseries group id (optional)
timeseries_group_like = 'timeseries_group_like_example' # str | Deprecated. Use timeseries-group-like. (optional)
location_category_like = 'location_category_like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the location category id (optional)
location_category_like = 'location_category_like_example' # str | Deprecated. Use location-category-like. (optional)
location_group_like = 'location_group_like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the location group id (optional)
location_group_like = 'location_group_like_example' # str | Deprecated. Use location-group-like. (optional)
bounding_office_like = 'bounding_office_like_example' # str | Posix <a href=\"regexp.html\">regular expression</a> matching against the location bounding office. When this field is used items with no bounding office set will not be present in results. (optional)

try:
    # Get cwmsData catalog with dataset
    api_response = api_instance.get_cwms_data_catalog_with_dataset(dataset, page=page, cursor=cursor, page_size=page_size, page_size=page_size, unit_system=unit_system, unit_system=unit_system, office=office, like=like, timeseries_category_like=timeseries_category_like, timeseries_category_like=timeseries_category_like, timeseries_group_like=timeseries_group_like, timeseries_group_like=timeseries_group_like, location_category_like=location_category_like, location_category_like=location_category_like, location_group_like=location_group_like, location_group_like=location_group_like, bounding_office_like=bounding_office_like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_cwms_data_catalog_with_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | [**CatalogableEndpoint**](.md)| A list of what data? E.g. Timeseries, Locations, Ratings, etc | 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. | [optional] 
 **cursor** | **str**| Deprecated. Use &#x27;page&#x27; instead. | [optional] 
 **page_size** | **int**| How many entires per page returned. Default 500. | [optional] 
 **page_size** | **int**| Deprecated. Use page-size. | [optional] 
 **unit_system** | [**UnitSystem**](.md)| Deprecated. Use unit-system. | [optional] 
 **unit_system** | [**UnitSystem**](.md)| Unit System desired in response. Can be SI (International Scientific) or EN (Imperial.) If unspecified, defaults to SI. | [optional] 
 **office** | **str**| 3-4 letter office name representing the district you want to isolate data to. | [optional] 
 **like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the id | [optional] 
 **timeseries_category_like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the timeseries category id | [optional] 
 **timeseries_category_like** | **str**| Deprecated. Use timeseries-category-like. | [optional] 
 **timeseries_group_like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the timeseries group id | [optional] 
 **timeseries_group_like** | **str**| Deprecated. Use timeseries-group-like. | [optional] 
 **location_category_like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the location category id | [optional] 
 **location_category_like** | **str**| Deprecated. Use location-category-like. | [optional] 
 **location_group_like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the location group id | [optional] 
 **location_group_like** | **str**| Deprecated. Use location-group-like. | [optional] 
 **bounding_office_like** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt; matching against the location bounding office. When this field is used items with no bounding office set will not be present in results. | [optional] 

### Return type

[**Catalog**](Catalog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

