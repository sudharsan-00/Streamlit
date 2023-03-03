import streamlit as st
import numpy as np
import plotly 
import plotly.figure_factory as ff

st.title("Emission of co2")
st.write("""To predict the emission of co2 by various factors""")
st.write("""Co2 Emission""")
dataset_name = st.sidebar.selectbox("select Dataset", ("Fuel","Industry", "Vehicle"))
st.write(dataset_name)

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

st.plotly_chart(fig, use_container_width=True)
