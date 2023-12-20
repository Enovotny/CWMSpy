# cda_client.TimeSeriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_timeseries_with_timeseries**](TimeSeriesApi.md#delete_cwms_data_timeseries_with_timeseries) | **DELETE** /cwms-data/timeseries/{timeseries} | Delete cwmsData timeseries with timeseries
[**get_cwms_data_timeseries**](TimeSeriesApi.md#get_cwms_data_timeseries) | **GET** /cwms-data/timeseries | Get cwmsData timeseries
[**patch_cwms_data_timeseries_with_timeseries**](TimeSeriesApi.md#patch_cwms_data_timeseries_with_timeseries) | **PATCH** /cwms-data/timeseries/{timeseries} | Patch cwmsData timeseries with timeseries
[**post_cwms_data_timeseries**](TimeSeriesApi.md#post_cwms_data_timeseries) | **POST** /cwms-data/timeseries | Post cwmsData timeseries

# **delete_cwms_data_timeseries_with_timeseries**
> delete_cwms_data_timeseries_with_timeseries(timeseries, office, begin, end, timezone=timezone, version_date=version_date, start_time_inclusive=start_time_inclusive, end_time_inclusive=end_time_inclusive, max_version=max_version, override_protection=override_protection)

Delete cwmsData timeseries with timeseries

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
api_instance = cda_client.TimeSeriesApi(cda_client.ApiClient(configuration))
timeseries = 'timeseries_example' # str | The timeseries-id of the timeseries values to be deleted. 
office = 'office_example' # str | Specifies the office of the timeseries to be deleted.
begin = 'begin_example' # str | The start of the time window to delete. The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., 'YYYY-MM-dd'T'hh:mm:ss[Z'['VV']']', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'.
end = 'end_example' # str | The end of the time window to delete.The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., 'YYYY-MM-dd'T'hh:mm:ss[Z'['VV']']', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'.
timezone = 'timezone_example' # str | This field specifies a default timezone to be used if the format of the begin, end, or version-date parameters do not include offset or time zone information. Defaults to UTC. (optional)
version_date = 'version_date_example' # str | The version date/time of the time series in the specified or default time zone. If NULL, the earliest or latest version date will be used depending on p_max_version. (optional)
start_time_inclusive = true # bool | A flag specifying whether any data at the start time should be deleted ('True') or only data <b><em>after</em></b> the start time ('False').  Default value is True (optional)
end_time_inclusive = true # bool | A flag ('True'/'False') specifying whether any data at the end time should be deleted ('True') or only data <b><em>before</em></b> the end time ('False'). Default value is False (optional)
max_version = true # bool | A flag ('True'/'False') specifying whether to use the earliest ('False') or latest ('True') version date for each time if p_version_date is NULL.  Default is 'True' (optional)
override_protection = true # bool | A flag ('True'/'False') specifying whether to delete protected data. Default is False (optional)

try:
    # Delete cwmsData timeseries with timeseries
    api_instance.delete_cwms_data_timeseries_with_timeseries(timeseries, office, begin, end, timezone=timezone, version_date=version_date, start_time_inclusive=start_time_inclusive, end_time_inclusive=end_time_inclusive, max_version=max_version, override_protection=override_protection)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->delete_cwms_data_timeseries_with_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeseries** | **str**| The timeseries-id of the timeseries values to be deleted.  | 
 **office** | **str**| Specifies the office of the timeseries to be deleted. | 
 **begin** | **str**| The start of the time window to delete. The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., &#x27;YYYY-MM-dd&#x27;T&#x27;hh:mm:ss[Z&#x27;[&#x27;VV&#x27;]&#x27;]&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | 
 **end** | **str**| The end of the time window to delete.The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., &#x27;YYYY-MM-dd&#x27;T&#x27;hh:mm:ss[Z&#x27;[&#x27;VV&#x27;]&#x27;]&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | 
 **timezone** | **str**| This field specifies a default timezone to be used if the format of the begin, end, or version-date parameters do not include offset or time zone information. Defaults to UTC. | [optional] 
 **version_date** | **str**| The version date/time of the time series in the specified or default time zone. If NULL, the earliest or latest version date will be used depending on p_max_version. | [optional] 
 **start_time_inclusive** | **bool**| A flag specifying whether any data at the start time should be deleted (&#x27;True&#x27;) or only data &lt;b&gt;&lt;em&gt;after&lt;/em&gt;&lt;/b&gt; the start time (&#x27;False&#x27;).  Default value is True | [optional] 
 **end_time_inclusive** | **bool**| A flag (&#x27;True&#x27;/&#x27;False&#x27;) specifying whether any data at the end time should be deleted (&#x27;True&#x27;) or only data &lt;b&gt;&lt;em&gt;before&lt;/em&gt;&lt;/b&gt; the end time (&#x27;False&#x27;). Default value is False | [optional] 
 **max_version** | **bool**| A flag (&#x27;True&#x27;/&#x27;False&#x27;) specifying whether to use the earliest (&#x27;False&#x27;) or latest (&#x27;True&#x27;) version date for each time if p_version_date is NULL.  Default is &#x27;True&#x27; | [optional] 
 **override_protection** | **bool**| A flag (&#x27;True&#x27;/&#x27;False&#x27;) specifying whether to delete protected data. Default is False | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_timeseries**
> TimeSeries get_cwms_data_timeseries(name, office=office, unit=unit, datum=datum, begin=begin, end=end, timezone=timezone, format=format, page=page, cursor=cursor, page_size=page_size, page_size=page_size)

Get cwmsData timeseries

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.TimeSeriesApi()
name = 'name_example' # str | Specifies the name(s) of the time series whose data is to be included in the response. A case insensitive comparison is used to match names.
office = 'office_example' # str | Specifies the owning office of the time series(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. (optional)
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   (default) Specifies English unit system.  Location level values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location level values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. (optional)
datum = 'datum_example' # str | Specifies the elevation datum of the response. This field affects only elevation location levels. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. (optional)
begin = 'begin_example' # str | Specifies the start of the time window for data to be included in the response. If this field is not specified, any required time window begins 24 hours prior to the specified or default end time. The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., 'YYYY-MM-dd'T'hh:mm:ss[Z'['VV']']', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'. (optional)
end = 'end_example' # str | Specifies the end of the time window for data to be included in the response. If this field is not specified, any required time window ends at the current time. The format for this field is ISO 8601 extended, with optional timezone, i.e., 'YYYY-MM-dd'T'hh:mm:ss[Z'['VV']']', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'. (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used.  Ignored if begin was specified with offset and timezone. (optional)
format = 'format_example' # str | Specifies the encoding format of the response. Valid values for the format field for this URI are:  1.    tab  2.    csv  3.    xml  4.  wml2 (only if name field is specified)  5.    json (default) (optional)
page = 'page_example' # str | This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
cursor = 'cursor_example' # str | Deprecated. Use 'page' instead. (optional)
page_size = 56 # int | How many entries per page returned. Default 500. (optional)
page_size = 56 # int | Deprecated. Please use page-size instead. (optional)

try:
    # Get cwmsData timeseries
    api_response = api_instance.get_cwms_data_timeseries(name, office=office, unit=unit, datum=datum, begin=begin, end=end, timezone=timezone, format=format, page=page, cursor=cursor, page_size=page_size, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->get_cwms_data_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name(s) of the time series whose data is to be included in the response. A case insensitive comparison is used to match names. | 
 **office** | **str**| Specifies the owning office of the time series(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. | [optional] 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   (default) Specifies English unit system.  Location level values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location level values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. | [optional] 
 **datum** | **str**| Specifies the elevation datum of the response. This field affects only elevation location levels. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. | [optional] 
 **begin** | **str**| Specifies the start of the time window for data to be included in the response. If this field is not specified, any required time window begins 24 hours prior to the specified or default end time. The format for this field is ISO 8601 extended, with optional offset and timezone, i.e., &#x27;YYYY-MM-dd&#x27;T&#x27;hh:mm:ss[Z&#x27;[&#x27;VV&#x27;]&#x27;]&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | [optional] 
 **end** | **str**| Specifies the end of the time window for data to be included in the response. If this field is not specified, any required time window ends at the current time. The format for this field is ISO 8601 extended, with optional timezone, i.e., &#x27;YYYY-MM-dd&#x27;T&#x27;hh:mm:ss[Z&#x27;[&#x27;VV&#x27;]&#x27;]&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | [optional] 
 **timezone** | **str**| Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used.  Ignored if begin was specified with offset and timezone. | [optional] 
 **format** | **str**| Specifies the encoding format of the response. Valid values for the format field for this URI are:  1.    tab  2.    csv  3.    xml  4.  wml2 (only if name field is specified)  5.    json (default) | [optional] 
 **page** | **str**| This end point can return a lot of data, this identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **cursor** | **str**| Deprecated. Use &#x27;page&#x27; instead. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 500. | [optional] 
 **page_size** | **int**| Deprecated. Please use page-size instead. | [optional] 

### Return type

[**TimeSeries**](TimeSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2, application/xml;version=2, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_timeseries_with_timeseries**
> patch_cwms_data_timeseries_with_timeseries(body, timeseries, version_date=version_date, timezone=timezone, create_as_lrts=create_as_lrts, store_rule=store_rule, override_protection=override_protection)

Patch cwmsData timeseries with timeseries

Update a TimeSeries with provided values

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
api_instance = cda_client.TimeSeriesApi(cda_client.ApiClient(configuration))
body = cda_client.TimeSeries() # TimeSeries | 
timeseries = 'timeseries_example' # str | Full CWMS Timeseries name
version_date = 'version_date_example' # str | Specifies the version date for the timeseries to create. If this field is not specified, a null version date will be used.  The format for this field is ISO 8601 extended, with optional timezone, i.e., 'format', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'. (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the version-date field (unless otherwise specified). If this field is not specified, the default time zone of UTC shall be used.  Ignored if version-date was specified with offset and timezone. (optional)
create_as_lrts = true # bool |  (optional)
store_rule = cda_client.StoreRule() # StoreRule | The business rule to use when merging the incoming with existing data (optional)
override_protection = true # bool | A flag to ignore the protected data quality when storing data.  \"'true' or 'false'\" (optional)

try:
    # Patch cwmsData timeseries with timeseries
    api_instance.patch_cwms_data_timeseries_with_timeseries(body, timeseries, version_date=version_date, timezone=timezone, create_as_lrts=create_as_lrts, store_rule=store_rule, override_protection=override_protection)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->patch_cwms_data_timeseries_with_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeries**](TimeSeries.md)|  | 
 **timeseries** | **str**| Full CWMS Timeseries name | 
 **version_date** | **str**| Specifies the version date for the timeseries to create. If this field is not specified, a null version date will be used.  The format for this field is ISO 8601 extended, with optional timezone, i.e., &#x27;format&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | [optional] 
 **timezone** | **str**| Specifies the time zone of the version-date field (unless otherwise specified). If this field is not specified, the default time zone of UTC shall be used.  Ignored if version-date was specified with offset and timezone. | [optional] 
 **create_as_lrts** | **bool**|  | [optional] 
 **store_rule** | [**StoreRule**](.md)| The business rule to use when merging the incoming with existing data | [optional] 
 **override_protection** | **bool**| A flag to ignore the protected data quality when storing data.  \&quot;&#x27;true&#x27; or &#x27;false&#x27;\&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json;version=2, application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_timeseries**
> post_cwms_data_timeseries(body, version_date=version_date, timezone=timezone, create_as_lrts=create_as_lrts, store_rule=store_rule, override_protection=override_protection)

Post cwmsData timeseries

Create new TimeSeries, will store any data provided

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
api_instance = cda_client.TimeSeriesApi(cda_client.ApiClient(configuration))
body = cda_client.TimeSeries() # TimeSeries | 
version_date = 'version_date_example' # str | Specifies the version date for the timeseries to create. If this field is not specified, a null version date will be used.  The format for this field is ISO 8601 extended, with optional timezone, i.e., 'format', e.g., '2021-06-10T13:00:00-0700[PST8PDT]'. (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the version-date field (unless otherwise specified). If this field is not specified, the default time zone of UTC shall be used.  Ignored if version-date was specified with offset and timezone. (optional)
create_as_lrts = true # bool | Flag indicating if timeseries should be created as Local Regular Time Series. 'True' or 'False', default is 'False' (optional)
store_rule = cda_client.StoreRule() # StoreRule | The business rule to use when merging the incoming with existing data (optional)
override_protection = true # bool | A flag to ignore the protected data quality when storing data. 'True' or 'False' (optional)

try:
    # Post cwmsData timeseries
    api_instance.post_cwms_data_timeseries(body, version_date=version_date, timezone=timezone, create_as_lrts=create_as_lrts, store_rule=store_rule, override_protection=override_protection)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->post_cwms_data_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeries**](TimeSeries.md)|  | 
 **version_date** | **str**| Specifies the version date for the timeseries to create. If this field is not specified, a null version date will be used.  The format for this field is ISO 8601 extended, with optional timezone, i.e., &#x27;format&#x27;, e.g., &#x27;2021-06-10T13:00:00-0700[PST8PDT]&#x27;. | [optional] 
 **timezone** | **str**| Specifies the time zone of the version-date field (unless otherwise specified). If this field is not specified, the default time zone of UTC shall be used.  Ignored if version-date was specified with offset and timezone. | [optional] 
 **create_as_lrts** | **bool**| Flag indicating if timeseries should be created as Local Regular Time Series. &#x27;True&#x27; or &#x27;False&#x27;, default is &#x27;False&#x27; | [optional] 
 **store_rule** | [**StoreRule**](.md)| The business rule to use when merging the incoming with existing data | [optional] 
 **override_protection** | **bool**| A flag to ignore the protected data quality when storing data. &#x27;True&#x27; or &#x27;False&#x27; | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json;version=2, application/xml;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

