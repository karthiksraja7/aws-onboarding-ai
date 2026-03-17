import json
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

def load_infra():

    data = ""

    files = [
        "infra_data/security_groups.json",
        "infra_data/subnets.json",
        "infra_data/load_balancers.json"
    ]

    for file in files:
        with open(file) as f:
            data += f.read()

    return data


def analyze_onboarding(app_details):

    infra = load_infra()

    with open("prompts/onboarding_prompt.txt") as f:
        template = f.read()

    prompt = template.format(
        infra=infra[:12000],
        app_details=app_details
    )

    response = llm.invoke(prompt)

    return response.content
