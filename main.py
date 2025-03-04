import os, requests
from dotenv import load_dotenv, find_dotenv
from cloudflare import Cloudflare

load_dotenv(find_dotenv())

def get_current_ip():
    return requests.get("https://api.ipify.org").text

client = Cloudflare(
    api_email=os.getenv("API_EMAIL"),
    api_key=os.getenv("API_KEY"),
)
page = client.dns.records.list(
    zone_id=os.getenv("ZONE_ID"),
)
for record in page.result:
    record = record.model_dump()
    if record["name"] == os.getenv("RECORD_NAME"):
        record_id = record["id"]
        record_content = record["content"]
        break

current_ip = get_current_ip()
if record_content != current_ip:
    record_response = client.dns.records.edit(
        dns_record_id=record_id,
        zone_id=os.getenv("ZONE_ID"),
        content=current_ip,
    )