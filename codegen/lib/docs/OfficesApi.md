# cda_client.OfficesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cwms_data_offices**](OfficesApi.md#get_cwms_data_offices) | **GET** /cwms-data/offices | Get cwmsData offices
[**get_cwms_data_offices_with_office**](OfficesApi.md#get_cwms_data_offices_with_office) | **GET** /cwms-data/offices/{office} | Get cwmsData offices with office

# **get_cwms_data_offices**
> OfficeFormatV1 get_cwms_data_offices(format=format, has_data=has_data)

Get cwmsData offices

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.OfficesApi()
format = 'format_example' # str | (Deprecated in favor of Accept header) Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) (optional)
has_data = true # bool | A flag ('True'/'False') When set to true this returns offices that have operational data. Default value is <b>False</b>,. <a href=\"https://github.com/USACE/cwms-data-api/issues/321\" target=\"_blank\">Feature #321</a> (optional)

try:
    # Get cwmsData offices
    api_response = api_instance.get_cwms_data_offices(format=format, has_data=has_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->get_cwms_data_offices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| (Deprecated in favor of Accept header) Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) | [optional] 
 **has_data** | **bool**| A flag (&#x27;True&#x27;/&#x27;False&#x27;) When set to true this returns offices that have operational data. Default value is &lt;b&gt;False&lt;/b&gt;,. &lt;a href&#x3D;\&quot;https://github.com/USACE/cwms-data-api/issues/321\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Feature #321&lt;/a&gt; | [optional] 

### Return type

[**OfficeFormatV1**](OfficeFormatV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, , application/json;version=2, text/tab-separated-values, text/csv, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_offices_with_office**
> OfficeFormatV1 get_cwms_data_offices_with_office(office, format=format)

Get cwmsData offices with office

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cda_client.OfficesApi()
office = 'office_example' # str | The 3 letter office ID you want more information for
format = 'format_example' # str | (Deprecated in favor of Accept header) Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) (optional)

try:
    # Get cwmsData offices with office
    api_response = api_instance.get_cwms_data_offices_with_office(office, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->get_cwms_data_offices_with_office: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office** | **str**| The 3 letter office ID you want more information for | 
 **format** | **str**| (Deprecated in favor of Accept header) Specifies the encoding format of the response. Valid value for the format field for this URI are:  1. tab  2. csv   3. xml  4. json (default) | [optional] 

### Return type

[**OfficeFormatV1**](OfficeFormatV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, , application/json;version=2, text/tab-separated-values, text/csv, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

