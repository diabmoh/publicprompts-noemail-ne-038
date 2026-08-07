# Awesome AI Directories 🚀

A curated list of top AI directories, startup discovery platforms, and submission sites to boost your AI tool's SEO, backlink profile, and user acquisition. Includes live **Domain Rating (DR)** metrics fetched directly via Ahrefs Free API (`https://api.ahrefs.com/v3/public/domain-rating-free`) and founder/team details for outreach.

> **Note:** Domain Rating metrics are retrieved directly from Ahrefs API. Domain Rating by Ahrefs (https://ahrefs.com/).

---

## 📋 Comprehensive Directory List (Sorted A to Z)

| Directory / Platform | Domain Rating (DR) | Founder / Operator | Website URL | Submission Link |
| :--- | :---: | :--- | :--- | :--- |
| **AI Tool Hunt** | **55** | AI Tool Hunt Team | [aitoolhunt.com](https://aitoolhunt.com/) | [Submit Tool](https://aitoolhunt.com/) |
| **AI Tools fyi** | **43** | AI Tools FYI Team | [aitools.fyi](https://aitools.fyi/) | [Submit Tool](https://aitools.fyi/) |
| **AI Website Directory** | **13** | **Kites.Dev LLC** | [aiwebsitedirectory.com](https://aiwebsitedirectory.com/) | [Submit Tool](https://aiwebsitedirectory.com/) |
| **AIxploria** | **56** | AIxploria Team | [aixploria.com](https://www.aixploria.com/) | [Submit Tool](https://www.aixploria.com/submit-ai/) |
| **All Things AI** | **47** | All Things AI Team | [allthingsai.com](https://allthingsai.com/) | [Submit Tool](https://allthingsai.com/submit) |
| **AlternativeTo** | **80** | Ola and Markus | [alternativeto.net](https://alternativeto.net/) | [Add Software](https://alternativeto.net/) |
| **Alternative.me** | **75** | Alternative.me Team | [alternative.me](https://alternative.me/) | [Submit Software](https://alternative.me/) |
| **Best AI Brands** | **11** | Best AI Brands Team | [bestaibrands.com](https://bestaibrands.com/) | [Submit Brand](https://bestaibrands.com/) |
| **BetaList** | **76** | Marc Köhlbrugge | [betalist.com](https://betalist.com/) | [Submit Startup](https://betalist.com/submit) |
| **Capterra** | **91** | Gartner Digital Markets | [capterra.com](https://www.capterra.com/) | [List Product](https://www.capterra.com/) |
| **Easy With AI** | **59** | Easy With AI Team | [easywithai.com](https://easywithai.com/) | [Submit AI Tool](https://easywithai.com/submit-ai-tool/) |
| **Futurepedia** | **72** | Futurepedia LLC | [futurepedia.io](https://www.futurepedia.io/) | [Submit Tool](https://www.futurepedia.io/submit-tool) |
| **Future Tools** | **69** | Matt Wolfe | [futuretools.io](https://www.futuretools.io/) | [Submit Tool](https://www.futuretools.io/submit-a-tool) |
| **G2** | **91** | Godard Abel | [g2.com](https://www.g2.com/) | [List Software](https://sell.g2.com/) |
| **Insidr AI** | **48** | Insidr Team | [insidr.ai](https://www.insidr.ai/) | [Submit Tool](https://www.insidr.ai/submit-ai-tool/) |
| **Launching Next** | **52** | Launching Next Team | [launchingnext.com](https://www.launchingnext.com/) | [Submit Startup](https://www.launchingnext.com/submit/) |
| **Product Hunt** | **91** | Ryan Hoover | [producthunt.com](https://www.producthunt.com/) | [Post Product](https://www.producthunt.com/posts/new) |
| **SaaSHub** | **80** | Stan Bright | [saashub.com](https://www.saashub.com/) | [Submit Software](https://www.saashub.com/submit) |
| **StartupBase** | **70** | StartupBase Team | [startupbase.io](https://startupbase.io/) | [Submit Startup](https://startupbase.io/) |
| **StartupHub.ai** | **61** | StartupHub Team | [startuphub.ai](https://startuphub.ai/) | [Submit Startup](https://startuphub.ai/) |
| **There's An AI For That** | **77** | There's An AI For That SRL | [theresanaiforthat.com](https://theresanaiforthat.com/) | [Submit Tool](https://theresanaiforthat.com/submit/) |
| **Toolify.ai** | **72** | Jehanzaib Ahmed / Saifur Rahman | [toolify.ai](https://www.toolify.ai/) | [Submit Tool](https://www.toolify.ai/submit) |
| **Top AI Tools** | **64** | TopAI Team | [topai.tools](https://topai.tools/) | [Submit Tool](https://topai.tools/submit) |
| **Uneed** | **75** | Thomas Sanlis | [uneed.best](https://www.uneed.best/) | [Submit Product](https://www.uneed.best/submit) |
| **What The AI** | **35** | What The AI Team | [whattheai.tech](https://whattheai.tech/) | [Submit Tool](https://whattheai.tech/submit-ai-tool/) |

---

## 🛠️ How to Fetch DR via Ahrefs Free API

You can verify or update Domain Ratings at any time using Ahrefs public free API endpoint:

```bash
curl -s "https://api.ahrefs.com/v3/public/domain-rating-free?target=aiwebsitedirectory.com"
```

### Python Script (`fetch_dr.py`)

```python
import urllib.request
import json
import time

domains = [
    "aitoolhunt.com",
    "aitools.fyi",
    "aiwebsitedirectory.com",
    "aixploria.com",
    "allthingsai.com",
    "alternative.me",
    "alternativeto.net",
    "bestaibrands.com",
    "betalist.com",
    "capterra.com",
    "easywithai.com",
    "futurepedia.io",
    "futuretools.io",
    "g2.com",
    "insidr.ai",
    "launchingnext.com",
    "producthunt.com",
    "saashub.com",
    "startupbase.io",
    "startuphub.ai",
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
    time.sleep(0.3)
```

---

## 🤝 Contributing

Found a new AI directory or want to update founder information? Feel free to open a Pull Request!
