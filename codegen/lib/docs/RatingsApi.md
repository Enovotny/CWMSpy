# cda_client.RatingsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_ratings_spec_with_rating_id**](RatingsApi.md#delete_cwms_data_ratings_spec_with_rating_id) | **DELETE** /cwms-data/ratings/spec/{rating-id} | Delete cwmsData ratings spec with ratingId
[**delete_cwms_data_ratings_template_with_template_id**](RatingsApi.md#delete_cwms_data_ratings_template_with_template_id) | **DELETE** /cwms-data/ratings/template/{template-id} | Delete cwmsData ratings template with templateId
[**delete_cwms_data_ratings_with_rating_id**](RatingsApi.md#delete_cwms_data_ratings_with_rating_id) | **DELETE** /cwms-data/ratings/{rating-id} | Delete cwmsData ratings with ratingId
[**get_cwms_data_ratings**](RatingsApi.md#get_cwms_data_ratings) | **GET** /cwms-data/ratings | Get cwmsData ratings
[**get_cwms_data_ratings_metadata**](RatingsApi.md#get_cwms_data_ratings_metadata) | **GET** /cwms-data/ratings/metadata | Get cwmsData ratings metadata
[**get_cwms_data_ratings_spec**](RatingsApi.md#get_cwms_data_ratings_spec) | **GET** /cwms-data/ratings/spec | Get cwmsData ratings spec
[**get_cwms_data_ratings_spec_with_rating_id**](RatingsApi.md#get_cwms_data_ratings_spec_with_rating_id) | **GET** /cwms-data/ratings/spec/{rating-id} | Get cwmsData ratings spec with ratingId
[**get_cwms_data_ratings_template**](RatingsApi.md#get_cwms_data_ratings_template) | **GET** /cwms-data/ratings/template | Get cwmsData ratings template
[**get_cwms_data_ratings_template_with_template_id**](RatingsApi.md#get_cwms_data_ratings_template_with_template_id) | **GET** /cwms-data/ratings/template/{template-id} | Get cwmsData ratings template with templateId
[**get_cwms_data_ratings_with_rating_id**](RatingsApi.md#get_cwms_data_ratings_with_rating_id) | **GET** /cwms-data/ratings/{rating-id} | Get cwmsData ratings with ratingId
[**patch_cwms_data_ratings_with_rating_id**](RatingsApi.md#patch_cwms_data_ratings_with_rating_id) | **PATCH** /cwms-data/ratings/{rating-id} | Patch cwmsData ratings with ratingId
[**post_cwms_data_ratings**](RatingsApi.md#post_cwms_data_ratings) | **POST** /cwms-data/ratings | Post cwmsData ratings
[**post_cwms_data_ratings_spec**](RatingsApi.md#post_cwms_data_ratings_spec) | **POST** /cwms-data/ratings/spec | Post cwmsData ratings spec
[**post_cwms_data_ratings_template**](RatingsApi.md#post_cwms_data_ratings_template) | **POST** /cwms-data/ratings/template | Post cwmsData ratings template

# **delete_cwms_data_ratings_spec_with_rating_id**
> delete_cwms_data_ratings_spec_with_rating_id(rating_id, office, method)

Delete cwmsData ratings spec with ratingId

Deletes requested rating specification

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
rating_id = 'rating_id_example' # str | The rating-spec-id of the ratings data to be deleted.
office = 'office_example' # str | Specifies the owning office of the ratings to be deleted.
method = cda_client.DeleteMethod() # DeleteMethod | Specifies the delete method used.

try:
    # Delete cwmsData ratings spec with ratingId
    api_instance.delete_cwms_data_ratings_spec_with_rating_id(rating_id, office, method)
except ApiException as e:
    print("Exception when calling RatingsApi->delete_cwms_data_ratings_spec_with_rating_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| The rating-spec-id of the ratings data to be deleted. | 
 **office** | **str**| Specifies the owning office of the ratings to be deleted. | 
 **method** | [**DeleteMethod**](.md)| Specifies the delete method used. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cwms_data_ratings_template_with_template_id**
> delete_cwms_data_ratings_template_with_template_id(template_id, office, method)

Delete cwmsData ratings template with templateId

Deletes requested rating specification

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
template_id = 'template_id_example' # str | The rating-template-id of the ratings data to be deleted.
office = 'office_example' # str | Specifies the owning office of the ratings to be deleted.
method = cda_client.DeleteMethod() # DeleteMethod | Specifies the delete method used.

try:
    # Delete cwmsData ratings template with templateId
    api_instance.delete_cwms_data_ratings_template_with_template_id(template_id, office, method)
except ApiException as e:
    print("Exception when calling RatingsApi->delete_cwms_data_ratings_template_with_template_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The rating-template-id of the ratings data to be deleted. | 
 **office** | **str**| Specifies the owning office of the ratings to be deleted. | 
 **method** | [**DeleteMethod**](.md)| Specifies the delete method used. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cwms_data_ratings_with_rating_id**
> delete_cwms_data_ratings_with_rating_id(rating_id, office, begin, end, timezone=timezone)

Delete cwmsData ratings with ratingId

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
rating_id = 'rating_id_example' # str | The rating-id of the effective dates to be deleted. 
office = 'office_example' # str | Specifies the office of the ratings to be deleted.
begin = 'begin_example' # str | The start of the time window to delete. The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., 'YYYY-MM-dd'T'hh:mm:ss[Z'['VV']']', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'.
end = 'end_example' # str | The end of the time window to delete.The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., 'YYYY-MM-dd'T'hh:mm:ss[Z'['VV']']', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'.
timezone = 'timezone_example' # str | This field specifies a default timezone to be used if the format of the begin, end, or version-date parameters do not include offset or time zone information. Defaults to UTC. (optional)

try:
    # Delete cwmsData ratings with ratingId
    api_instance.delete_cwms_data_ratings_with_rating_id(rating_id, office, begin, end, timezone=timezone)
except ApiException as e:
    print("Exception when calling RatingsApi->delete_cwms_data_ratings_with_rating_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| The rating-id of the effective dates to be deleted.  | 
 **office** | **str**| Specifies the office of the ratings to be deleted. | 
 **begin** | **str**| The start of the time window to delete. The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., &#x27;YYYY-MM-dd&#x27;T&#x27;hh:mm:ss[Z&#x27;[&#x27;VV&#x27;]&#x27;]&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | 
 **end** | **str**| The end of the time window to delete.The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., &#x27;YYYY-MM-dd&#x27;T&#x27;hh:mm:ss[Z&#x27;[&#x27;VV&#x27;]&#x27;]&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | 
 **timezone** | **str**| This field specifies a default timezone to be used if the format of the begin, end, or version-date parameters do not include offset or time zone information. Defaults to UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings**
> Unit get_cwms_data_ratings(name=name, office=office, unit=unit, datum=datum, at=at, end=end, timezone=timezone, format=format)

Get cwmsData ratings

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
name = 'name_example' # str | Specifies the name(s) of the rating whose data is to be included in the response. A case insensitive comparison is used to match names. (optional)
office = 'office_example' # str | Specifies the owning office of the Rating(s) whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. (optional)
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:  1. EN.   Specifies English unit system.  Rating values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Rating values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. (optional)
datum = 'datum_example' # str | Specifies the elevation datum of the response. This field affects only elevation Ratings. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. (optional)
at = 'at_example' # str | Specifies the start of the time window for data to be included in the response. If this field is not specified, any required time window begins 24 hours prior to the specified or default end time. (optional)
end = 'end_example' # str | Specifies the end of the time window for data to be included in the response. If this field is not specified, any required time window ends at the current time (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used. (optional)
format = 'format_example' # str | Specifies the encoding format of the response. Valid values for the format field for this URI are:  1.    tab  2.    csv  3.    xml  4.    json (default) (optional)

try:
    # Get cwmsData ratings
    api_response = api_instance.get_cwms_data_ratings(name=name, office=office, unit=unit, datum=datum, at=at, end=end, timezone=timezone, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name(s) of the rating whose data is to be included in the response. A case insensitive comparison is used to match names. | [optional] 
 **office** | **str**| Specifies the owning office of the Rating(s) whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | [optional] 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:  1. EN.   Specifies English unit system.  Rating values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Rating values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. | [optional] 
 **datum** | **str**| Specifies the elevation datum of the response. This field affects only elevation Ratings. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. | [optional] 
 **at** | **str**| Specifies the start of the time window for data to be included in the response. If this field is not specified, any required time window begins 24 hours prior to the specified or default end time. | [optional] 
 **end** | **str**| Specifies the end of the time window for data to be included in the response. If this field is not specified, any required time window ends at the current time | [optional] 
 **timezone** | **str**| Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used. | [optional] 
 **format** | **str**| Specifies the encoding format of the response. Valid values for the format field for this URI are:  1.    tab  2.    csv  3.    xml  4.    json (default) | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/tab-separated-values, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings_metadata**
> RatingMetadataList get_cwms_data_ratings_metadata(office=office, rating_id_mask=rating_id_mask, start=start, end=end, timezone=timezone, page=page, page_size=page_size)

Get cwmsData ratings metadata

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
office = 'office_example' # str | Specifies the owning office of the Rating Specs whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. (optional)
rating_id_mask = 'rating_id_mask_example' # str | RegExp that specifies the rating IDs to be included in the response. If this field is not specified, all Rating Specs shall be returned. (optional)
start = 'start_example' # str | Specifies the start of the time window of the effective dates to be included. If this field is not specified no start time will be used. (optional)
end = 'end_example' # str | Specifies the end of the time window for effective dates to be included. If this field is not specified no end time will be used. (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the values of the begin and end fields (unless otherwise specified). If this field is not specified, the default time zone of UTC shall be used. (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
page_size = 56 # int | How many entries per page returned. Default 50. (optional)

try:
    # Get cwmsData ratings metadata
    api_response = api_instance.get_cwms_data_ratings_metadata(office=office, rating_id_mask=rating_id_mask, start=start, end=end, timezone=timezone, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the Rating Specs whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | [optional] 
 **rating_id_mask** | **str**| RegExp that specifies the rating IDs to be included in the response. If this field is not specified, all Rating Specs shall be returned. | [optional] 
 **start** | **str**| Specifies the start of the time window of the effective dates to be included. If this field is not specified no start time will be used. | [optional] 
 **end** | **str**| Specifies the end of the time window for effective dates to be included. If this field is not specified no end time will be used. | [optional] 
 **timezone** | **str**| Specifies the time zone of the values of the begin and end fields (unless otherwise specified). If this field is not specified, the default time zone of UTC shall be used. | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 50. | [optional] 

### Return type

[**RatingMetadataList**](RatingMetadataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings_spec**
> RatingSpecs get_cwms_data_ratings_spec(office=office, rating_id_mask=rating_id_mask, page=page, page_size=page_size)

Get cwmsData ratings spec

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
office = 'office_example' # str | Specifies the owning office of the Rating Specs whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. (optional)
rating_id_mask = 'rating_id_mask_example' # str | Posix <a href=\"regexp.html\">regular expression</a>  that specifies the rating IDs to be included in the response. If this field is not specified, all Rating Specs shall be returned. (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
page_size = 56 # int | How many entries per page returned. Default 100. (optional)

try:
    # Get cwmsData ratings spec
    api_response = api_instance.get_cwms_data_ratings_spec(office=office, rating_id_mask=rating_id_mask, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the Rating Specs whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | [optional] 
 **rating_id_mask** | **str**| Posix &lt;a href&#x3D;\&quot;regexp.html\&quot;&gt;regular expression&lt;/a&gt;  that specifies the rating IDs to be included in the response. If this field is not specified, all Rating Specs shall be returned. | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 100. | [optional] 

### Return type

[**RatingSpecs**](RatingSpecs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings_spec_with_rating_id**
> RatingSpec get_cwms_data_ratings_spec_with_rating_id(rating_id, office)

Get cwmsData ratings spec with ratingId

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
rating_id = 'rating_id_example' # str | Specifies the rating-id of the Rating Spec to be included in the response
office = 'office_example' # str | Specifies the owning office of the Rating Specs whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned.

try:
    # Get cwmsData ratings spec with ratingId
    api_response = api_instance.get_cwms_data_ratings_spec_with_rating_id(rating_id, office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings_spec_with_rating_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| Specifies the rating-id of the Rating Spec to be included in the response | 
 **office** | **str**| Specifies the owning office of the Rating Specs whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | 

### Return type

[**RatingSpec**](RatingSpec.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings_template**
> RatingTemplates get_cwms_data_ratings_template(office=office, template_id_mask=template_id_mask, page=page, page_size=page_size)

Get cwmsData ratings template

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
office = 'office_example' # str | Specifies the owning office of the Rating Templates whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. (optional)
template_id_mask = 'template_id_mask_example' # str | RegExp that specifies the rating template IDs to be included in the response. If this field is not specified, all rating templates shall be returned. (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
page_size = 56 # int | How many entries per page returned. Default 100. (optional)

try:
    # Get cwmsData ratings template
    api_response = api_instance.get_cwms_data_ratings_template(office=office, template_id_mask=template_id_mask, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the Rating Templates whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | [optional] 
 **template_id_mask** | **str**| RegExp that specifies the rating template IDs to be included in the response. If this field is not specified, all rating templates shall be returned. | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 100. | [optional] 

### Return type

[**RatingTemplates**](RatingTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings_template_with_template_id**
> list[RatingTemplate] get_cwms_data_ratings_template_with_template_id(template_id, office)

Get cwmsData ratings template with templateId

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
template_id = 'template_id_example' # str | Specifies the template whose data is to be included in the response
office = 'office_example' # str | Specifies the owning office of the Rating Templates whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned.

try:
    # Get cwmsData ratings template with templateId
    api_response = api_instance.get_cwms_data_ratings_template_with_template_id(template_id, office)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings_template_with_template_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Specifies the template whose data is to be included in the response | 
 **office** | **str**| Specifies the owning office of the Rating Templates whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | 

### Return type

[**list[RatingTemplate]**](RatingTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_ratings_with_rating_id**
> Unit get_cwms_data_ratings_with_rating_id(rating_id, office, begin=begin, end=end, timezone=timezone, method=method)

Get cwmsData ratings with ratingId

Returns CWMS Rating Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.RatingsApi()
rating_id = 'rating_id_example' # str | The rating-id of the effective dates to be retrieve. 
office = 'office_example' # str | Specifies the owning office of the ratingset to be included in the response.
begin = 'begin_example' # str | Specifies the start of the time window for data to be included in the response. If this field is not specified no start time will be used. (optional)
end = 'end_example' # str | Specifies the end of the time window for data to be included in the response. If this field is not specified no end time will be used. (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used. (optional)
method = cda_client.DatabaseLoadMethod() # DatabaseLoadMethod | Specifies the retrieval method used.  If no method is provided EAGER will be used. (optional)

try:
    # Get cwmsData ratings with ratingId
    api_response = api_instance.get_cwms_data_ratings_with_rating_id(rating_id, office, begin=begin, end=end, timezone=timezone, method=method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_cwms_data_ratings_with_rating_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| The rating-id of the effective dates to be retrieve.  | 
 **office** | **str**| Specifies the owning office of the ratingset to be included in the response. | 
 **begin** | **str**| Specifies the start of the time window for data to be included in the response. If this field is not specified no start time will be used. | [optional] 
 **end** | **str**| Specifies the end of the time window for data to be included in the response. If this field is not specified no end time will be used. | [optional] 
 **timezone** | **str**| Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used. | [optional] 
 **method** | [**DatabaseLoadMethod**](.md)| Specifies the retrieval method used.  If no method is provided EAGER will be used. | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_ratings_with_rating_id**
> patch_cwms_data_ratings_with_rating_id(body, rating_id, store_template=store_template)

Patch cwmsData ratings with ratingId

Update a RatingSet

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
body = cda_client.Unit() # Unit | 
rating_id = 'rating_id_example' # str | 
store_template = true # bool | Also store updates to the rating template. Default: true (optional)

try:
    # Patch cwmsData ratings with ratingId
    api_instance.patch_cwms_data_ratings_with_rating_id(body, rating_id, store_template=store_template)
except ApiException as e:
    print("Exception when calling RatingsApi->patch_cwms_data_ratings_with_rating_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Unit**](Unit.md)|  | 
 **rating_id** | **str**|  | 
 **store_template** | **bool**| Also store updates to the rating template. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/xml;version=2, application/json;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_ratings**
> post_cwms_data_ratings(body, store_template=store_template)

Post cwmsData ratings

Create new RatingSet

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
body = cda_client.Unit() # Unit | 
store_template = true # bool | Also store updates to the rating template. Default: true (optional)

try:
    # Post cwmsData ratings
    api_instance.post_cwms_data_ratings(body, store_template=store_template)
except ApiException as e:
    print("Exception when calling RatingsApi->post_cwms_data_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Unit**](Unit.md)|  | 
 **store_template** | **bool**| Also store updates to the rating template. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/xml;version=2, application/json;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_ratings_spec**
> post_cwms_data_ratings_spec(body, fail_if_exists=fail_if_exists)

Post cwmsData ratings spec

Create new Rating Specification

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
body = cda_client.RatingSpec() # RatingSpec | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData ratings spec
    api_instance.post_cwms_data_ratings_spec(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling RatingsApi->post_cwms_data_ratings_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingSpec**](RatingSpec.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_ratings_template**
> post_cwms_data_ratings_template(body, fail_if_exists=fail_if_exists)

Post cwmsData ratings template

Create new Rating Template

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
api_instance = cda_client.RatingsApi(cda_client.ApiClient(configuration))
body = cda_client.RatingTemplate() # RatingTemplate | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData ratings template
    api_instance.post_cwms_data_ratings_template(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling RatingsApi->post_cwms_data_ratings_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RatingTemplate**](RatingTemplate.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

