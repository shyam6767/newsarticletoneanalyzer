import { useState } from "react";
import "./App.css";

const API = "http://localhost:5000/analyze";

function ScoreBar({ value, max = 1 }) {
  const pct = Math.min((value / max) * 100, 100);
  return (
    <div className="bar-bg">
      <div className="bar-fill" style={{ width: `${pct}%` }} />
    </div>
  );
}

function Badge({ label, type }) {
  return <span className={`badge badge-${type}`}>{label}</span>;
}

function getBadgeType(label) {
  const map = {
    "Positive": "positive",
    "Negative": "negative",
    "Neutral": "neutral",
    "High": "high",
    "Medium": "medium",
    "Low": "low",
    "Mostly Factual": "positive",
    "Mixed": "medium",
    "Highly Opinion-Based": "high",
    "Formal / Journalistic": "positive",
    "Sensationalist": "high",
    "Informal": "medium",
  };
  return map[label] || "neutral";
}

function Section({ title, children }) {
  return (
    <div className="section">
      <h3>{title}</h3>
      {children}
    </div>
  );
}

function Row({ label, value, children }) {
  return (
    <div className="row">
      <span className="row-label">{label}</span>
      <span className="row-value">{value || children}</span>
    </div>
  );
}

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyze = async () => {
    if (!url.trim()) return;
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const data = await res.json();
      if (data.error) {
        setError(data.error);
      } else {
        setResult(data);
      }
    } catch (e) {
      setError("Could not connect to server.");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="container">
        <h1>News Article Sentiment Analyzer</h1>
        <p className="subtitle">Paste a news article URL to analyze its tone, sentiment, and rhetoric patterns.</p>

        <div className="input-row">
          <input
            type="text"
            placeholder="https://www.thehindu.com/news/..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && analyze()}
          />
          <button onClick={analyze} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze"}
          </button>
        </div>

        {error && <p className="error">{error}</p>}

        {result && (
          <div className="results">

            <div className="article-header">
              <p className="article-title">{result.title}</p>
              <a href={result.url} target="_blank" rel="noreferrer">{result.url}</a>
            </div>

            {result.source_profile && (
              <Section title="Source Profile">
                <Row label="Name" value={result.source_profile.name} />
                <Row label="Reliability" value={result.source_profile.reliability} />
                <Row label="Known For" value={result.source_profile.known_for} />
                {result.source_profile.international && (
                  <p className="note">International source — India coverage may lack local context.</p>
                )}
              </Section>
            )}

            {!result.source_profile && (
              <Section title="Source Profile">
                <p className="note">Source not found in database.</p>
              </Section>
            )}

            <Section title="Sentiment">
              <Row label="Overall">
                <Badge label={result.sentiment.label} type={getBadgeType(result.sentiment.label)} />
              </Row>
              <Row label="Positive Score" value={result.sentiment.positive} />
              <Row label="Negative Score" value={result.sentiment.negative} />
              <Row label="Compound Score" value={result.sentiment.compound_score} />
              <ScoreBar value={Math.abs(result.sentiment.compound_score)} max={1} />
              <p className="note">{result.sentiment.note}</p>
            </Section>

            <Section title="Subjectivity">
              <Row label="Classification">
                <Badge label={result.subjectivity.label} type={getBadgeType(result.subjectivity.label)} />
              </Row>
              <Row label="Score (0 = Factual, 1 = Opinion)" value={result.subjectivity.score} />
              <ScoreBar value={result.subjectivity.score} max={1} />
            </Section>

            <Section title="Emotional Intensity">
              <Row label="Level">
                <Badge label={result.emotional_intensity.label} type={getBadgeType(result.emotional_intensity.label)} />
              </Row>
              <Row label="Trigger Words Found" value={result.emotional_intensity.trigger_word_count} />
            </Section>

            <Section title="Language Style">
              <Row label="Style">
                <Badge label={result.language_style.label} type={getBadgeType(result.language_style.label)} />
              </Row>
              <Row label="Avg Sentence Length" value={`${result.language_style.avg_sentence_length} words`} />
            </Section>

            <Section title="Clickbait Detection">
              <Row label="Level">
                <Badge label={result.clickbait.label} type={getBadgeType(result.clickbait.label)} />
              </Row>
            </Section>

            <Section title="Rhetoric Markers">
              <Row label="Scare Quotes in Headline" value={result.rhetoric.scare_quotes_in_headline} />
              <Row label="Anonymous Sourcing" value={result.rhetoric.anonymous_sourcing} />
              <Row label="Question Framing" value={result.rhetoric.question_framing} />
              <Row label="Absolute Language" value={result.rhetoric.absolute_language} />
            </Section>

            <p className="word-count">Word count: {result.word_count}</p>

          </div>
        )}
      </div>
    </div>
  );
}

export default App;