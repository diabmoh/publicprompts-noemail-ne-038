import urllib.request
import json
import time

domains = [
    "aiwebsitedirectory.com",
    "aixploria.com",
    "allthingsai.com",
    "easywithai.com",
    "futurepedia.io",
    "futuretools.io",
    "insidr.ai",
    "producthunt.com",
    "saashub.com",
    "theresanaiforthat.com",
    "toolify.ai",
    "topai.tools",
    "uneed.best",
    "whattheai.tech"
]

def fetch_ratings():
    results = []
    print("Fetching live Domain Ratings via Ahrefs Free API...\n")
    for domain in sorted(domains):
        url = f"https://api.ahrefs.com/v3/public/domain-rating-free?target={domain}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                dr = data.get("domain_rating", {}).get("domain_rating", 0)
                results.append((domain, dr))
                print(f"[{domain}] DR: {dr}")
        except Exception as e:
            results.append((domain, "N/A"))
            print(f"[{domain}] Error: {e}")
        time.sleep(0.5)
    return results

if __name__ == "__main__":
    fetch_ratings()
