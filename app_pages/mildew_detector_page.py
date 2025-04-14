import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_prediction_probs
                                                    )

def mildew_detector_body():
    """
    Produce results of analysis on uploaded image
    """
    st.info(
        "**Business Requirements 2 & 3: Classification and Reporting**\n\n"
        "- This section focuses on building and using a machine learning model to **predict whether a cherry leaf is healthy or infected** with powdery mildew based on an uploaded image.\n"
        "- Additionally, users will be able to **generate and access reports** based on the model's predictions to better understand and interpret the results."
    )

    st.write(
        "📥 *To test the model, you can upload your own image or use a pre-existing dataset of healthy and infected cherry leaves.*\n\n"
        "You can download example images from the [Cherry Leaves Dataset on Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    )

    st.write("---")

    images_buffer = st.file_uploader('Upload cherry leaf samples.'
                                     'You may select more than one.',
                                     accept_multiple_files=True)

    if images_buffer is not None:
        report_df = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil,
                     caption=f"Image Size:"
                     f"{img_array.shape[1]}px width x"
                     f"{img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img,
                                                            version=version)
            plot_prediction_probs(pred_proba, pred_class)

            report_df = report_df._append({"Name": image.name,
                                           'Result': pred_class},
                                          ignore_index=True)

        if not report_df.empty:
            st.success("Analysis Report")
            st.table(report_df)
            st.markdown(download_dataframe_as_csv(report_df),
                        unsafe_allow_html=True)
