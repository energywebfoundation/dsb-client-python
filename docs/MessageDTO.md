# MessageDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Message id | 
**topic** | **str** | Message topic | 
**payload** | **str** | Any stringified payload like JSON, BASE64 etc | 
**signature** | **str** | Compacted EcdsaSecp256k1Signature2019 | 
**sender** | **str** | Sender of the message | 
**timestamp_nanos** | **float** | Message published timestamp in nanoseconds | 
**correlation_id** | **str** | Correlation id used for message de duplication and correlation purposes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


