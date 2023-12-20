# TimeSeries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **datetime** | The requested start time of the data, in ISO-8601 format with offset and timezone (&#x27;yyyy-MM-dd&#x27;T&#x27;HH:mm:ssZ&#x27;[&#x27;VV&#x27;]&#x27;&#x27;) | [optional] 
**end** | **datetime** | The requested end time of the data, in ISO-8601 format with offset and timezone (&#x27;yyyy-MM-dd&#x27;T&#x27;HH:mm:ssZ&#x27;[&#x27;VV&#x27;]&#x27;&#x27;) | [optional] 
**interval** | [**TimeSeriesInterval**](TimeSeriesInterval.md) |  | [optional] 
**interval_offset** | **int** | Offset from top of interval | [optional] 
**name** | **str** | Time-series name | [optional] 
**next_page** | **str** | The cursor to the next page of data; null if there is no more data | [optional] 
**office_id** | **str** | Office ID that owns the time-series | [optional] 
**page** | **str** | The cursor to the current page of data | [optional] 
**page_size** | **int** | The number of records fetched per-page; this may be larger than the number of records actually retrieved | [optional] 
**time_zone** | **str** | Only on 21.1.1 Database. The timezone the Interval Offset is from. | [optional] 
**total** | **int** | The total number of records retrieved; null or not present if not supported or unknown | [optional] 
**units** | **str** | The units of the time series data | 
**value_columns** | [**list[TimeSeriesColumn]**](TimeSeriesColumn.md) |  | [optional] 
**values** | **list[list[object]]** |  | [optional] 
**vertical_datum_info** | [**VerticalDatumInfo**](VerticalDatumInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

