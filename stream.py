import streamlit as st
import pandas as pd
import os


DATA_FILE = "user_data.csv"


def save_data(number, email):

    new_data = pd.DataFrame({"Number": [number], "Email": [email]})
    if os.path.exists(DATA_FILE):
        existing_data = pd.read_csv(DATA_FILE)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data

    updated_data.to_csv(DATA_FILE, index=False)


def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Number", "Email"])


st.title("📇 Contact Storage App")

st.write("Enter your contact details below:")


number = st.text_input("📞 Phone Number")
email = st.text_input("📧 Email Address")


if st.button("Save"):
    if number and email:
        save_data(number, email)
        st.success("✅ Data saved successfully!")
    else:
        st.warning("⚠️ Please enter both number and email.")


st.subheader("📋 Stored Contacts")
data = load_data()
st.dataframe(data)
