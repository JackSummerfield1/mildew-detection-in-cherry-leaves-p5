import streamlit as st
from app_pages.multipage import MultiPage

# Load scripts for each page
from app_pages.project_summary_page import project_summary_body
from app_pages.image_visualiser_page import image_visualiser_body
from app_pages.mildew_detector_page import mildew_detector_body
from app_pages.project_hypotheses_page import project_hypothesis_body
from app_pages.ml_perf_metrics_page import ml_performance_metrics

# Create an instance of the app
app = MultiPage(app_name="Mildew Detector - Cherry Leaves")

# Add app pages
app.add_page("Project Summary", project_summary_body)
app.add_page("Image Visualiser", image_visualiser_body)
app.add_page("Mildew Detector", mildew_detector_body)
app.add_page("Project Hypotheses", project_hypothesis_body)
app.add_page("ML Performance Metrics", ml_performance_metrics)

# Run the app
app.run()