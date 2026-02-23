from fastapi import FastAPI
from sqlalchemy import text
from database import SessionLocal

app = FastAPI()

@app.get("/qualified-candidates")
def get_candidates():
    db = SessionLocal()
    result = db.execute(text("""
        SELECT candidate_id
        FROM candidates
        WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
        GROUP BY candidate_id
        HAVING COUNT(DISTINCT skill) = 3
        ORDER BY candidate_id;
    """)).fetchall()

    db.close()
    return [row[0] for row in result]
