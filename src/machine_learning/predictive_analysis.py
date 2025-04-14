import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_prediction_probs(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class= pd.DataFrame(
            data=[0,0],
            index={'Healthy': 0, 'Powdery Mildew': 1}.keys(),
            columns=['Probability']
        )
    
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index
    
    fig = px.bar(
            prob_per_class,
            x = 'Diagnostic',
            y = prob_per_class['Probability'],
            range_y=[0,1],
            width=800, height=400,template='seaborn')
    st.plotly_chart(fig)

def resize_input_image(img, version):
    """
    Reshape image to the average image size
    """

    img_shape = load_pkl_file(file_path=f"outputs/{version}/img_shape.pkl")
    img_resized = img.resize((img_shape[1], img_shape[0]), Image.LANCZOS)
    my_img = np.expand_dims(img_resized, axis=0)/255

    return my_img

def load_model_and_predict(my_img, version):
    """
    Making ML predictions on live images
    """

    model = load_model(f"outputs/{version}/powdery_mildew_model.h5")

    pred_proba = model.predict(my_img)[0, 0]

    target_map = {v: k for k, v in {'Healthy': 0, 'Powdery Mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    if pred_class == 'Healthy':
        st.write(
            f"The predictive analysis indicates that the cherry leaf is "
            f"**healthy**")
    else:
        st.write(
            f"The predictive analysis indicates that the cherry leaf has "
            f"**powdery mildew**")

    return pred_proba, pred_class