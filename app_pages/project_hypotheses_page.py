import streamlit as st
import matplotlib.pyplot as plt

def project_hypothesis_body():
    """
    Display content for Project Hypothesis Page
    """
    st.write("### Project Hypotheses")

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