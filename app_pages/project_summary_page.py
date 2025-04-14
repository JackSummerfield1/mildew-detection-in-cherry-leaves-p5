import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():
    """
    Displays content for the Project Summary Page
    """
    st.write("### Project Summary")

    st.info(
        "**General Information**\n\n"
        "- Powdery mildew is a fungal disease that affects many types of plants. "
        "It is caused by various species of ascomycete fungi and typically appears as "
        "distinctive white patches on the leaves and stems of infected plants.\n\n"
        "- This disease thrives in warm, humid conditions and is especially common in horticultural crops. "
        "It can lead to significant yield losses if not properly managed.\n\n"
        "- The client is currently facing an outbreak of powdery mildew across several cherry tree plantations. "
        "Manual inspection of leaves has proven inefficient, prompting the need for a more scalable solution.\n\n"
        "- To address this, the client has requested a Machine Learning (ML) model capable of analyzing uploaded images "
        "and determining whether a cherry leaf shows signs of infection."
    )

    st.info(
        "**Dataset Information**\n\n"
        "- The dataset consists of 4,208 images of cherry tree leaves, with an equal split: "
        "2,104 images of healthy leaves and 2,104 images showing signs of powdery mildew infection.\n\n"
        "- This dataset was provided by the client and is also publicly available on "
        "[Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    )

    st.write(
        "🔗 *For more details, please refer to the* "
        "[Project README](https://github.com/JackSummerfield1/mildew-detection-in-cherry-leaves-p5/blob/main/README.md)."
    )

    st.success(
        "**Business Requirements**\n\n"
        "**Requirement 1: Data Visualisation**\n"
        "- Present the average (mean) and variability (standard deviation) of the images for both healthy and mildew-infected cherry leaves.\n"
        "- Display representative images of an average healthy leaf and an average infected leaf to highlight visual differences.\n"
        "- Provide an image gallery showcasing examples of healthy and infected cherry leaves.\n\n"
        "**Requirement 2: Classification**\n"
        "- Develop and train a machine learning model to classify whether a cherry leaf is healthy or infected with powdery mildew.\n"
        "- This will be approached as a binary classification problem, as there are only two possible outcomes: healthy or infected.\n\n"
        "**Requirement 3: Report**\n"
        "- Generate user-friendly reports that summarize the model’s predictions and performance.\n"
        "- Ensure reports are easily accessible and understandable for all users, regardless of their technical background."
    )