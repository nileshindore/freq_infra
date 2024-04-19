import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Repository Name')

args = parser.parse_args()
if args.name:
    client = boto3.client("ecr")
    client.create_repository(args.name)