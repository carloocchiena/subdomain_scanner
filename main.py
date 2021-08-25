import requests

domain = "google.com"

with open ("subdomains.txt", encoding="utf-8") as f:
    content = f.read()
    
subdomains = content.splitlines()

discovered_subdomains = list()

for subdomain in subdomains:
    url = f"https://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print (">>> Discovered subdomain:", url)
        discovered_subdomains.append(url)
