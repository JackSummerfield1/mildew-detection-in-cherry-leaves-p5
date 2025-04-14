import streamlit as st
import matplotlib.pyplot as plt

def project_hypothesis_body():
    """
    Display content for Project Hypothesis Page
    """
    st.write("### Project Hypothesis 1")

    # Null Hypothesis
    st.info(
        "**Null Hypothesis (H₀):**\n"
        "A binary classification model cannot accurately predict the presence of powdery mildew on cherry leaves."
    )

    # Alternative Hypothesis
    st.success(
        "**Alternative Hypothesis (H₁):**\n"
        "A binary classification model can accurately predict the presence of powdery mildew on cherry leaves."
    )

    # Visual Defects in Infected Leaves
    st.write(
        "### Visual Defects and Leaf Comparison\n"
        "Cherry leaves infected with powdery mildew exhibit distinctive visual defects, "
        "such as numerous white or grayish powdery spots that cover large areas of the leaf. "
        "Healthy leaves are generally uniform in color with no visible spots."
    )

    # Average Image Study
    st.write(
        "### Average Image Study\n"
        "We will analyze the average images of healthy and infected leaves to identify any consistent visual differences. "
        "This study will help determine if visual patterns, like the presence of white spots, can be used to differentiate between the two."
    )

    # Validation of Hypothesis
    st.success(
        "**Validation:**\n"
        "Initial analysis of the average images confirms that infected leaves show clear visual differences, "
        "such as the characteristic white spots, which could aid in classifying leaves as infected or healthy."
    )

    st.write("---")


    st.write("### Project Hypothesis 2")

    # Null Hypothesis
    st.info(
        "**Null Hypothesis (H₀):**\n"
        "There is no significant visual difference between healthy and mildew-infected cherry leaves observable through average and variability image analysis."
    )

    # Alternative Hypothesis
    st.success(
        "**Alternative Hypothesis (H₁):**\n"
        "There are significant visual differences between healthy and mildew-infected cherry leaves, which can be identified through average and variability image analysis."
    )

    # Visual Defects in Infected Leaves
    st.write(
        "### Visual Defects and Leaf Comparison\n"
        "Cherry leaves affected by powdery mildew tend to display noticeable visual defects, "
        "particularly white or grayish powdery spots that spread across the leaf surface. "
        "These features are typically absent in healthy leaves, which appear more uniform in color and texture."
    )

    # Average and Variability Image Study
    st.write(
        "### Average and Variability Image Study\n"
        "By examining average and variability images for both healthy and infected leaves, "
        "we aim to determine whether these visual patterns are consistent and distinctive enough to differentiate the two categories."
    )

    # Validation of Hypothesis
    st.success(
        "**Validation:**\n"
        "Preliminary image analysis reveals clear and consistent visual differences between the average and variability images of healthy and infected leaves. "
        "This supports the hypothesis that powdery mildew presence can be visually distinguished before applying machine learning."
    )

    st.write("---")
