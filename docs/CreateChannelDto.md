# CreateChannelDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqcn** | **str** | Fully Qualified Channel Name (fcqn) | 
**topics** | **[str]** | Array of topic objects that determines topics for messages. | [optional] 
**admins** | **[str]** | Array of DIDs that have permission to edit the channel. If it is omitted, creator of the channel will be the default admin. | [optional] 
**publishers** | **[str]** | A mixed array of DIDs and roles that have permission to publish messages to the channel. If it is omitted, any user with \&quot;user\&quot; role can publish messages to the channel. | [optional] 
**subscribers** | **[str]** | A mixed array of DIDs and roles that have permission to subscribe to the channel. If it is omitted, any user with \&quot;user\&quot; role can subscribe to the channel. | [optional] 
**max_msg_age** | **float** | Maximum age of any message in the channel, expressed in nanoseconds. | [optional] 
**max_msg_size** | **float** | Maximum size of any message in the channel, expressed in bytes. Maximum value is 8388608 bytes (8Mb) | [optional]  if omitted the server will use the default value of 1048576
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


