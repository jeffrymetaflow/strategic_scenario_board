import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Strategic Scenario Board", layout="wide")
st.title("🧭 Strategic Scenario Planning Board for Investors")

st.markdown("""
### Explore how future global power dynamics and economic fragmentation could shape investment strategy.
Select a scenario below to view detailed analysis and recommended investor actions.
""")

# Display quadrant chart
st.subheader("🌍 Scenario Quadrant Map")
fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Power Shift vs. Economic Fragmentation")

# Add quadrant labels
ax.text(-0.9, 0.9, "Pax Americana 2.0", fontsize=10, color='green')
ax.text(0.5, 0.9, "Fragmented Powers", fontsize=10, color='red')
ax.text(0.5, -0.8, "Chinese Century", fontsize=10, color='blue')
ax.text(-0.9, -0.8, "Cold Tech War", fontsize=10, color='orange')

# Label axes
ax.text(0.9, -0.05, "China-Centric →", ha='right', fontsize=8)
ax.text(-0.9, -0.05, "← U.S.-Centric", ha='left', fontsize=8)
ax.text(-0.05, 0.95, "Integrated ↑", va='bottom', fontsize=8)
ax.text(-0.05, -0.95, "↓ Decoupled", va='top', fontsize=8)

st.pyplot(fig)

scenario = st.selectbox("Choose a Scenario:", [
    "🟩 Pax Americana 2.0",
    "🟥 Fragmented Powers",
    "🟦 Chinese Century",
    "🟨 Cold Tech War"
])

if scenario.endswith("Pax Americana 2.0"):
    st.header("🟩 Pax Americana 2.0")
    st.markdown("""
    **Narrative:** The U.S. renews leadership through innovation and alliances. Tariffs normalize. 
    **Indicators:** USD dominance, NATO stability, reintegration of global supply chains.

    **Sectors:** Tech, U.S. Financials, Consumer Discretionary  
    **Strategy:** Long: S&P 500, Treasuries, Growth ETFs  
    **Geo Hotspots:** North America, Western Europe
    """)

elif scenario.endswith("Fragmented Powers"):
    st.header("🟥 Fragmented Powers")
    st.markdown("""
    **Narrative:** Multiple global players (U.S., China, India, EU) compete without a clear hegemon. 
    **Indicators:** Bilateral trade, mixed currency trust, regional tech standards.

    **Sectors:** Commodities, Cybersecurity, Logistics  
    **Strategy:** Long: Emerging Markets, Commodities, Infrastructure  
    **Geo Hotspots:** Africa, ASEAN, LATAM
    """)

elif scenario.endswith("Chinese Century"):
    st.header("🟦 Chinese Century")
    st.markdown("""
    **Narrative:** China rises as dominant power via trade, currency, and resource control. 
    **Indicators:** RMB oil trade, BRICS+ CBDC, rare earth export dominance.

    **Sectors:** Green tech, Rare Earths, Chinese megacaps  
    **Strategy:** Long: China ETFs, Gold, RMB baskets  
    **Geo Hotspots:** China, Central Asia, Africa
    """)

elif scenario.endswith("Cold Tech War"):
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

