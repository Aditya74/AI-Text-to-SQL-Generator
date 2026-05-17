from langchain_core.prompts import PromptTemplate

template = """
You are an expert SQL query generator.

Generate SQL query from the given database schema and user question.

Return ONLY valid JSON.

DATABASE SCHEMA:
{schema}

QUESTION:
{question}

Expected JSON format:
{{
    "sql_query": "string",
    "explanation": "string",
    "tables_used": ["string"],
    "conditions_applied": ["string"]
}}
"""

prompt = PromptTemplate(
    input_variables=["schema", "question"],
    template=template
)