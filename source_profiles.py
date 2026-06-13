# Source Profiles Lookup Table
# Leaning scale: Far-Left | Centre-Left | Centrist | Centre-Right | Far-Right
# Reliability scale: Very High | High | Medium | Low | Very Low
# Note: These classifications reflect commonly observed editorial patterns
# and are inherently subjective. Treat as a starting point, not ground truth.

SOURCE_PROFILES = {

    # ─── INDIAN ENGLISH — DIGITAL NATIVE ───────────────────────────────────────

    "thequint.com": {
        "name": "The Quint",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Quintillion Business Media (Raghav Bahl)",
        "known_for": "Investigative journalism, fact-checking, critical of establishment",
        "covers_india": True,
        "international": False
    },
    "scroll.in": {
        "name": "Scroll",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Scroll Media Inc",
        "known_for": "Long-form journalism, liberal commentary, arts and culture",
        "covers_india": True,
        "international": False
    },
    "thewire.in": {
        "name": "The Wire",
        "leaning": "Left",
        "reliability": "High",
        "ownership": "Foundation for Independent Journalism",
        "known_for": "Investigative reporting, strongly critical of BJP government",
        "covers_india": True,
        "international": False
    },
    "opindia.com": {
        "name": "OpIndia",
        "leaning": "Far-Right",
        "reliability": "Low",
        "ownership": "Medha Vishwakarma / Private",
        "known_for": "Explicitly Hindu nationalist, counter-mainstream narrative",
        "covers_india": True,
        "international": False
    },
    "swarajyamag.com": {
        "name": "Swarajya",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "Kovai Media",
        "known_for": "Pro-BJP, market-friendly, Hindu cultural perspective",
        "covers_india": True,
        "international": False
    },
    "newslaundry.com": {
        "name": "Newslaundry",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Newslaundry Media Pvt Ltd (Abhinandan Sekhri)",
        "known_for": "Media criticism, subscription-based, no ads",
        "covers_india": True,
        "international": False
    },
    "theprintindia.com": {
        "name": "The Print",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "ThePrint (Shekhar Gupta)",
        "known_for": "Policy analysis, defence, national security, centrist commentary",
        "covers_india": True,
        "international": False
    },
    "theprint.in": {
        "name": "The Print",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "ThePrint (Shekhar Gupta)",
        "known_for": "Policy analysis, defence, national security, centrist commentary",
        "covers_india": True,
        "international": False
    },
    "newsminute.com": {
        "name": "The News Minute",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Quintillion Business Media",
        "known_for": "South India focused, LGBTQ+ and minority rights coverage",
        "covers_india": True,
        "international": False
    },
    "thenewsminute.com": {
        "name": "The News Minute",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Quintillion Business Media",
        "known_for": "South India focused, LGBTQ+ and minority rights coverage",
        "covers_india": True,
        "international": False
    },
    "thelogicalindian.com": {
        "name": "The Logical Indian",
        "leaning": "Centre-Left",
        "reliability": "Medium",
        "ownership": "Logical Indian Media",
        "known_for": "Social media driven, positive stories, youth audience",
        "covers_india": True,
        "international": False
    },
    "alt-news.in": {
        "name": "Alt News",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "Pravda Media Foundation (Mohammed Zubair)",
        "known_for": "Fact-checking, debunking misinformation, strongly critical of right-wing fake news",
        "covers_india": True,
        "international": False
    },
    "altnews.in": {
        "name": "Alt News",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "Pravda Media Foundation (Mohammed Zubair)",
        "known_for": "Fact-checking, debunking misinformation",
        "covers_india": True,
        "international": False
    },
    "medianamablog.com": {
        "name": "Medianama",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Medianama",
        "known_for": "Technology policy, digital economy, telecom regulation",
        "covers_india": True,
        "international": False
    },

    # ─── INDIAN ENGLISH — LEGACY PRINT / TV ────────────────────────────────────

    "timesofindia.com": {
        "name": "Times of India",
        "leaning": "Centrist",
        "reliability": "Medium",
        "ownership": "Bennett, Coleman and Co. Ltd (BCCL)",
        "known_for": "Largest English daily, pro-business, clickbait digital presence",
        "covers_india": True,
        "international": False
    },
    "hindustantimes.com": {
        "name": "Hindustan Times",
        "leaning": "Centrist",
        "reliability": "Medium",
        "ownership": "HT Media (KK Birla group)",
        "known_for": "National coverage, corporate friendly, moderate editorial line",
        "covers_india": True,
        "international": False
    },
    "indianexpress.com": {
        "name": "The Indian Express",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Indian Express Group (Viveck Goenka)",
        "known_for": "Investigative journalism, strong editorial independence, respected nationally",
        "covers_india": True,
        "international": False
    },
    "thehindu.com": {
        "name": "The Hindu",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "Kasturi and Sons Ltd",
        "known_for": "Oldest English daily, strong editorial standards, South India base",
        "covers_india": True,
        "international": False
    },
    "deccanherald.com": {
        "name": "Deccan Herald",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "The Printers (Mysore) Private Limited",
        "known_for": "Karnataka focused, independent editorial line",
        "covers_india": True,
        "international": False
    },
    "telegraphindia.com": {
        "name": "The Telegraph India",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "ABP Group",
        "known_for": "Bengal based, frequently critical of BJP and Modi government",
        "covers_india": True,
        "international": False
    },
    "livemint.com": {
        "name": "Mint",
        "leaning": "Centre-Right",
        "reliability": "High",
        "ownership": "HT Media",
        "known_for": "Business and economy focus, market-friendly, pro-reform",
        "covers_india": True,
        "international": False
    },
    "businessstandard.com": {
        "name": "Business Standard",
        "leaning": "Centre-Right",
        "reliability": "High",
        "ownership": "Business Standard Ltd",
        "known_for": "Financial news, policy analysis, pro-market",
        "covers_india": True,
        "international": False
    },
    "economictimes.com": {
        "name": "The Economic Times",
        "leaning": "Centre-Right",
        "reliability": "High",
        "ownership": "Bennett, Coleman and Co. Ltd (BCCL)",
        "known_for": "Business news, markets, pro-liberalisation editorial line",
        "covers_india": True,
        "international": False
    },
    "financialexpress.com": {
        "name": "Financial Express",
        "leaning": "Centre-Right",
        "reliability": "High",
        "ownership": "Indian Express Group",
        "known_for": "Business, economy, markets",
        "covers_india": True,
        "international": False
    },
    "ndtv.com": {
        "name": "NDTV",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Adani Group (acquired 2022)",
        "known_for": "Previously considered liberal, ownership change noted, national TV news",
        "covers_india": True,
        "international": False
    },
    "republicworld.com": {
        "name": "Republic World",
        "leaning": "Far-Right",
        "reliability": "Low",
        "ownership": "ARG Outlier Media (Arnab Goswami)",
        "known_for": "Aggressively pro-BJP, high outrage content, debated journalistic standards",
        "covers_india": True,
        "international": False
    },
    "zeenews.india.com": {
        "name": "Zee News",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "Zee Media Corporation (Subhash Chandra)",
        "known_for": "Pro-establishment, Hindu nationalist tilt, large TV audience",
        "covers_india": True,
        "international": False
    },
    "aajtak.in": {
        "name": "Aaj Tak",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "India Today Group (Aroon Purie)",
        "known_for": "Largest Hindi news channel, sensationalist at times",
        "covers_india": True,
        "international": False
    },
    "indiatoday.in": {
        "name": "India Today",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "India Today Group (Aroon Purie)",
        "known_for": "Weekly magazine legacy, strong investigative unit, centrist editorial",
        "covers_india": True,
        "international": False
    },
    "outlookindia.com": {
        "name": "Outlook India",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Outlook Publishing India Pvt Ltd",
        "known_for": "Long-form journalism, critical of BJP, magazine legacy",
        "covers_india": True,
        "international": False
    },
    "caravanmagazine.in": {
        "name": "The Caravan",
        "leaning": "Left",
        "reliability": "High",
        "ownership": "Delhi Press",
        "known_for": "Long-form investigative journalism, strongly critical of Modi government",
        "covers_india": True,
        "international": False
    },
    "frontline.thehindu.com": {
        "name": "Frontline",
        "leaning": "Left",
        "reliability": "High",
        "ownership": "Kasturi and Sons (The Hindu group)",
        "known_for": "Political analysis, left-leaning commentary, magazine format",
        "covers_india": True,
        "international": False
    },
    "organiser.org": {
        "name": "Organiser",
        "leaning": "Far-Right",
        "reliability": "Low",
        "ownership": "RSS (Rashtriya Swayamsevak Sangh)",
        "known_for": "Officially RSS mouthpiece, Hindu nationalist ideology",
        "covers_india": True,
        "international": False
    },
    "firstpost.com": {
        "name": "Firstpost",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "Network18 (Reliance Industries)",
        "known_for": "Digital news, commentary, pro-establishment tilt since Reliance acquisition",
        "covers_india": True,
        "international": False
    },
    "moneycontrol.com": {
        "name": "Moneycontrol",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Network18 (Reliance Industries)",
        "known_for": "Financial markets, business news, stock market focus",
        "covers_india": True,
        "international": False
    },
    "news18.com": {
        "name": "News18",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "Network18 (Reliance Industries)",
        "known_for": "TV news digital arm, pro-establishment since Reliance acquisition",
        "covers_india": True,
        "international": False
    },
    "wionews.com": {
        "name": "WION",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "Zee Media Corporation",
        "known_for": "International news from Indian perspective, nationalist framing on geopolitics",
        "covers_india": True,
        "international": False
    },
    "thestatesman.com": {
        "name": "The Statesman",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "The Statesman Ltd",
        "known_for": "Kolkata based, one of oldest English dailies, independent editorial",
        "covers_india": True,
        "international": False
    },
    "tribuneindia.com": {
        "name": "The Tribune",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Tribune Trust",
        "known_for": "North India focus, Punjab and Chandigarh base, independent",
        "covers_india": True,
        "international": False
    },
    "deccanchronicle.com": {
        "name": "Deccan Chronicle",
        "leaning": "Centrist",
        "reliability": "Medium",
        "ownership": "Deccan Chronicle Holdings",
        "known_for": "Hyderabad and South India focus",
        "covers_india": True,
        "international": False
    },
    "hindustantimes.com": {
        "name": "Hindustan Times",
        "leaning": "Centrist",
        "reliability": "Medium",
        "ownership": "HT Media",
        "known_for": "National coverage, corporate-friendly editorial line",
        "covers_india": True,
        "international": False
    },
    "newsclick.in": {
        "name": "Newsclick",
        "leaning": "Left",
        "reliability": "Medium",
        "ownership": "PPK Newsclick Studio Pvt Ltd",
        "known_for": "Labour rights, anti-establishment, left-wing commentary",
        "covers_india": True,
        "international": False
    },
    "sabrangindia.in": {
        "name": "Sabrang India",
        "leaning": "Far-Left",
        "reliability": "Medium",
        "ownership": "Sabrang Communications",
        "known_for": "Civil liberties, minority rights, strongly anti-BJP",
        "covers_india": True,
        "international": False
    },
    "catchnews.com": {
        "name": "Catch News",
        "leaning": "Centre-Left",
        "reliability": "Medium",
        "ownership": "Catch Media Pvt Ltd",
        "known_for": "Digital native, youth focused",
        "covers_india": True,
        "international": False
    },
    "theweek.in": {
        "name": "The Week",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Malayala Manorama Group",
        "known_for": "Weekly magazine, national coverage, balanced editorial",
        "covers_india": True,
        "international": False
    },
    "sundayguardianlive.com": {
        "name": "Sunday Guardian",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "M D Nalapat / Private",
        "known_for": "Conservative commentary, geopolitics, pro-establishment",
        "covers_india": True,
        "international": False
    },
    "pgurus.com": {
        "name": "PGurus",
        "leaning": "Far-Right",
        "reliability": "Low",
        "ownership": "Private (NRI funded)",
        "known_for": "Pro-Hindu, anti-Congress, conspiracy adjacent content",
        "covers_india": True,
        "international": False
    },
    "mynation.com": {
        "name": "MyNation",
        "leaning": "Far-Right",
        "reliability": "Very Low",
        "ownership": "Network18 / Zee (disputed)",
        "known_for": "Fake news flagged multiple times, nationalist clickbait",
        "covers_india": True,
        "international": False
    },
    "postcard.news": {
        "name": "Postcard News",
        "leaning": "Far-Right",
        "reliability": "Very Low",
        "ownership": "Mahesh Vikram Hegde",
        "known_for": "Repeatedly flagged for fake news, hardcore Hindu nationalist",
        "covers_india": True,
        "international": False
    },
    "kreately.in": {
        "name": "Kreately",
        "leaning": "Far-Right",
        "reliability": "Very Low",
        "ownership": "Private",
        "known_for": "Pro-BJP propaganda, unverified claims",
        "covers_india": True,
        "international": False
    },

    # ─── INTERNATIONAL — COVERS INDIA SIGNIFICANTLY ────────────────────────────

    "bbc.com": {
        "name": "BBC",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "UK Public Broadcaster",
        "known_for": "Global reach, high editorial standards, India coverage sometimes criticized as Western-centric",
        "covers_india": True,
        "international": True
    },
    "reuters.com": {
        "name": "Reuters",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Thomson Reuters",
        "known_for": "Wire service, factual reporting, minimal editorializing",
        "covers_india": True,
        "international": True
    },
    "apnews.com": {
        "name": "Associated Press",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Non-profit cooperative",
        "known_for": "Wire service, factual, widely syndicated",
        "covers_india": True,
        "international": True
    },
    "aljazeera.com": {
        "name": "Al Jazeera",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Qatar government funded",
        "known_for": "Strong Global South coverage, critical of Indian government on minority issues",
        "covers_india": True,
        "international": True
    },
    "theguardian.com": {
        "name": "The Guardian",
        "leaning": "Left",
        "reliability": "High",
        "ownership": "Scott Trust Limited",
        "known_for": "Progressive journalism, environment, human rights, critical India coverage",
        "covers_india": True,
        "international": True
    },
    "nytimes.com": {
        "name": "The New York Times",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "The New York Times Company",
        "known_for": "Premium journalism, critical of Modi government, Western liberal perspective",
        "covers_india": True,
        "international": True
    },
    "washingtonpost.com": {
        "name": "Washington Post",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "Jeff Bezos / Nash Holdings",
        "known_for": "Investigative journalism, democracy focus, critical of authoritarian governments",
        "covers_india": True,
        "international": True
    },
    "wsj.com": {
        "name": "Wall Street Journal",
        "leaning": "Centre-Right",
        "reliability": "Very High",
        "ownership": "News Corp (Rupert Murdoch)",
        "known_for": "Business focus, conservative editorial board, high reporting standards",
        "covers_india": True,
        "international": True
    },
    "ft.com": {
        "name": "Financial Times",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Nikkei Inc",
        "known_for": "Global business and economy, high editorial standards",
        "covers_india": True,
        "international": True
    },
    "economist.com": {
        "name": "The Economist",
        "leaning": "Centre-Right",
        "reliability": "Very High",
        "ownership": "The Economist Group",
        "known_for": "Liberal economics, pro-market, critical of populism including Modi government",
        "covers_india": True,
        "international": True
    },
    "bloomberg.com": {
        "name": "Bloomberg",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Bloomberg LP (Michael Bloomberg)",
        "known_for": "Financial and business journalism, data-driven",
        "covers_india": True,
        "international": True
    },
    "time.com": {
        "name": "TIME",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Salesforce founder Marc Benioff",
        "known_for": "Long-form journalism, human interest, critical Modi covers",
        "covers_india": True,
        "international": True
    },
    "foreignpolicy.com": {
        "name": "Foreign Policy",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Graham Holdings",
        "known_for": "Geopolitics, international relations, democracy index coverage",
        "covers_india": True,
        "international": True
    },
    "theatlantic.com": {
        "name": "The Atlantic",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Emerson Collective (Laurene Powell Jobs)",
        "known_for": "Long-form journalism, liberal commentary, culture",
        "covers_india": False,
        "international": True
    },
    "dw.com": {
        "name": "Deutsche Welle",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "German public broadcaster",
        "known_for": "International news, human rights focus, covers India extensively",
        "covers_india": True,
        "international": True
    },
    "france24.com": {
        "name": "France 24",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "French public broadcaster",
        "known_for": "International news, multilingual coverage",
        "covers_india": True,
        "international": True
    },
    "scmp.com": {
        "name": "South China Morning Post",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Alibaba Group",
        "known_for": "Asia focus, covers India-China relations extensively",
        "covers_india": True,
        "international": True
    },
    "straitstimes.com": {
        "name": "The Straits Times",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Singapore Press Holdings",
        "known_for": "Southeast Asia focus, covers South Asia including India",
        "covers_india": True,
        "international": True
    },
    "dawn.com": {
        "name": "Dawn",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Pakistan Herald Publications",
        "known_for": "Pakistan's oldest English daily, covers India from Pakistani perspective",
        "covers_india": True,
        "international": True
    },
    "theconversation.com": {
        "name": "The Conversation",
        "leaning": "Centre-Left",
        "reliability": "High",
        "ownership": "Academic non-profit",
        "known_for": "Academic analysis, expert commentary, fact-based",
        "covers_india": True,
        "international": True
    },
    "vox.com": {
        "name": "Vox",
        "leaning": "Left",
        "reliability": "High",
        "ownership": "Vox Media",
        "known_for": "Explanatory journalism, progressive commentary",
        "covers_india": False,
        "international": True
    },
    "vice.com": {
        "name": "Vice",
        "leaning": "Left",
        "reliability": "Medium",
        "ownership": "Vice Media Group",
        "known_for": "Youth focused, investigative, progressive",
        "covers_india": True,
        "international": True
    },
    "buzzfeednews.com": {
        "name": "BuzzFeed News",
        "leaning": "Centre-Left",
        "reliability": "Medium",
        "ownership": "BuzzFeed Inc",
        "known_for": "Viral journalism, some investigative work on India",
        "covers_india": True,
        "international": True
    },
    "axios.com": {
        "name": "Axios",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Axios Media",
        "known_for": "Smart brevity format, policy focus",
        "covers_india": False,
        "international": True
    },
    "propublica.org": {
        "name": "ProPublica",
        "leaning": "Centre-Left",
        "reliability": "Very High",
        "ownership": "Non-profit",
        "known_for": "Investigative journalism, public interest reporting",
        "covers_india": False,
        "international": True
    },

    # ─── WIRE SERVICES / AGGREGATORS ───────────────────────────────────────────

    "pti.in": {
        "name": "Press Trust of India",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Cooperative of Indian newspapers",
        "known_for": "India's largest wire service, factual, wire-style reporting",
        "covers_india": True,
        "international": False
    },
    "ani.in": {
        "name": "ANI",
        "leaning": "Centre-Right",
        "reliability": "Medium",
        "ownership": "Asian News International (Prem Prakash)",
        "known_for": "Wire service, criticized for close ties to government sources",
        "covers_india": True,
        "international": False
    },

    # ─── FACT-CHECKERS ──────────────────────────────────────────────────────────

    "boomlive.in": {
        "name": "BOOM Live",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "Boom Live Media Pvt Ltd",
        "known_for": "Fact-checking, IFCN signatory, covers all political sides",
        "covers_india": True,
        "international": False
    },
    "factchecker.in": {
        "name": "FactChecker",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "IndiaSpend",
        "known_for": "Data-driven fact-checking, government claims verification",
        "covers_india": True,
        "international": False
    },
    "indiaspend.com": {
        "name": "IndiaSpend",
        "leaning": "Centrist",
        "reliability": "Very High",
        "ownership": "IndiaSpend",
        "known_for": "Data journalism, government data analysis",
        "covers_india": True,
        "international": False
    },
    "vishvasnews.com": {
        "name": "Vishvas News",
        "leaning": "Centrist",
        "reliability": "High",
        "ownership": "Jagran New Media",
        "known_for": "Fact-checking in Hindi and English",
        "covers_india": True,
        "international": False
    },

}


