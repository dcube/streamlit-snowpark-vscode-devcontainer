"""..."""
import streamlit as st
from package.snowpark_utils import snowpark_session

if __name__ == '__main__':
    # set page config for this app
    st.set_page_config(layout="wide")

    # create or get snowpark session (singleton)
    snowpark_session = snowpark_session.create_or_get_snowpark_session(st.secrets["snowflake"])

    # add a title
    st.title('Streamlit & snowpark starter kit')

    st.markdown("""
    Everything is working, you're ready to start!
    """)
