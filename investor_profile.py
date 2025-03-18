import streamlit as st

# Define investment profiles
investment_profiles = {
    "Conservative": {
        "Focus": "Capital preservation with predictable income.",
        "Risk Tolerance": "Low, suitable for short investment horizons.",
        "Investments": "Cash equivalents, bonds, and low-volatility assets."
    },
    "Moderate": {
        "Focus": "Stability with some capital growth over time.",
        "Risk Tolerance": "Moderate, balancing income and growth.",
        "Investments": "A mix of fixed income and equities."
    },
    "Balanced": {
        "Focus": "Long-term capital growth and regular income.",
        "Risk Tolerance": "Accepts moderate volatility for stable returns.",
        "Investments": "Diversified portfolios combining equities and bonds."
    },
    "Growth": {
        "Focus": "Long-term capital appreciation with some income.",
        "Risk Tolerance": "High, tolerating significant volatility.",
        "Investments": "Equities dominate, but not exclusively."
    },
    "Aggressive": {
        "Focus": "Maximizing long-term returns.",
        "Risk Tolerance": "Very high, accepting substantial fluctuations in value.",
        "Investments": "Primarily equity-heavy portfolios."
    }
}

def display_investor_profile():
    """
    Displays the UI for selecting an investment profile and returns the selected profile.
    """
    st.title("Investment Profile Selector")
    st.write("Select your investment profile to get started.")

    # User selects an initial investment profile
    selected_profile = st.selectbox(
        label="Choose your investment profile:",
        options=list(investment_profiles.keys())
    )

    # Display details of the selected profile
    if selected_profile:
        st.subheader(f"Selected Profile: {selected_profile}")
        st.write(f"**Focus:** {investment_profiles[selected_profile]['Focus']}")
        st.write(f"**Risk Tolerance:** {investment_profiles[selected_profile]['Risk Tolerance']}")
        st.write(f"**Investments:** {investment_profiles[selected_profile]['Investments']}")

    return selected_profile
