import streamlit as st
from openai import OpenAI
from investor_profile import display_investor_profile  # Import the investor profile function
import logging

# Set your OpenAI API key
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def main():
    # Step 1: Show Investor Profile Page First
    selected_profile = display_investor_profile()
    
    if selected_profile:
        st.write(f"You have selected the **{selected_profile}** profile.")
        
        # Step 2: Allow Refinement of ETF Recommendations
        sector_focus = select_sectors()
        region_focus = select_regions()
        asset_class_focus = select_asset_classes()
        
        # Step 3: Fetch Top ETFs Based on Preferences
        st.write("Fetching top ETFs based on your preferences...")
        with st.spinner("Generating ETF recommendations..."):
            etfs_with_links = recommend_etfs_with_links(selected_profile, sector_focus, region_focus, asset_class_focus)
        
        if etfs_with_links:
            st.subheader("Recommended ETFs")
            for etf in etfs_with_links:
                # Display ticker, long-form name, and link
                st.write(f"Ticker: {etf['ticker']}, Name: {etf['name']}, Link: {etf['link']}")

def select_sectors():
    """
    Allows the user to select sectors of interest for ETF recommendations.
    """
    sectors = ["Technology", "Healthcare", "Finance", "Energy", 
               "Consumer Discretionary", "Real Estate", 
               "Industrials", "Utilities", 
               "Materials", "Communication Services"]
    
    selected_sectors = st.multiselect(
        label="Select sectors to focus on (optional):",
        options=sectors,
        help="Choose one or more sectors you'd like your ETFs to focus on."
    )
    
    return selected_sectors

def select_regions():
    """
    Allows the user to select geographic regions of interest for ETF recommendations.
    """
    regions = ["USA", "Canada", "Europe", 
               "Asia", "Rest of the World"]
    
    selected_regions = st.multiselect(
        label="Select geographic regions to focus on (optional):",
        options=regions,
        help="Choose one or more regions you'd like your ETFs to focus on."
    )
    
    return selected_regions

def select_asset_classes():
    """
    Allows the user to select asset classes of interest for ETF recommendations.
    """
    asset_classes = ["Equity", "Bonds", 
                     "Cash & Equivalents"]
    
    selected_asset_classes = st.multiselect(
        label="Select asset classes to focus on (optional):",
        options=asset_classes,
        help="Choose one or more asset classes you'd like your ETFs to focus on."
    )
    
    return selected_asset_classes


# Configure the logger to write to a file or console
logging.basicConfig(level=logging.INFO, filename="skipped_entries.log", filemode="w")

def recommend_etfs_with_links(profile, sectors, regions, asset_classes):
    """
    Uses GPT-4 to recommend ETFs based on the investor profile,
    sector preferences, geographic region preferences, and asset class preferences.
    
    Returns a list of dictionaries containing ticker, name, and link.
    """
    # Build a dynamic prompt based on user inputs
    prompt = f"""
    Recommend the top 10 ETFs suitable for a {profile} investor.
    
    The ETFs should focus on:
      - Sectors: {', '.join(sectors) if sectors else 'No specific sector preference'}
      - Regions: {', '.join(regions) if regions else 'No specific geographic preference'}
      - Asset Classes: {', '.join(asset_classes) if asset_classes else 'No specific asset class preference'}
    
    For each ETF, provide:
      - Ticker symbol
      - Long-form name of the fund
      - Official fund manager's website link
    
    Format your response strictly as:
      Ticker: <ticker>, Name: <long-form name>, Link: <official link>
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    etfs_with_links = response.choices[0].message.content.strip().split("\n")
    
    # Parse GPT-4 output into a structured format
    etf_data = []
    skipped_entries = []  # Keep track of skipped entries for debugging
    
    for etf_info in etfs_with_links:
        if not etf_info.strip():
            continue  # Skip empty lines
        
        parts = etf_info.split(", ")
        
        if len(parts) < 3 or not all(": " in part for part in parts):
            skipped_entries.append(etf_info)  # Log skipped entry
            continue  # Skip malformed lines
        
        try:
            ticker = parts[0].split(": ")[1].strip()
            name = parts[1].split(": ")[1].strip()
            link = parts[2].split(": ")[1].strip()
            etf_data.append({"ticker": ticker, "name": name, "link": link})
        except IndexError:
            skipped_entries.append(etf_info)  # Log skipped entry

    # Log skipped entries internally without showing them in the UI
    if skipped_entries:
        logging.info(f"Skipped Entries: {skipped_entries}")

    return etf_data



if __name__ == "__main__":
    main()
