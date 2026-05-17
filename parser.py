from pydantic import BaseModel
from typing import List

class SQLResponse(BaseModel):
    sql_query: str
    explanation: str
    tables_used: List[str]
    conditions_applied: List[str]