import re
import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from source_profiles import get_source_profile

vader = SentimentIntensityAnalyzer()


def scrape_article(url: str) -> dict:
    """Scrape article title and text from URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # Get title
        title = ""
        if soup.title:
            title = soup.title.get_text().strip()
        elif soup.find("h1"):
            title = soup.find("h1").get_text().strip()

        # Get body text — try article tag first, fall back to paragraphs
        article = soup.find("article")
        if article:
            paragraphs = article.find_all("p")
        else:
            paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        return {"title": title, "text": text, "success": True}

    except Exception as e:
        return {"title": "", "text": "", "success": False, "error": str(e)}


def analyze_sentiment(text: str) -> dict:
    """VADER sentiment analysis."""
    scores = vader.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        label = "Positive"
    elif compound <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "label": label,
        "compound_score": round(compound, 3),
        "positive": round(scores["pos"], 3),
        "negative": round(scores["neg"], 3),
        "neutral": round(scores["neu"], 3),
        "note": "Sentiment accuracy is highest on opinion pieces and editorials. Formal news reports with legal or neutral language may show unexpected scores."
    }


def analyze_subjectivity(text: str) -> dict:
    """TextBlob subjectivity — 0 is factual, 1 is opinion."""
    blob = TextBlob(text)
    score = round(blob.sentiment.subjectivity, 3)

    if score < 0.3:
        label = "Mostly Factual"
    elif score < 0.6:
        label = "Mixed"
    else:
        label = "Highly Opinion-Based"

    return {"label": label, "score": score}


def analyze_emotional_intensity(text: str) -> dict:
    """Detect emotional language using word lists."""
    high_intensity_words = [
        "outrage", "shocking", "devastating", "horrific", "explosive",
        "bombshell", "alarming", "disgraceful", "catastrophic", "furious",
        "disgusting", "scandalous", "shameful", "brutal", "urgent",
        "crisis", "disaster", "chaos", "threat", "danger", "panic"
    ]

    text_lower = text.lower()
    count = sum(1 for word in high_intensity_words if word in text_lower)
    word_count = len(text.split())
    density = count / word_count * 100 if word_count > 0 else 0

    if density > 0.5:
        label = "High"
    elif density > 0.2:
        label = "Medium"
    else:
        label = "Low"

    return {"label": label, "trigger_word_count": count, "density": round(density, 3)}


def analyze_rhetoric(text: str, title: str) -> dict:
    """Detect rhetoric patterns."""
    combined = title + " " + text

    # Scare quotes in headline
    scare_quotes = len(re.findall(r"'[^']{1,30}'", title))

    # Anonymous sourcing
    anonymous_patterns = [
        r"sources? said", r"according to sources",
        r"officials? (who|said)", r"people familiar",
        r"sources? close to", r"unnamed"
    ]
    anonymous_count = sum(
        len(re.findall(p, combined, re.IGNORECASE))
        for p in anonymous_patterns
    )

    # Question framing
    question_count = combined.count("?")

    # Absolute language
    absolute_words = ["always", "never", "every", "all", "none", "completely", "totally", "absolutely"]
    absolute_count = sum(1 for w in absolute_words if w in combined.lower())

    return {
        "scare_quotes_in_headline": scare_quotes,
        "anonymous_sourcing": anonymous_count,
        "question_framing": question_count,
        "absolute_language": absolute_count
    }


def analyze_clickbait(title: str) -> dict:
    """Detect clickbait patterns in headline."""
    clickbait_patterns = [
        r"you won't believe",
        r"this is what",
        r"here's why",
        r"the truth about",
        r"what (they|nobody|no one) (don't|won't)",
        r"\d+ (things|reasons|ways|facts)",
        r"breaking:?",
        r"exclusive:?",
        r"just in:?"
    ]

    title_lower = title.lower()
    matches = sum(1 for p in clickbait_patterns if re.search(p, title_lower))
    has_scare_quotes = bool(re.search(r"'[^']{1,30}'", title))
    has_caps = bool(re.search(r'\b[A-Z]{3,}\b', title))

    score = matches + (1 if has_scare_quotes else 0) + (1 if has_caps else 0)

    if score >= 3:
        label = "High"
    elif score >= 1:
        label = "Medium"
    else:
        label = "Low"

    return {"label": label, "score": score}


def analyze_language_style(text: str) -> dict:
    """Detect language style based on sentence length and vocabulary."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    if not sentences:
        return {"label": "Unknown", "avg_sentence_length": 0}

    avg_length = sum(len(s.split()) for s in sentences) / len(sentences)

    formal_words = ["alleged", "stated", "confirmed", "according", "announced",
                    "reported", "indicated", "acknowledged", "disclosed"]
    informal_words = ["huge", "massive", "crazy", "insane", "epic", "slammed",
                      "blasted", "ripped", "torched", "destroyed"]

    text_lower = text.lower()
    formal_count = sum(1 for w in formal_words if w in text_lower)
    informal_count = sum(1 for w in informal_words if w in text_lower)

    if avg_length > 20 and formal_count > informal_count:
        label = "Formal / Journalistic"
    elif informal_count > formal_count:
        label = "Sensationalist"
    else:
        label = "Informal"

    return {"label": label, "avg_sentence_length": round(avg_length, 1)}


def full_analysis(url: str) -> dict:
    """Run complete analysis on a URL."""

    # Scrape
    scraped = scrape_article(url)
    if not scraped["success"]:
        return {"error": "Could not scrape article. Try pasting the text directly."}

    title = scraped["title"]
    text = scraped["text"]

    if len(text) < 100:
        return {"error": "Article text too short to analyze. The site may be blocking scraping."}

    # Run all analyzers
    return {
        "title": title,
        "url": url,
        "source_profile": get_source_profile(url),
        "sentiment": analyze_sentiment(text),
        "subjectivity": analyze_subjectivity(text),
        "emotional_intensity": analyze_emotional_intensity(text),
        "rhetoric": analyze_rhetoric(text, title),
        "clickbait": analyze_clickbait(title),
        "language_style": analyze_language_style(text),
        "word_count": len(text.split())
    }