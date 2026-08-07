# Top AI Directory Founders List (Sorted A-Z)

A curated list of top AI directories and submission platforms, including Domain Rating (DR) fetched live via Ahrefs free API endpoint (`https://api.ahrefs.com/v3/public/domain-rating-free`) and founder details for outreach and site submissions.

> **Note:** Domain Rating metrics are retrieved directly from Ahrefs API. Domain Rating by Ahrefs (https://ahrefs.com/).

---

## Directory List (Sorted A-Z by Directory / Platform Name)

| Directory / Platform | Domain Rating (DR) | Founder / Team | Website URL | Submission Link |
| :--- | :---: | :--- | :--- | :--- |
| **AI Website Directory** | **13** | **Jabed Bhuiyan** | [aiwebsitedirectory.com](https://aiwebsitedirectory.com/) | [Submit Tool](https://aiwebsitedirectory.com/) |
| **AIxploria** | **56** | AIxploria Team | [aixploria.com](https://www.aixploria.com/) | [Submit Tool](https://www.aixploria.com/submit-ai/) |
| **All Things AI** | **47** | All Things AI Team | [allthingsai.com](https://allthingsai.com/) | [Submit Tool](https://allthingsai.com/submit) |
| **Easy With AI** | **59** | Easy With AI Team | [easywithai.com](https://easywithai.com/) | [Submit Tool](https://easywithai.com/submit-ai-tool/) |
| **Futurepedia** | **72** | Futurepedia LLC | [futurepedia.io](https://www.futurepedia.io/) | [Submit Tool](https://www.futurepedia.io/submit-tool) |
| **Future Tools** | **69** | Matt Wolfe | [futuretools.io](https://www.futuretools.io/) | [Submit Tool](https://www.futuretools.io/submit-a-tool) |
| **Insidr AI** | **48** | Insidr Team | [insidr.ai](https://www.insidr.ai/) | [Submit Tool](https://www.insidr.ai/submit-ai-tool/) |
| **Product Hunt** | **91** | Ryan Hoover | [producthunt.com](https://www.producthunt.com/) | [Post Product](https://www.producthunt.com/posts/new) |
| **SaaSHub** | **80** | Stan Bright | [saashub.com](https://www.saashub.com/) | [Submit Software](https://www.saashub.com/submit) |
| **There's An AI For That** | **77** | There's An AI For That SRL | [theresanaiforthat.com](https://theresanaiforthat.com/) | [Submit Tool](https://theresanaiforthat.com/submit/) |
| **Toolify.ai** | **72** | Jehanzaib Ahmed / Saifur Rahman | [toolify.ai](https://www.toolify.ai/) | [Submit Tool](https://www.toolify.ai/submit) |
| **Top AI Tools** | **64** | TopAI Team | [topai.tools](https://topai.tools/) | [Submit Tool](https://topai.tools/submit) |
| **Uneed** | **75** | Thomas Sanlis | [uneed.best](https://www.uneed.best/) | [Submit Product](https://www.uneed.best/submit) |
| **What The AI** | **35** | What The AI Team | [whattheai.tech](https://whattheai.tech/) | [Submit Tool](https://whattheai.tech/submit-ai-tool/) |

---

## How to Fetch DR via Ahrefs Free API

You can verify or update Domain Ratings at any time using Ahrefs public free API endpoint:

```bash
curl -s "https://api.ahrefs.com/v3/public/domain-rating-free?target=aiwebsitedirectory.com"
```

### Python Script Example (`fetch_dr.py`)

```python
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

print(f"{'Domain':<25} | {'Domain Rating (DR)':<18}")
print("-" * 46)

for domain in sorted(domains):
    url = f"https://api.ahrefs.com/v3/public/domain-rating-free?target={domain}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            dr = data.get("domain_rating", {}).get("domain_rating", 0)
            print(f"{domain:<25} | {dr:<18}")
    except Exception as e:
        print(f"{domain:<25} | Error: {e}")
    time.sleep(0.5)
```
