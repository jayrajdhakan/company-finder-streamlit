import streamlit as st
from scraper.selenium_scraper import scrape_companies
from config.data import cities, company_types
import time
from io import BytesIO

# st.set_page_config(layout="wide")

st.title("Gujarat Company Finder")

city = st.selectbox("Select City", cities)
company_type = st.selectbox("Select Company Type", company_types)

col1, col2 = st.columns([1, 1])

# Find Companies Button
if col1.button("Find Companies"):

    with st.spinner("Scraping companies..."):
        df = scrape_companies(city, company_type)

    # Save dataframe in session state
    st.session_state["companies_df"] = df

    success_msg = st.empty()
    success_msg.success("Results Found")
    time.sleep(3)
    success_msg.empty()


# Export CSV Button
if "companies_df" in st.session_state:

    buffer = BytesIO()

    df = st.session_state["companies_df"]
    df.to_excel(buffer, index=False, engine="openpyxl")

    col2.download_button(
        label="Export to Excel",
        data=buffer,
        file_name="companies.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    df = st.session_state["companies_df"]

    st.write("### Company Details")

    for i, row in df.iterrows():

        st.subheader(row["Company Name"])

        st.write("📍 Address:", row["Address"])
        st.write("📞 Phone:", row["Phone"])

        st.markdown(f"[Open in Google Maps]({row['Google Maps Link']})")

        st.write("---")
