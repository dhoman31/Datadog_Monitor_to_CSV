"""
Get all monitor details returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
import pandas as pd 

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors()

    monitor_items = {"Monitor Name": [], "Monitor ID": [], "Creator Name": [], "Creator Email": [], "Created": [], "Query": [], "Message": [], "Tags": []}
    # loop through each value
    for each in response:
        mon_name = str(each["name"])
        mon_id = str(each["id"])
        creator_name = str(each["creator"]["name"])
        creator_email = str(each['creator']['email'])
        created = str(each["created"])
        query = str(each["query"])
        message = str(each["message"])
        tags = ','.join(each["tags"])

        monitor_items["Monitor Name"].append(mon_name)
        monitor_items["Monitor ID"].append(mon_id)
        monitor_items["Creator Name"].append(creator_name)
        monitor_items["Creator Email"].append(creator_email)
        monitor_items["Created"].append(created)
        monitor_items["Query"].append(query)
        monitor_items["Message"].append(message)
        monitor_items["Tags"].append(tags)
    df = pd.DataFrame(monitor_items)
    
    # push to a CSV
    df.to_csv('monitors_list.csv', index=False)