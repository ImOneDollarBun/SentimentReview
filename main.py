import uvicorn
from fastapi import FastAPI
import sqlite3
import json
from pydantic import BaseModel
import datetime


class ReviewSchema(BaseModel):
    text: str


class Database:
    def __init__(self, dbname="reviews.db"):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS reviews (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              text TEXT NOT NULL,
                              sentiment TEXT NOT NULL,
                              created_at TEXT NOT NULL
                            );""")

    def add_item(self, text, sentiment, created_at):
        self.cursor.execute('INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)', (text, sentiment, created_at,))
        response = self.cursor.execute("SELECT * FROM reviews WHERE text = ?", (text,)).fetchone()
        return response

    def find_by_sentiment_item(self, sentiment):
        response = self.cursor.execute("SELECT * FROM reviews WHERE sentiment = ?", (sentiment,)).fetchall()
        return response


app = FastAPI()
db = Database()


@app.get('/reviews')
async def get_reviews(sentiment=""):
    response = db.find_by_sentiment_item(sentiment)
    return response


@app.post("/reviews")
async def upload_review(review: ReviewSchema):
    sentiment = 'neutral'
    if 'хорошо' in review.text or 'люблю' in review.text:
        sentiment = 'positive'
    elif 'плохо' in review.text or 'ненавиж' in review.text:
        sentiment = 'negative'

    created_at = datetime.datetime.utcnow().isoformat()
    response = db.add_item(review.text, sentiment, created_at)

    return response


if __name__ == "__main__":
    uvicorn.run('main:app')