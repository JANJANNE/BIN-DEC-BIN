import streamlit as st
import time
import DECTOBIN as db
import BINTODEC as bd

background_image = "https://thumbs.dreamstime.com/b/wooden-floors-city-night-view-distance-142298053.jpg"
title_text = "<div style='text-align: left; color: white;'>CONVERTER</div>"
name = "Mario D. Naive Jr."
st.markdown(name, unsafe_allow_html=True)
markdown_str = f"""
    <style>
        .background {{
            background-image: url('{background_image}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
    </style>

    <div class="background">
        <h1 class="Converter">{title_text}</h1>
    </div>
"""
st.markdown(markdown_str, unsafe_allow_html=True)

selected_con = st.toggle("← Click to Choose")
show_spinner = st.sidebar.checkbox("Show Spinner")

if show_spinner:
    with st.spinner("Please wait a moment..."):
        time.sleep(2)
        st.success("Done!")
else:
    st.write("Spinner is not shown.")

if selected_con:
    st.title("Binary To Decimal Converter")
    binary_input = st.text_input("Enter a binary number: ", key="binary_number")


    if not binary_input.isdigit() or set(binary_input) - {"0", "1"}:
        st.error("Warning!! Please put a valid binary number.")
    else:
        control_button = st.button("Convert")
        st.session_state["con_button"] = control_button
        if control_button:
            decimal_number = bd.Binary_To_Decimal(binary_input)
            st.session_state["decimal number"] = decimal_number
            st.text_input("Therefore, the conversion is: ", value = str(decimal_number))
            print(st.session_state)

else:
    st.title("Decimal To Binary Converter")
    decimal_input = st.text_input("Enter a decimal number: ", key="decimal_input")

    if not decimal_input.isdigit():
        st.error("Warning!! Please put a valid decimal number.")
    else:
        control_button = st.button("Convert")
        st.session_state["con_button"] = control_button
        if control_button:
            binary_number = db.Decimal_To_Binary(int(decimal_input))
            st.session_state["binary number"] = binary_number
            st.text_input("Therefore, the conversion is: ", value = str(binary_number))
            print(st.session_state)