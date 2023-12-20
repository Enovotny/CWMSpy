# cda_client.LocationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_locations_with_location_id**](LocationsApi.md#delete_cwms_data_locations_with_location_id) | **DELETE** /cwms-data/locations/{location-id} | Delete cwmsData locations with locationId
[**get_cwms_data_locations**](LocationsApi.md#get_cwms_data_locations) | **GET** /cwms-data/locations | Get cwmsData locations
[**get_cwms_data_locations_with_location_id**](LocationsApi.md#get_cwms_data_locations_with_location_id) | **GET** /cwms-data/locations/{location-id} | Get cwmsData locations with locationId
[**patch_cwms_data_locations_with_location_id**](LocationsApi.md#patch_cwms_data_locations_with_location_id) | **PATCH** /cwms-data/locations/{location-id} | Patch cwmsData locations with locationId
[**post_cwms_data_locations**](LocationsApi.md#post_cwms_data_locations) | **POST** /cwms-data/locations | Post cwmsData locations

# **delete_cwms_data_locations_with_location_id**
> delete_cwms_data_locations_with_location_id(location_id, office=office)

Delete cwmsData locations with locationId

Delete CWMS Location

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
api_instance = cda_client.LocationsApi(cda_client.ApiClient(configuration))
location_id = 'location_id_example' # str | 
office = 'office_example' # str | Specifies the owning office of the location whose data is to be deleted. If this field is not specified, matching location information will be deleted from all offices. (optional)

try:
    # Delete cwmsData locations with locationId
    api_instance.delete_cwms_data_locations_with_location_id(location_id, office=office)
except ApiException as e:
    print("Exception when calling LocationsApi->delete_cwms_data_locations_with_location_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **office** | **str**| Specifies the owning office of the location whose data is to be deleted. If this field is not specified, matching location information will be deleted from all offices. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_locations**
> Unit get_cwms_data_locations(names=names, office=office, unit=unit, datum=datum, format=format)

Get cwmsData locations

Returns CWMS Location Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LocationsApi()
names = 'names_example' # str | Specifies the name(s) of the location(s) whose data is to be included in the response (optional)
office = 'office_example' # str | Specifies the owning office of the location level(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. (optional)
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system.  Location level values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location level values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. (optional)
datum = 'datum_example' # str | Specifies the elevation datum of the response. This field affects only elevation location levels. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. (optional)
format = 'format_example' # str | Specifies the encoding format of the response. Valid values for the format field for this URI are:  1.    tab  2.    csv  3.    xml  4.  wml2 (only if name field is specified)  5.    json (default) 6.    geojson (optional)

try:
    # Get cwmsData locations
    api_response = api_instance.get_cwms_data_locations(names=names, office=office, unit=unit, datum=datum, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_cwms_data_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **str**| Specifies the name(s) of the location(s) whose data is to be included in the response | [optional] 
 **office** | **str**| Specifies the owning office of the location level(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. | [optional] 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system.  Location level values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location level values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. | [optional] 
 **datum** | **str**| Specifies the elevation datum of the response. This field affects only elevation location levels. Valid values for this field are:  1. NAVD88.  The elevation values will in the specified or default units above the NAVD-88 datum.  2. NGVD29.  The elevation values will be in the specified or default units above the NGVD-29 datum. | [optional] 
 **format** | **str**| Specifies the encoding format of the response. Valid values for the format field for this URI are:  1.    tab  2.    csv  3.    xml  4.  wml2 (only if name field is specified)  5.    json (default) 6.    geojson | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/tab-separated-values, text/csv, application/xml, application/vnd.opengis.waterml+xml, application/geo+json, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_locations_with_location_id**
> Location get_cwms_data_locations_with_location_id(location_id, office, unit=unit)

Get cwmsData locations with locationId

Returns CWMS Location Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.LocationsApi()
location_id = 'location_id_example' # str | 
office = 'office_example' # str | Specifies the owning office of the location level(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned.
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system.  Location values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. (optional)

try:
    # Get cwmsData locations with locationId
    api_response = api_instance.get_cwms_data_locations_with_location_id(location_id, office, unit=unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_cwms_data_locations_with_location_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **office** | **str**| Specifies the owning office of the location level(s) whose data is to be included in the response. If this field is not specified, matching location level information from all offices shall be returned. | 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system.  Location values will be in the default English units for their parameters.  2. SI.   Specifies the SI unit system.  Location values will be in the default SI units for their parameters.  3. Other. Any unit returned in the response to the units URI request that is appropriate for the requested parameters. | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cwms_data_locations_with_location_id**
> patch_cwms_data_locations_with_location_id(body, location_id)

Patch cwmsData locations with locationId

Update CWMS Location

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
api_instance = cda_client.LocationsApi(cda_client.ApiClient(configuration))
body = cda_client.Location() # Location | 
location_id = 'location_id_example' # str | 

try:
    # Patch cwmsData locations with locationId
    api_instance.patch_cwms_data_locations_with_location_id(body, location_id)
except ApiException as e:
    print("Exception when calling LocationsApi->patch_cwms_data_locations_with_location_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Location**](Location.md)|  | 
 **location_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_locations**
> post_cwms_data_locations(body)

Post cwmsData locations

Create new CWMS Location

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
api_instance = cda_client.LocationsApi(cda_client.ApiClient(configuration))
body = cda_client.Location() # Location | 

try:
    # Post cwmsData locations
    api_instance.post_cwms_data_locations(body)
except ApiException as e:
    print("Exception when calling LocationsApi->post_cwms_data_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Location**](Location.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