def get_source_profile(url: str) -> dict:
    """
    Extract domain from URL and return source profile.
    Returns None if source not found in database.
    """
    import re
    # Extract domain from URL
    domain_match = re.search(r'(?:https?://)?(?:www\.)?([^/\s]+)', url)
    if not domain_match:
        return None

    domain = domain_match.group(1).lower()

    # Direct lookup
    if domain in SOURCE_PROFILES:
        return SOURCE_PROFILES[domain]

    # Try without subdomain
    parts = domain.split('.')
    if len(parts) > 2:
        base_domain = '.'.join(parts[-2:])
        if base_domain in SOURCE_PROFILES:
            return SOURCE_PROFILES[base_domain]

    return None


def get_reliability_color(reliability: str) -> str:
    colors = {
        "Very High": "#6bcb77",
        "High": "#90be6d",
        "Medium": "#ffd93d",
        "Low": "#ff9a3c",
        "Very Low": "#ff6b6b"
    }
    return colors.get(reliability, "#9ca3af")


def get_leaning_color(leaning: str) -> str:
    colors = {
        "Far-Left": "#1a1aff",
        "Left": "#4d79ff",
        "Centre-Left": "#80a8ff",
        "Centrist": "#9ca3af",
        "Centre-Right": "#ff9966",
        "Right": "#ff6633",
        "Far-Right": "#ff0000"
    }
    return colors.get(leaning, "#9ca3af")


if __name__ == "__main__":
    # Quick test
    test_urls = [
        "https://www.thequint.com/news/politics/some-article",
        "https://republicworld.com/india-news/article",
        "https://www.thehindu.com/news/national/article",
        "https://bbc.com/news/world-asia-india",
        "https://www.unknownsource.com/article"
    ]

    for url in test_urls:
        profile = get_source_profile(url)
        if profile:
            print(f"\n{profile['name']}")
            print(f"  Leaning:     {profile['leaning']}")
            print(f"  Reliability: {profile['reliability']}")
            print(f"  Known for:   {profile['known_for']}")
        else:
            print(f"\nSource not found in database for: {url}")
