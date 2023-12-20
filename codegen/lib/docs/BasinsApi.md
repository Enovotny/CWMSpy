# cda_client.BasinsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_basins**](BasinsApi.md#get_cwms_data_basins) | **GET** /cwms-data/basins | Get cwmsData basins
[**get_cwms_data_basins_with_basin_id**](BasinsApi.md#get_cwms_data_basins_with_basin_id) | **GET** /cwms-data/basins/{basin-id} | Get cwmsData basins with basinId

# **get_cwms_data_basins**
> Basin get_cwms_data_basins(office=office, unit=unit)

Get cwmsData basins

Returns CWMS Basin Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.BasinsApi()
office = 'office_example' # str | Specifies the owning office of the basin whose data is to be included in the response. If this field is not specified, matching basin information from all offices shall be returned. (optional)
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system. Basin values will be in the default English units for their parameters. (This is default if no value is entered)  2. SI.   Specifies the SI unit system. Basin values will be in the default SI units for their parameters. (optional)

try:
    # Get cwmsData basins
    api_response = api_instance.get_cwms_data_basins(office=office, unit=unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasinsApi->get_cwms_data_basins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| Specifies the owning office of the basin whose data is to be included in the response. If this field is not specified, matching basin information from all offices shall be returned. | [optional] 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system. Basin values will be in the default English units for their parameters. (This is default if no value is entered)  2. SI.   Specifies the SI unit system. Basin values will be in the default SI units for their parameters. | [optional] 

### Return type

[**Basin**](Basin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.named+pg+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_basins_with_basin_id**
> Basin get_cwms_data_basins_with_basin_id(basin_id, office=office, unit=unit)

Get cwmsData basins with basinId

Returns CWMS Basin Data

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.BasinsApi()
basin_id = 'basin_id_example' # str | 
office = 'office_example' # str | Specifies the owning office of the basin whose data is to be included in the response. If this field is not specified, matching basin information from all offices shall be returned. (optional)
unit = 'unit_example' # str | Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system. Basin values will be in the default English units for their parameters. (This is default if no value is entered)  2. SI.   Specifies the SI unit system. Basin values will be in the default SI units for their parameters. (optional)

try:
    # Get cwmsData basins with basinId
    api_response = api_instance.get_cwms_data_basins_with_basin_id(basin_id, office=office, unit=unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasinsApi->get_cwms_data_basins_with_basin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basin_id** | **str**|  | 
 **office** | **str**| Specifies the owning office of the basin whose data is to be included in the response. If this field is not specified, matching basin information from all offices shall be returned. | [optional] 
 **unit** | **str**| Specifies the unit or unit system of the response. Valid values for the unit field are:   1. EN.   Specifies English unit system. Basin values will be in the default English units for their parameters. (This is default if no value is entered)  2. SI.   Specifies the SI unit system. Basin values will be in the default SI units for their parameters. | [optional] 

### Return type

[**Basin**](Basin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.named+pg+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

