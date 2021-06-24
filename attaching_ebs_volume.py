import boto3



def describe_ec2_instance():
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][1]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][1]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)


def describe_volumes():
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_volumes()["Volumes"][1]["VolumeId"])
        return str(resource_ec2.describe_volumes()["Volumes"][1]["VolumeId"])
    except Exception as e:
        print(e)


x=describe_ec2_instance()
print(x)
y = describe_volumes()
print(y)


def attach_ebs_volume_to_instance():
    try:
        print ("attaching ebs volume")
        ec2_client=boto3.client("ec2")
        ec2_client.attach_volume(
            Device = "/dev/sdf",
            InstanceId = x,
            VolumeId = y
        )
    except Exception as e:
        print(e)

attach_ebs_volume_to_instance()