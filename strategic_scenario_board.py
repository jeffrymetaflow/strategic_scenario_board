import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Strategic Scenario Board", layout="wide")
st.title("🧭 Strategic Scenario Planning Board for Investors")

st.markdown("""
### Explore how future global power dynamics and economic fragmentation could shape investment strategy.
Select a scenario below to view detailed analysis and recommended investor actions.
""")

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
    scenario = st.selectbox("Choose a Scenario:", [
        "🟩 Pax Americana 2.0",
        "🟥 Fragmented Powers",
        "🟦 Chinese Century",
        "🟨 Cold Tech War"
    ])

    def plot_scenario_chart(title, x_label, y_label, data_func):
        fig, ax = plt.subplots(figsize=(6, 2))
        x = np.arange(10)
        y = data_func(x)
        ax.plot(x, y, marker='o')
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        st.pyplot(fig)

    if scenario.endswith("Pax Americana 2.0"):
        st.header("🟩 Pax Americana 2.0")
        st.markdown("""
        **Narrative:** The U.S. renews leadership through innovation and alliances. Tariffs normalize. 
        **Indicators:** USD dominance, NATO stability, reintegration of global supply chains.

        **Sectors:** Tech, U.S. Financials, Consumer Discretionary  
        **Strategy:** Long: S&P 500, Treasuries, Growth ETFs  
        **Geo Hotspots:** North America, Western Europe
        """)
        plot_scenario_chart("Projected S&P 500 Growth", "Years Ahead", "Index Value", lambda x: 5000 + 300 * x)

    elif scenario.endswith("Fragmented Powers"):
        st.header("🟥 Fragmented Powers")
        st.markdown("""
        **Narrative:** Multiple global players (U.S., China, India, EU) compete without a clear hegemon. 
        **Indicators:** Bilateral trade, mixed currency trust, regional tech standards.

        **Sectors:** Commodities, Cybersecurity, Logistics  
        **Strategy:** Long: Emerging Markets, Commodities, Infrastructure  
        **Geo Hotspots:** Africa, ASEAN, LATAM
        """)
        plot_scenario_chart("Commodity Volatility Index (Simulated)", "Months", "Volatility", lambda x: 20 + 5 * np.sin(x))

    elif scenario.endswith("Chinese Century"):
        st.header("🟦 Chinese Century")
        st.markdown("""
        **Narrative:** China rises as dominant power via trade, currency, and resource control. 
        **Indicators:** RMB oil trade, BRICS+ CBDC, rare earth export dominance.

        **Sectors:** Green tech, Rare Earths, Chinese megacaps  
        **Strategy:** Long: China ETFs, Gold, RMB baskets  
        **Geo Hotspots:** China, Central Asia, Africa
        """)
        plot_scenario_chart("Rare Earth Index vs. USD", "Years", "Price Index", lambda x: 100 + 20 * x + 15 * np.random.randn(len(x)))

    elif scenario.endswith("Cold Tech War"):
        st.header("🟨 Cold Tech War")
        st.markdown("""
        **Narrative:** U.S. and China fully decouple. Parallel systems form. Allies take sides. 
        **Indicators:** Trade bans, rare earth weaponization, FX bifurcation.

        **Sectors:** Defense, Cybersecurity, Reshoring  
        **Strategy:** Long: Gold, U.S. Defense, VIX hedging  
        **Geo Hotspots:** India, Mexico, Taiwan (high risk)
        """)
        plot_scenario_chart("Defense Budget Growth (Simulated)", "Years", "Spending (B$)", lambda x: 700 + 30 * x)

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
