from bs4 import BeautifulSoup
import requests
import re
import urllib.parse
from collections import deque

url = str(input("Enter Target URL To Scan: "))
urls = deque([url])

scraped_urls = set()
emails = set()

count = 0

while len(urls):
    count += 1
    if count == 100:
        break
    url = urls.popleft()
    scraped_urls.add(url)
    
    parts = urllib.parse.urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/') + 1] if '/' in parts.path else url

    print(f"[{count}] Processing {url}")

    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    # Extract emails
    new_emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))
    emails.update(new_emails)

    # Parse links
    soup = BeautifulSoup(response.text, features="lxml")
    for anchor in soup.find_all("a"):
        link = anchor.attrs.get('href', '')
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        if link not in urls and link not in scraped_urls:
            urls.append(link)

except KeyboardInterrupt:
    print("[-] Closing!")
    break

# Output emails
for mail in emails:
    print(mail)
