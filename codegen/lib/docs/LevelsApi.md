# cda_client.LevelsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_levels_with_level_id**](LevelsApi.md#delete_cwms_data_levels_with_level_id) | **DELETE** /cwms-data/levels/{level-id} | Delete cwmsData levels with levelId
[**delete_cwms_data_specified_levels_with_specified_level_id**](LevelsApi.md#delete_cwms_data_specified_levels_with_specified_level_id) | **DELETE** /cwms-data/specified-levels/{specified-level-id} | Delete cwmsData specifiedLevels with specifiedLevelId
[**get_cwms_data_levels**](LevelsApi.md#get_cwms_data_levels) | **GET** /cwms-data/levels | Get cwmsData levels
[**get_cwms_data_levels_with_level_id**](LevelsApi.md#get_cwms_data_levels_with_level_id) | **GET** /cwms-data/levels/{level-id} | Get cwmsData levels with levelId
[**get_cwms_data_specified_levels**](LevelsApi.md#get_cwms_data_specified_levels) | **GET** /cwms-data/specified-levels | Get cwmsData specifiedLevels
[**patch_cwms_data_levels_with_level_id**](LevelsApi.md#patch_cwms_data_levels_with_level_id) | **PATCH** /cwms-data/levels/{level-id} | Patch cwmsData levels with levelId
[**patch_cwms_data_specified_levels_with_specified_level_id**](LevelsApi.md#patch_cwms_data_specified_levels_with_specified_level_id) | **PATCH** /cwms-data/specified-levels/{specified-level-id} | Patch cwmsData specifiedLevels with specifiedLevelId
[**post_cwms_data_levels**](LevelsApi.md#post_cwms_data_levels) | **POST** /cwms-data/levels | Post cwmsData levels
[**post_cwms_data_specified_levels**](LevelsApi.md#post_cwms_data_specified_levels) | **POST** /cwms-data/specified-levels | Post cwmsData specifiedLevels

# **delete_cwms_data_levels_with_level_id**
> delete_cwms_data_levels_with_level_id(level_id, cascade_delete=cascade_delete, office=office, _date=_date, effective_date=effective_date)

Delete cwmsData levels with levelId

Delete CWMS Location Level

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
api_instance = cda_client.LevelsApi(cda_client.ApiClient(configuration))
level_id = 'level_id_example' # str | Specifies the location level id of the Location Level to be deleted
cascade_delete = true # bool |  (optional)
office = 'office_example' # str | Specifies the owning office of the location level whose data is to be deleted. If this field is not specified, matching location level information will be deleted from all offices. (optional)
_date = '_date_example' # str | Deprecated, use effective-date (optional)
effective_date = 'effective_date_example' # str | Specifies the effective date of the level to be deleted. If not provided will delete all data and reference to the location level. (optional)

try:
    # Delete cwmsData levels with levelId
    api_instance.delete_cwms_data_levels_with_level_id(level_id, cascade_delete=cascade_delete, office=office, _date=_date, effective_date=effective_date)
except ApiException as e:
    print("Exception when calling LevelsApi->delete_cwms_data_levels_with_level_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level_id** | **str**| Specifies the location level id of the Location Level to be deleted | 
 **cascade_delete** | **bool**|  | [optional] 
 **office** | **str**| Specifies the owning office of the location level whose data is to be deleted. If this field is not specified, matching location level information will be deleted from all offices. | [optional] 
 **_date** | **str**| Deprecated, use effective-date | [optional] 
 **effective_date** | **str**| Specifies the effective date of the level to be deleted. If not provided will delete all data and reference to the location level. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cwms_data_specified_levels_with_specified_level_id**
> delete_cwms_data_specified_levels_with_specified_level_id(specified_level_id, office)

Delete cwmsData specifiedLevels with specifiedLevelId

Deletes requested specified level id

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
api_instance = cda_client.LevelsApi(cda_client.ApiClient(configuration))
specified_level_id = 'specified_level_id_example' # str | The specified level id to be deleted
office = 'office_example' # str | Specifies the owning office of the timeseries identifier to be deleted

try:
    # Delete cwmsData specifiedLevels with specifiedLevelId
    api_instance.delete_cwms_data_specified_levels_with_specified_level_id(specified_level_id, office)
except ApiException as e:
    print("Exception when calling LevelsApi->delete_cwms_data_specified_levels_with_specified_level_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specified_level_id** | **str**| The specified level id to be deleted | 
 **office** | **str**| Specifies the owning office of the timeseries identifier to be deleted | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_levels**
> Unit get_cwms_data_levels(name=name, level_id_mask=level_id_mask, office=office, unit=unit, datum=datum, begin=begin, end=end, timezone=timezone, format=format, page=page, page_size=page_size)

Get cwmsData levels

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LevelsApi()
name = 'name_example' # str | Deprecated, use level-id-mask.  (optional)
level_id_mask = 'level_id_mask_example' # str | Specifies the name(s) of the location level(s) whose data is to be included in the response. Uses * for all. (optional)
office = 'office_example' # str | Specifies the owning office of the location level(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. (optional)
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system.  Location level values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location level values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. (optional)
datum = 'datum_example' # str | Specifies the elevation datum of the response. This field affects only elevation location levels. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. (optional)
begin = 'begin_example' # str | Specifies the start of the time window for data to be included in the response. If this field is not specified, any required time window begins 24 hours prior to the specified or default end time. (optional)
end = 'end_example' # str | Specifies the end of the time window for data to be included in the response. If this field is not specified, any required time window ends at the current time (optional)
timezone = 'timezone_example' # str | Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used. (optional)
format = 'format_example' # str | Specifies the encoding format of the response. Requests specifying an Accept header:application/json;version=2 must not include this field. Valid format field values for this URI are:  1.    tab  2.    csv  3.    xml  4.    wml2 (only if name field is specified)  5.    json (default)   (optional)
page = 'page_example' # str | This identifies where in the request you are. This is an opaque value, and can be obtained from the 'next-page' value in the response. (optional)
page_size = 56 # int | How many entries per page returned. Default 100. (optional)

try:
    # Get cwmsData levels
    api_response = api_instance.get_cwms_data_levels(name=name, level_id_mask=level_id_mask, office=office, unit=unit, datum=datum, begin=begin, end=end, timezone=timezone, format=format, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LevelsApi->get_cwms_data_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Deprecated, use level-id-mask.  | [optional] 
 **level_id_mask** | **str**| Specifies the name(s) of the location level(s) whose data is to be included in the response. Uses * for all. | [optional] 
 **office** | **str**| Specifies the owning office of the location level(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. | [optional] 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system.  Location level values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location level values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. | [optional] 
 **datum** | **str**| Specifies the elevation datum of the response. This field affects only elevation location levels. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. | [optional] 
 **begin** | **str**| Specifies the start of the time window for data to be included in the response. If this field is not specified, any required time window begins 24 hours prior to the specified or default end time. | [optional] 
 **end** | **str**| Specifies the end of the time window for data to be included in the response. If this field is not specified, any required time window ends at the current time | [optional] 
 **timezone** | **str**| Specifies the time zone of the values of the begin and end fields (unless otherwise specified), as well as the time zone of any times in the response. If this field is not specified, the default time zone of UTC shall be used. | [optional] 
 **format** | **str**| Specifies the encoding format of the response. Requests specifying an Accept header:application/json;version&#x3D;2 must not include this field. Valid format field values for this URI are:  1.    tab  2.    csv  3.    xml  4.    wml2 (only if name field is specified)  5.    json (default)   | [optional] 
 **page** | **str**| This identifies where in the request you are. This is an opaque value, and can be obtained from the &#x27;next-page&#x27; value in the response. | [optional] 
 **page_size** | **int**| How many entries per page returned. Default 100. | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, , application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_levels_with_level_id**
> LocationLevel get_cwms_data_levels_with_level_id(level_id, office, effective_date, _date=_date, unit=unit)

Get cwmsData levels with levelId

Retrieves requested Location Level

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LevelsApi()
level_id = 'level_id_example' # str | Specifies the requested location level.
office = 'office_example' # str | Specifies the office of the Location Level to be returned
effective_date = 'effective_date_example' # str | Specifies the effective date of Location Level to be returned
_date = '_date_example' # str | Deprecated, use effective-date (optional)
unit = 'unit_example' # str | Desired unit for the values retrieved. (optional)

try:
    # Get cwmsData levels with levelId
    api_response = api_instance.get_cwms_data_levels_with_level_id(level_id, office, effective_date, _date=_date, unit=unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LevelsApi->get_cwms_data_levels_with_level_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level_id** | **str**| Specifies the requested location level. | 
 **office** | **str**| Specifies the office of the Location Level to be returned | 
 **effective_date** | **str**| Specifies the effective date of Location Level to be returned | 
 **_date** | **str**| Deprecated, use effective-date | [optional] 
 **unit** | **str**| Desired unit for the values retrieved. | [optional] 

### Return type

[**LocationLevel**](LocationLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_specified_levels**
> SpecifiedLevel get_cwms_data_specified_levels(office=office, template_id_mask=template_id_mask)

Get cwmsData specifiedLevels

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LevelsApi()
office = 'office_example' # str | Specifies the owning office of the Specified Levels whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. (optional)
template_id_mask = 'template_id_mask_example' # str | Mask that specifies the IDs to be included in the response. If this field is not specified, all specified levels shall be returned. (optional)

try:
    # Get cwmsData specifiedLevels
    api_response = api_instance.get_cwms_data_specified_levels(office=office, template_id_mask=template_id_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LevelsApi->get_cwms_data_specified_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the Specified Levels whose data is to be included in the response. If this field is not specified, matching rating information from all offices shall be returned. | [optional] 
 **template_id_mask** | **str**| Mask that specifies the IDs to be included in the response. If this field is not specified, all specified levels shall be returned. | [optional] 

### Return type

[**SpecifiedLevel**](SpecifiedLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_levels_with_level_id**
> patch_cwms_data_levels_with_level_id(body, level_id, _date=_date, effective_date=effective_date)

Patch cwmsData levels with levelId

Update CWMS Location Level

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
api_instance = cda_client.LevelsApi(cda_client.ApiClient(configuration))
body = cda_client.LocationLevel() # LocationLevel | 
level_id = 'level_id_example' # str | Specifies the location level id of the Location Level to be updated
_date = '_date_example' # str | Deprecated, use effective-date (optional)
effective_date = 'effective_date_example' # str | Specifies the effective date of Location Level that will be updated (optional)

try:
    # Patch cwmsData levels with levelId
    api_instance.patch_cwms_data_levels_with_level_id(body, level_id, _date=_date, effective_date=effective_date)
except ApiException as e:
    print("Exception when calling LevelsApi->patch_cwms_data_levels_with_level_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationLevel**](LocationLevel.md)|  | 
 **level_id** | **str**| Specifies the location level id of the Location Level to be updated | 
 **_date** | **str**| Deprecated, use effective-date | [optional] 
 **effective_date** | **str**| Specifies the effective date of Location Level that will be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_specified_levels_with_specified_level_id**
> patch_cwms_data_specified_levels_with_specified_level_id(specified_level_id, specified_level_id, office)

Patch cwmsData specifiedLevels with specifiedLevelId

Renames the requested specified level id

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
api_instance = cda_client.LevelsApi(cda_client.ApiClient(configuration))
specified_level_id = 'specified_level_id_example' # str | 
specified_level_id = 'specified_level_id_example' # str | The new specified level id.
office = 'office_example' # str | Specifies the owning office of the specified level to be renamed

try:
    # Patch cwmsData specifiedLevels with specifiedLevelId
    api_instance.patch_cwms_data_specified_levels_with_specified_level_id(specified_level_id, specified_level_id, office)
except ApiException as e:
    print("Exception when calling LevelsApi->patch_cwms_data_specified_levels_with_specified_level_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specified_level_id** | **str**|  | 
 **specified_level_id** | **str**| The new specified level id. | 
 **office** | **str**| Specifies the owning office of the specified level to be renamed | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_levels**
> post_cwms_data_levels(body)

Post cwmsData levels

Create new CWMS Location Level

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
api_instance = cda_client.LevelsApi(cda_client.ApiClient(configuration))
body = cda_client.LocationLevel() # LocationLevel | 

try:
    # Post cwmsData levels
    api_instance.post_cwms_data_levels(body)
except ApiException as e:
    print("Exception when calling LevelsApi->post_cwms_data_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationLevel**](LocationLevel.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_specified_levels**
> post_cwms_data_specified_levels(body, fail_if_exists=fail_if_exists)

Post cwmsData specifiedLevels

Create new SpecifiedLevel

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
api_instance = cda_client.LevelsApi(cda_client.ApiClient(configuration))
body = cda_client.SpecifiedLevel() # SpecifiedLevel | 
fail_if_exists = true # bool | Create will fail if provided ID already exists. Default: true (optional)

try:
    # Post cwmsData specifiedLevels
    api_instance.post_cwms_data_specified_levels(body, fail_if_exists=fail_if_exists)
except ApiException as e:
    print("Exception when calling LevelsApi->post_cwms_data_specified_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpecifiedLevel**](SpecifiedLevel.md)|  | 
 **fail_if_exists** | **bool**| Create will fail if provided ID already exists. Default: true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json;version=2
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

