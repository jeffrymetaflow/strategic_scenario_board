
import streamlit as st

st.set_page_config(page_title="Strategic Scenario Board", layout="wide")
st.title("🧭 Strategic Scenario Planning Board for Investors")

st.markdown("""
### Explore how future global power dynamics and economic fragmentation could shape investment strategy.
Select a scenario below to view detailed analysis and recommended investor actions.
""")

scenario = st.selectbox("Choose a Scenario:", [
    "Pax Americana 2.0",
    "Fragmented Powers",
    "Chinese Century",
    "Cold Tech War"
])

if scenario == "Pax Americana 2.0":
    st.header("🟩 Pax Americana 2.0")
    st.markdown("""
    **Narrative:** The U.S. renews leadership through innovation and alliances. Tariffs normalize. 
    **Indicators:** USD dominance, NATO stability, reintegration of global supply chains.

    **Sectors:** Tech, U.S. Financials, Consumer Discretionary  
    **Strategy:** Long: S&P 500, Treasuries, Growth ETFs  
    **Geo Hotspots:** North America, Western Europe
    """)

elif scenario == "Fragmented Powers":
    st.header("🟥 Fragmented Powers")
    st.markdown("""
    **Narrative:** Multiple global players (U.S., China, India, EU) compete without a clear hegemon. 
    **Indicators:** Bilateral trade, mixed currency trust, regional tech standards.

    **Sectors:** Commodities, Cybersecurity, Logistics  
    **Strategy:** Long: Emerging Markets, Commodities, Infrastructure  
    **Geo Hotspots:** Africa, ASEAN, LATAM
    """)

elif scenario == "Chinese Century":
    st.header("🟦 Chinese Century")
    st.markdown("""
    **Narrative:** China rises as dominant power via trade, currency, and resource control. 
    **Indicators:** RMB oil trade, BRICS+ CBDC, rare earth export dominance.

    **Sectors:** Green tech, Rare Earths, Chinese megacaps  
    **Strategy:** Long: China ETFs, Gold, RMB baskets  
    **Geo Hotspots:** China, Central Asia, Africa
    """)

elif scenario == "Cold Tech War":
    st.header("🟨 Cold Tech War")
    st.markdown("""
    **Narrative:** U.S. and China fully decouple. Parallel systems form. Allies take sides. 
    **Indicators:** Trade bans, rare earth weaponization, FX bifurcation.

    **Sectors:** Defense, Cybersecurity, Reshoring  
    **Strategy:** Long: Gold, U.S. Defense, VIX hedging  
    **Geo Hotspots:** India, Mexico, Taiwan (high risk)
    """)

st.markdown("---")

st.markdown("""
### 🧩 Transition Triggers to Watch:
| Event | Shift Direction |
|-------|-----------------|
| Major U.S. debt crisis | Pax Americana → Cold Tech War |
| Rare earth export bans | Fragmented Powers → Chinese Century |
| BRICS CBDC adoption | Pax Americana → Chinese Century |
| U.S. manufacturing boom | Cold Tech War → Pax Americana 2.0 |
""")
