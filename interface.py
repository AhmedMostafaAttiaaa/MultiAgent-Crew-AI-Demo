import streamlit as st
from crew_run import result

st.title("Event Management Crew App")
st.write("Result of Crew Execution:")
st.success(result)
