import json
import pandas as pd
import numpy as np
import streamlit as st
import plotly.figure_factory as ff


st.title("Johannesburg Market Daily Prices")

st.sidebar.markdown("## Select commodity and container")

with open('sample_data/apples.json') as f:
    data = json.load(f)

st.markdown(f'Commodity: {data["commodity"]}')

