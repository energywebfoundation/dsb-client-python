# LoginReturnDataDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Bearer token | 
**did** | **str** | DID of the Message Broker | 
**address** | **str** | Address of the Message Broker for signature recovery purposes | 
**signature** | **str** | The compact hex ECDSA signature of keccak256(address+did+userDID) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


