import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard(history):

    st.header("📊 Analytics Dashboard")

    # ----------------------------
    # No data
    # ----------------------------
    if len(history) == 0:
        st.info("No predictions available.")
        return

    # ----------------------------
    # Create DataFrame
    # ----------------------------
    df = pd.DataFrame(history)

    # ----------------------------
    # Prediction History
    # ----------------------------
    st.subheader("📜 Prediction History")

    st.dataframe(
        df,
        width="stretch"
    )

    # ----------------------------
    # Emotion Counts
    # ----------------------------
    st.subheader("📈 Emotion Counts")

    emotion_counts = (
        df.groupby("emotion")
        .size()
        .reset_index(name="Count")
    )

    emotion_counts.rename(
        columns={"emotion": "Emotion"},
        inplace=True
    )

    # Debug (remove later if you want)
    st.write(emotion_counts)

    # ----------------------------
    # Bar Chart
    # ----------------------------
    fig_bar = px.bar(
        emotion_counts,
        x="Emotion",
        y="Count",
        color="Emotion",
        text="Count",
        title="Emotion Counts"
    )

    fig_bar.update_layout(
        xaxis_title="Emotion",
        yaxis_title="Count",
        template="plotly_white",
        height=450
    )

    st.plotly_chart(
        fig_bar,
        width="stretch"
    )

    # ----------------------------
    # Pie Chart
    # ----------------------------
    st.subheader("🥧 Emotion Distribution")

    fig_pie = px.pie(
        emotion_counts,
        names="Emotion",
        values="Count",
        color="Emotion",
        hole=0.4,
        title="Emotion Distribution"
    )

    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_pie.update_layout(
        height=500,
        template="plotly_white"
    )

    st.plotly_chart(
        fig_pie,
        width="stretch"
    )
