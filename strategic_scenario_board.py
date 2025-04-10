import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

st.set_page_config(page_title="Strategic Scenario Board", layout="wide")
st.title("🧭 Strategic Scenario Planning Board for Investors")

st.markdown("""
### Explore how future global power dynamics and economic fragmentation could shape investment strategy.
Select a scenario below to view detailed analysis, sentiment overlays, and simulated charts.
""")

# Setup Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

scenario_keywords = {
    "🟩 Pax Americana 2.0": "NATO OR US innovation OR global leadership",
    "🟥 Fragmented Powers": "trade blocs OR multipolar OR regional conflict",
    "🟦 Chinese Century": "China economy OR BRICS OR yuan OR rare earths",
    "🟨 Cold Tech War": "chip bans OR tech decoupling OR cybersecurity OR reshoring"
}

# Use columns to position the quadrant chart
col1, col2 = st.columns([2, 1])

with col2:
    st.subheader("🌍 Scenario Quadrant Map")
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Power Shift vs. Economic Fragmentation", fontsize=9)

    ax.text(-0.5, 0.5, "Pax Americana\n2.0", fontsize=8, color='green', ha='center', va='center')
    ax.text(0.5, 0.5, "Fragmented\nPowers", fontsize=8, color='red', ha='center', va='center')
    ax.text(0.5, -0.5, "Chinese\nCentury", fontsize=8, color='blue', ha='center', va='center')
    ax.text(-0.5, -0.5, "Cold\nTech War", fontsize=8, color='orange', ha='center', va='center')

    ax.text(0.95, -0.05, "China-Centric →", ha='right', fontsize=7)
    ax.text(-0.95, -0.05, "← U.S.-Centric", ha='left', fontsize=7)
    ax.text(-0.05, 0.95, "Integrated ↑", va='bottom', fontsize=7)
    ax.text(-0.05, -0.95, "↓ Decoupled", va='top', fontsize=7)

    st.pyplot(fig)

with col1:
    scenario = st.selectbox("Choose a Scenario:", list(scenario_keywords.keys()))

    st.markdown("---")

    def fetch_news_rss(query):
        url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}"
        feed = feedparser.parse(url)
        return feed.entries[:5]

    def analyze_sentiment(articles):
        results = []
        for entry in articles:
            text = entry.title + ' ' + (entry.get('summary', ''))
            score = sia.polarity_scores(text)['compound']
            results.append((entry.title, score))
        return results

    articles = fetch_news_rss(scenario_keywords[scenario])
    sentiments = analyze_sentiment(articles)

    st.subheader("📰 Real-Time News Sentiment Overlay")
    for title, score in sentiments:
        st.markdown(f"- **{title}** — Sentiment Score: `{score}`")

    st.markdown("---")

    # Existing scenario logic follows below... (no change to rest of the app)
