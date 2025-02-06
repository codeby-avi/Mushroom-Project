import streamlit as st
import base64
import pandas as pd
import plotly.express as px


def app():

    # Load images and set the background dynamically
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Load background image for page
    img = get_img_as_base64("images/mushroom7.jpg")
    # bg_image = "https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg"
    page_bg_img = f"""
    
    <style>
    .stApp {{
                background: url("data:image/jpeg;base64,{img}");
                background-size: cover;
                # background-repeat: no-repeat;
                
            }}

    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Header Section
    st.title(" Mushroom Trio Classifier 🍄")
    st.write(
        """
        Welcome to the **Mushroom Classification Project**! This advanced system uses machine learning models to help classify mushrooms as either **edible** or **poisonous** based on their physical features.
        
        The goal of this project is to provide an easy-to-use platform for mushroom enthusiasts, researchers, and foragers to identify mushrooms quickly and safely.

        In this project, we have developed two models:
        - **Model 1**: Input the characteristics of a mushroom to predict if it's edible or poisonous.
        - **Model 2**: Upload a mushroom dataset and classify multiple mushrooms automatically.
        """
    )

    # # Quick Links and Buttons Section
    # col1, col2 = st.columns(2)
    # with col1:
    #     if st.button("Go to About Page"):
    #         st.session_state.page = "about"  # Navigate to the About page

    # with col2:
    #     if st.button("Start Classifying"):
    #         from views.model1 import app
    #         app()  # Navigate to the Classification model page

    # Showcase Mushroom Data Visualizations
    # For demonstration purposes, we will show some mock data visualizations
    data = {
        "Mushroom Type": ["Edible", "Poisonous", "Edible", "Poisonous", "Edible", "Poisonous", "Edible", "Poisonous"],
        "Frequency": [200, 150, 180, 210, 240, 190, 220, 160],
    }
    df = pd.DataFrame(data)

    # Create a bar chart
    fig = px.bar(df, x="Mushroom Type", y="Frequency", title="Mushroom Type Distribution", color="Mushroom Type")
    st.plotly_chart(fig, use_container_width=True)

    # Mushroom Classification Overview
    st.header("How It Works")
    st.write(
        """
        Our project uses two powerful models to classify mushrooms based on their characteristics:

        1. **User Input-based Classification**:
            - Users provide details about a mushroom’s features (e.g., cap shape, cap color, odor) via dropdown menus and text inputs.
            - The model then predicts whether the mushroom is **edible** or **poisonous** based on these inputs.

        2. **Dataset-based Classification**:
            - Users upload a dataset of mushrooms with their features.
            - The model classifies each mushroom as either edible or poisonous in bulk.
        
        **Key Features**:
        - Fast and accurate predictions.
        - Easily accessible for both beginners and professionals.
        """
    )

    # Safety Tips and Warnings
    st.header("Important Safety Notice")
    st.write(
        """
        Even though this tool uses machine learning to provide accurate predictions, **always exercise caution** when foraging or consuming mushrooms.
        
        **Important Tips**:
        - Do not rely solely on this model for mushroom identification.
        - Always consult an expert before consuming any wild mushrooms.
        """
    )
    # Footer with social links
    st.markdown('<div class="footer">Created with ❤️ Avinash Chavan</div>', unsafe_allow_html=True)

    # Footer - Technologies and Acknowledgments
    # st.header("Technologies Behind This Project")
    # st.write(
    #     """
    #     This project is powered by the following technologies:
    #     - **Python**: The language used for the back-end logic.
    #     - **Streamlit**: The framework for building the web interface.
    #     - **Plotly**: For creating interactive visualizations.
    #     - **Scikit-learn**: Used for machine learning model development.
    #     - **Pandas**: For data manipulation and feature processing.

    #     Special thanks to the **UCI Mushroom Dataset** for providing real-world data for training our models.
    #     """
    # )
