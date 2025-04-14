import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

def image_visualiser_body():
    """
    Display average and variability images, differences between classes,
    and an image gallery as part of Business Requirement 1: Data Visualisation.
    """
    st.write("## 📊 Image Visualizer")
    st.info(
        "**Business Requirement 1: Data Visualisation**\n\n"
        "This section supports the first business requirement by helping to visually differentiate between healthy cherry leaves "
        "and those infected with powdery mildew.\n\n"
        "We explore statistical summaries (mean and variability), visual comparisons, and image galleries for both classes."
    )

    version = 'v1'

    # Average and Variability Visualisation
    if st.checkbox("📈 Show Average and Variability Images"):
        avg_healthy = plt.imread("outputs/" + version + "/avg_var_healthy.png")
        avg_mildew = plt.imread("outputs/" + version + "/avg_var_powdery_mildew.png")

        st.subheader("Healthy Leaf - Average & Variability")
        st.image(avg_healthy, caption="Healthy Cherry Leaf: Average and Standard Deviation")

        st.subheader("Infected Leaf - Average & Variability")
        st.image(avg_mildew, caption="Infected Cherry Leaf: Average and Standard Deviation")

        st.warning(
            "- The **variability images** reveal textural patterns such as white mildew spots that are more pronounced in infected leaves.\n"
            "- The **average images** highlight general color differences, with healthy leaves appearing darker green than infected ones."
        )
        st.write("---")

    # Differences Between Averages
    if st.checkbox("🔍 Compare Average Healthy vs Powdery Mildew Infected Leaves"):
        diff_bet_avgs = plt.imread("outputs/" + version + "/avg_diff.png")

        st.subheader("Difference Between Average Images")
        st.image(diff_bet_avgs, caption="Pixel-wise Difference: Average Healthy vs Infected Leaf")
        st.warning(
            "- Slight but consistent differences in shape and color intensity were found.\n"
            "- These distinctions suggest that **automated visual classification** is feasible."
        )
        st.write("---")

    # Image Gallery
    if st.checkbox("🖼️ Display Image Gallery"):
        st.subheader("Image Gallery")
        st.write("Select a category and click the button to generate a gallery of example leaves.")
        my_data_dir = "inputs/cherry_leaves_dataset/cherry-leaves"
        labels = os.listdir(my_data_dir + "/validation")

        label_to_display = st.selectbox("Select label", options=labels, index=0)

        if st.button("Create Montage"):
            image_gallery(
                dir_path=my_data_dir + "/validation",
                label_to_display=label_to_display,
                nrows=8, ncols=3, figsize=(10, 25)
            )
        st.info(
            "Above is a visual gallery of randomly selected **" + label_to_display.replace('_', ' ').title() +
            "** leaves from the validation dataset."
        )
        st.write("---")

def image_gallery(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """
    Display gallery of images of requested image type
    """

    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(dir_path + '/' + label_to_display)

        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your gallery. \n"
                f"There are {len(images_list)} images in the subset. "
                f"You requested a gallery with {nrows * ncols} spaces")
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

        for x in range(0, nrows * ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])

        plt.tight_layout()
        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")