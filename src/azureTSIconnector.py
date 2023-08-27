from azure.identity import DefaultAzureCredential
from azure.mgmt.timeseriesinsights import TimeSeriesInsightsClient
from azure.mgmt.timeseriesinsights.models import EventSourceCreateOrUpdateParameters, EventSourceResource

# Replace with your own values
subscription_id = 'your-subscription-id'
resource_group_name = 'your-resource-group-name'
environment_fqdn = 'your-environment-fqdn'
event_source_name = 'your-event-source-name'

credential = DefaultAzureCredential()

client = TimeSeriesInsightsClient(credential, subscription_id)

event_source_resource = EventSourceResource(
    kind='Microsoft.TimeSeriesInsights/environments/eventSources',
    location='westus2',
    tags={},
    properties={
        'description': 'Python SDK event source',
        'type': 'EventHub',
        'provisioningState': 'Succeeded',
        'eventSourceResourceId': '/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.EventHub/namespaces/{2}/eventhubs/{3}'.format(subscription_id, resource_group_name, event_hub_namespace_name, event_hub_name),
        'localTimestamp': {
            'propertyName': 'timestamp'
        },
        'timestampPropertyName': 'timestamp'
    }
)

event_source_create_or_update_parameters = EventSourceCreateOrUpdateParameters(
    event_source_resource=event_source_resource
)

client.event_sources.create_or_update(
    resource_group_name=resource_group_name,
    environment_name=environment_fqdn,
    event_source_name=event_source_name,
    parameters=event_source_create_or_update_parameters
)
