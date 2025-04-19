import json
import boto3

def lambda_handler(event, context):

    client = boto3.client('ec2')

    response = client.describe_instances(
        InstanceIds=[
            '<instance_id>',
        ]
    )

    PublicDnsName = response["Reservations"][0]["Instances"][0]["NetworkInterfaces"][0]["Association"]["PublicDnsName"]
    private_ip_address = response["Reservations"][0]["Instances"][0]["NetworkInterfaces"][0]["PrivateDnsName"]
    STATE = response["Reservations"][0]["Instances"][0]["State"]["Name"]

    print(
            json.dumps(
                {
                    "PublicDnsName": PublicDnsName,
                    "private_ip_address": private_ip_address,
                    "State": STATE

                },
                indent=4
        )
    )

    def change_new_function():
        pass


