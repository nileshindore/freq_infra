import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Repository Name')

args = parser.parse_args()
if args.name:
    client = boto3.client("ecr",region_name='us-east-2update')
    client.create_repository(repositoryName=args.name)
else:
    print("Repository name need to provide.")