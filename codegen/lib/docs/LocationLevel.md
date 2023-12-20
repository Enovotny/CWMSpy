# LocationLevel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **str** | Owning office of object. | 
**location_level_id** | **str** | Name of the location level | 
**seasonal_time_series_id** | **str** | Timeseries ID (e.g. from the times series catalog) to use as the location level. Mutually exclusive with seasonalValues and siParameterUnitsConstantValue | [optional] 
**seasonal_values** | [**list[SeasonalValueBean]**](SeasonalValueBean.md) | List of Repeating seasonal values. The values repeater after the specified interval. A yearly interval seasonable could have 12 different values, one for each month for example. Mutually exclusive with seasonalTimeSeriesId and siParameterUnitsConstantValue | [optional] 
**specified_level_id** | **str** | Generic name of this location level. Common names are &#x27;Top of Dam&#x27;, &#x27;Streambed&#x27;, &#x27;Bottom of Dam&#x27;. | [optional] 
**parameter_type_id** | **str** | To indicate if single or aggregate value | [optional] 
**parameter_id** | **str** | Data Type such as Stage, Elevation, or others. | [optional] 
**constant_value** | **float** | Single value for this location level. Mutually exclusive with seasonableTimeSeriesId and seasonValues. | [optional] 
**level_units_id** | **str** | Units the provided levels are in | [optional] 
**level_date** | **datetime** | The date/time at which this location level configuration takes effect. | [optional] 
**level_comment** | **str** |  | [optional] 
**interval_origin** | **datetime** | The start point of provided seasonal values | [optional] 
**interval_months** | **int** |  | [optional] 
**interval_minutes** | **int** |  | [optional] 
**interpolate_string** | **str** | Indicating whether or not to interpolate between seasonal values. | [optional] 
**duration_id** | **str** | 0 if parameterTypeId is Inst. Otherwise duration indicating the time window of the aggregate value. | [optional] 
**attribute_value** | **float** |  | [optional] 
**attribute_units_id** | **str** |  | [optional] 
**attribute_parameter_type_id** | **str** |  | [optional] 
**attribute_parameter_id** | **str** |  | [optional] 
**attribute_duration_id** | **str** |  | [optional] 
**attribute_comment** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

