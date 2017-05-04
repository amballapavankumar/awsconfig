import boto3
import json
import sys
from time import sleep

ec2client=boto3.client('ec2')
ec2 = boto3.resource('ec2')
response = ec2client.describe_instances(Filters=[{'Name':'tag:Owner', 'Values':["sonetel"]},{'Name':'instance-state-name','Values':["running","pending","stopping","stopped"]}])
for r in response["Reservations"]:
	for i in r["Instances"]:
			instop=ec2client.terminate_instances(InstanceIds=[i["InstanceId"]])['TerminatingInstances'][0]['CurrentState']['Name']
			while instop in ('shutting-down'):
				sleep(5)
				instop= ec2client.describe_instances(InstanceIds=[i["InstanceId"]])["Reservations"][0]["Instances"][0]["State"]["Name"]
			else:
				print "Instance got Terminated!!!"
				instance = ec2.create_instances(ImageId="ami-c58c1dd3",KeyName="pavan",MinCount=1, MaxCount=1,InstanceType="t2.micro",TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{'Key': 'Owner', 'Value': 'sonetel'},{'Key': 'Name', 'Value': 'temp-instance'} ] } ])
				print "New instance creation started"
				for inst in instance:
					with open('data.json', 'w') as outfile:
						json.dump({"InstanceId":inst.id}, outfile)

if  response["Reservations"]==[]:
	instance = ec2.create_instances(ImageId="ami-c58c1dd3",KeyName="pavan",MinCount=1, MaxCount=1,InstanceType="t2.micro",TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{'Key': 'Owner', 'Value': 'sonetel'},{'Key': 'Name', 'Value': 'temp-instance'} ] } ])
	sleep(10)
	print "New instance creation started"
	for inst in instance:
		with open('data.json', 'w') as outfile:
			json.dump({"InstanceId":inst.id}, outfile)


