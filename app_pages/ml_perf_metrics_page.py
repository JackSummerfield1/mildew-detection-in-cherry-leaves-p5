import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

def ml_performance_metrics():
    """
    Display performance metrics of the ML model,
    including label distribution, training history,
    and evaluation on the test set.
    """
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    distribution_of_labels = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(distribution_of_labels,
             caption='Labels Distribution on Train, Validation and Test Sets')
    
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1:
        model_accuracy = plt.imread(f"outputs/{version}/model_training_accuracy.png")
        st.image(model_accuracy, caption='Model Training Accuracy')
    with col2:
        model_losses = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_losses, caption='Model Training Losses')

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                 index=['Loss', 'Accuracy']))
    
    st.write("### Conclusion")
    st.success(
    "* At the start of this project, the client requested a machine learning model "
    "capable of predicting the presence of mildew on cherry leaves with at least 97% accuracy.\n"
    "* As shown in the performance table above, the final model achieved 99% accuracy "
    "on the test dataset. This exceeds the required threshold, and we can therefore consider "
    "this business requirement fulfilled."
    )
