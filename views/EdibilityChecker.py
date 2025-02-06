import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import joblib


def classify_mushroom(odor, bruises, gill_color, cap_shape, cap_surface, cap_color):
    match (odor, bruises, gill_color, cap_shape, cap_surface, cap_color):
        # Poisonous: Strong odor (regardless of other factors)
        case ("f" | "y" | "c" | "m" | "p" | "s", _, _, _, _, _):
            return "Poisonous"

        # Edible: No odor, bruises, and certain cap colors
        case ("n", "t", _, _, _, "w" | "g" | "n"):
            return "Edible"

        # Edible: No odor, certain gill colors
        case ("n", _, "b" | "p" | "u", _, _, _):
            return "Edible"

        # Edible: Specific Odor + Specific Gill Color combinations (including Almond)
        case ("a", _, "b" | "p" | "u", _, _, _):
            return "Edible"

        # Edible: No Odor, Smooth Cap Surface, and Certain Cap Shape
        case ("n", _, _, "x" | "f", "s", _):
            return "Edible"

        # Poisonous: No bruises, specific cap shape, and cap surface
        case (_, "f", _, "b" | "c", "y" | "f", _):
            return "Poisonous"

        # Default case: Assume Poisonous
        case _:
            return "Poisonous"


# Streamlit app
def app():
    st.title("Mushroom Classifier 🍄")

    # Input fields
    odor = st.selectbox("Odor", ["Almond", "Anise", "Creosote", "Fishy", "Foul", "Musty", "None", "Pungent", "Spicy"])
    bruises = st.selectbox("Bruises", ["Yes", "No"])
    gill_color = st.selectbox("Gill Color", ["Black", "Brown", "Buff", "Chocolate", "Gray", "Green", "Orange", "Pink", "Purple", "Red", "White", "Yellow"])
    cap_shape = st.selectbox("Cap Shape", ["Bell", "Conical", "Flat", "Knobbed", "Sunken", "Convex"])
    cap_surface = st.selectbox("Cap Surface", ["Fibrous", "Grooves", "Smooth", "Scaly"])
    cap_color = st.selectbox("Cap Color", ["Brown", "Buff", "Cinnamon", "Gray", "Green", "Pink", "Purple", "Red", "White", "Yellow"])

    # Map selections to codes for classification
    odor_map = {"Almond": "a", "Anise": "l", "Creosote": "c", "Fishy": "y", "Foul": "f", "Musty": "m", "None": "n", "Pungent": "p", "Spicy": "s"}
    bruises_map = {"Yes": "t", "No": "f"}
    gill_color_map = {"Black": "k", "Brown": "n", "Buff": "b", "Chocolate": "h", "Gray": "g", "Green": "r", "Orange": "o", "Pink": "p", "Purple": "u", "Red": "e", "White": "w", "Yellow": "y"}
    cap_shape_map = {"Bell": "b", "Conical": "c", "Flat": "f", "Knobbed": "k", "Sunken": "s", "Convex": "x"}
    cap_surface_map = {"Fibrous": "f", "Grooves": "g", "Smooth": "s", "Scaly": "y"}
    cap_color_map = {"Brown": "n", "Buff": "b", "Cinnamon": "c", "Gray": "g", "Green": "r", "Pink": "p", "Purple": "u", "Red": "e", "White": "w", "Yellow": "y"}

    # Convert user selections to codes
    odor_code = odor_map[odor]
    bruises_code = bruises_map[bruises]
    gill_color_code = gill_color_map[gill_color]
    cap_shape_code = cap_shape_map[cap_shape]
    cap_surface_code = cap_surface_map[cap_surface]
    cap_color_code = cap_color_map[cap_color]

    # Classify the mushroom when button is clicked
    if st.button("Classify Mushroom"):
        classification = classify_mushroom(odor_code, bruises_code, gill_color_code, cap_shape_code, cap_surface_code, cap_color_code)
        st.subheader(f"The mushroom is **{classification}**. 🍄")

    st.markdown('<div class="footer">Created with ❤️ Avinash Chavan</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
