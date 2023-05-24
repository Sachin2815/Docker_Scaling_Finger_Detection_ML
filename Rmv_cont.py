import json
import boto3

def lambda_handler(event, context):
    

    # Create an SSM client
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    
    # Specify the command to be run
    command = f"docker rm -f $(docker ps -q | awk 'FNR <= 1 {{print}}')"
    
    # Specify the parameters for the SSM command
    params = {
        "commands": [command]
    }
    
    # Send the command to the EC2 instance using SSM
    response = ssm_client.send_command(
        DocumentName="AWS-RunShellScript",
        InstanceIds=["i-0c132e847dc76d922"],
        TimeoutSeconds=600,
        Parameters=params
    )
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Removed Docker Container!')
    }
