from fastapi import FastAPI
from pydantic import BaseModel
from prediction.predict import (
    predict_emotion,
    get_learning_recommendation,
    get_emotion_insight,
    get_motivation,
    save_prediction
)

# ==========================================================
# FastAPI App
# ==========================================================

app = FastAPI(
    title="Emotion Detection API",
    description="AI Powered Emotion Detection & Learning Support",
    version="2.0"
)

# ==========================================================
# Input Schema
# ==========================================================

class UserInput(BaseModel):
    text: str

# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():

    return {
        "message": "Emotion Detection API Running Successfully!"
    }

# ==========================================================
# Health Check
# ==========================================================

@app.get("/health")
def health():

    return {
        "status": "Healthy"
    }

# ==========================================================
# Prediction
# ==========================================================

@app.post("/predict")
def predict(user_input: UserInput):

    text = user_input.text

    # Get prediction result
    result = predict_emotion(text)

    primary_emotion = result["primary_emotion"]

    # Save prediction history
    save_prediction(text, primary_emotion)

    # Recommendation
    recommendation = get_learning_recommendation(
        primary_emotion
    )

    # Emotion Insight
    insight = get_emotion_insight(
        result["primary_emotion"],
        result["secondary_emotion"],
        result["mixed_emotion"]
    )

    # Motivation
    motivation = get_motivation(
        primary_emotion
    )

    return {

        "success": True,

        "text": text,

        "primary_emotion":
            result["primary_emotion"],

        "primary_confidence":
            result["primary_confidence"],

        "secondary_emotion":
            result["secondary_emotion"],

        "secondary_confidence":
            result["secondary_confidence"],

        "mixed_emotion":
            result["mixed_emotion"],

        "confidence":
            result["confidence"],

        "recommendation":
            recommendation,

        "emotion_insight":
            insight,

        "motivation":
            motivation
    }
