import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib
import streamlit as st


def download_dataframe_as_csv(df):
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    st.download_button(
        label=f"Download Report! ({datetime_now})",
        data=csv,
        file_name=f"Report_{datetime_now}.csv",
        mime='text/csv'
    )