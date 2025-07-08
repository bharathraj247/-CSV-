import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    /* Entire background including sidebar */
    .stApp {
        background-color: #d2f4ff;  /* Soft pink */
    }

    /* Inside content blocks */
    .block-container {
        background-color: #ffffff;  /* White content box */
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }

    /* Optional: Text color */
    h1, h2, h3, h4, h5, h6, p {
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Analyze your CSV file")

uploaded_file=st.file_uploader("choose a CSV file " ,type="csv")

if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   st.success("File uploaded ")
   
   st.subheader("Data preview")
   st.write(df.head())

   st.subheader(" data summary")
   st.write(df.describe())

   st.subheader("Filter Data")
   columns = df.columns.tolist()
   selected_column = st.selectbox("Select a column to filter",columns)
   unique_values = df[selected_column].unique()
   selected_value = st.selectbox("slect value" ,unique_values )
   filtered_data = df[df[selected_column]== selected_value]
   st.write(filtered_data)
   st.subheader("plot data")
   x_column = st.selectbox("select x-axis column", columns)
   y_column = st.selectbox("select y-axis column", columns)

   if st.button("Generate Plot"):
      st.bar_chart(filtered_data.set_index(x_column)[y_column])

else: 
      st.warning("Please upload a CSV file to continue.")