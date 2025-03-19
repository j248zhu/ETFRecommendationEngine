# Project Title: ETF Recommendation Engine

## Approach and Challenges

Initially, official APIs and web scraping techniques were considered for data collection. However, due to the difficulty of accessing official fund manager website details/ third party APIs and cost considerations (only premium features on third party sources offer ETF details data), a simplier and alternative approach was adopted using OpenAI's GPT-4. 

For a more comprehensive list of ETFs, please see the following: https://etfdb.com

## Key Features

- **Dynamic Prompts**: Tailored prompts based on investor profiles, sector preferences, geographic regions, and asset classes.
- **User-Friendly Interface**: Enables quick and efficient exploration of ETF options.
- **Ethical Compliance**: Ensures adherence to ethical standards in data usage, including not using a webscraper and adherence to robots.txt.

## Future Improvements

- Integration with official APIs for real-time data.
- Enhanced analytics and visualization tools.

Please see the live Streamlit demo at: https://etfrecommendationengine.streamlit.app.
Note that this project was built as a PoC.
