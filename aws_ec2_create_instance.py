import boto3
import os


def create_ec2_instance():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0ad704c126371a549",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="ec2user",
            SubnetId = "subnet-2604574e",
             SecurityGroupIds = ["sg-0a3d9eac122f18e38"]
        )
    except Exception as e:
        print(e)



def create_ebs_volume():
    try:
        print ("creating ebs volume")
        ec2_client=boto3.client("ec2")
        ec2_client.create_volume(AvailabilityZone='ap-south-1a',
      Size=5,             
      VolumeType='gp2',
      TagSpecifications=[
          {
              'ResourceType': 'volume',
              'Tags': [
                  {
                      'Key': 'Name',
                      'Value': 'Task-6'
                  },
              ]
          },
      ],
     
  )
    except Exception as e:
        print(e)

create_ec2_instance()
create_ebs_volume()



