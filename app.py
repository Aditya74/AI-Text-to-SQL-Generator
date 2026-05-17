import streamlit as st
import json

from prompt import prompt
from model import llm
from parser import SQLResponse

st.set_page_config(
    page_title="AI Text-to-SQL Generator",
    page_icon=""
)

st.title("AI Text-to-SQL Generator")

schema = st.text_area(
    "Enter Database Schema",
    height=200,
    placeholder="Table users(id, name, age)"
)

question = st.text_input(
    "Ask your question",
    placeholder="Show users older than 25"
)

if st.button("Generate SQL"):

    if schema and question:

        final_prompt = prompt.format(
            schema=schema,
            question=question
        )

        try:

            response = llm.invoke(final_prompt)

            raw_output = response.content

            parsed_output = json.loads(raw_output)

            validated_output = SQLResponse(**parsed_output)

            st.success("SQL Generated Successfully")

            st.subheader("SQL Query")
            st.code(validated_output.sql_query, language="sql")

            st.subheader("Explanation")
            st.write(validated_output.explanation)

            st.subheader("Tables Used")
            st.write(validated_output.tables_used)

            st.subheader("Conditions Applied")
            st.write(validated_output.conditions_applied)

            st.subheader("Full JSON Output")
            st.json(parsed_output)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter schema and question.")
        
        
# Table users(id, name, age, city)
# Show all users older than 25