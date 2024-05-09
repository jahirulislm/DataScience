import streamlit as st
# import pandas as pd
# import numpy as np
# # import matplotlib.pyplot as plt
# import seaborn as sns
# add title
st.title("Data Analysis Application")
st.subheader("This is a simple data analysis application")

# create dropdownn menu llist to choose dataset
dataset_options = ['iris','titanic','tips','diamonds']
selected_dataset=st.selectbox('Select a dataset', dataset_options)

# load and display the selected dataset
if(selected_dataset == 'iris'):
    df = sns.load_dataset('iris')