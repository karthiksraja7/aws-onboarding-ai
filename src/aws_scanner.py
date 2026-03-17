import boto3
import json
import os
from dotenv import load_dotenv
load_dotenv()
def collect_infra():

    ec2 = boto3.client("ec2")
    elb = boto3.client("elbv2")

    # Security Groups
    sg = ec2.describe_security_groups()

    # Subnets
    subnets = ec2.describe_subnets()

    # Load balancers
    lbs = elb.describe_load_balancers()

    os.makedirs("infra_data", exist_ok=True)

    with open("infra_data/security_groups.json", "w") as f:
        json.dump(sg, f, indent=2)

    with open("infra_data/subnets.json", "w") as f:
        json.dump(subnets, f, indent=2)

    with open("infra_data/load_balancers.json", "w") as f:
        json.dump(lbs, f, indent=2)

    print("Infrastructure data collected successfully")

if __name__ == "__main__":
    collect_infra()
