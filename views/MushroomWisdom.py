import streamlit as st
import base64


def app():
    """About Mushroom Page."""
    st.title("🍄 About Mushroom Classification")

    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Load background image
    img = get_img_as_base64("images/mushroom2.jpg")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0, 0, 0, 0);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}

    .stMarkdown {{
        color: rgba(255, 255, 255, 0.7);  /* Transparent white text */
        font-size: 16px;
    }}
    
    .stHeader h1 {{
        color: rgba(255, 255, 255, 0.9);  /* Slightly less transparent for header */
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    def set_bg_hack_url():

        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True)
    set_bg_hack_url()

    st.title("Mushroom Overview")
    st.write("""
    Mushrooms are fascinating fungi that bridge science, culture, and the environment. 
    As neither plants nor animals, mushrooms belong to the Fungi kingdom, 
    occupying a unique position in the web of life. Their culinary, medicinal, and ecological roles underline their importance in maintaining the balance of ecosystems and supporting human life.
    """)

    st.header("Biological Classification")
    st.markdown("""
    - **Kingdom**: Fungi  
    - **Phylum**: Basidiomycota (most mushrooms) or Ascomycota  
    - **Structure**:  
      - **Cap (Pileus)**: The prominent part, varying in shapes, sizes, and colors.  
      - **Gills (Lamellae)**: Found underneath the cap, they produce microscopic spores for reproduction.  
      - **Stalk (Stem or Stipe)**: Elevates the cap for efficient spore dispersal.  
      - **Mycelium**: The hidden, thread-like network beneath the surface, responsible for nutrient absorption and decomposition.
    """)

    st.header("Types of Mushrooms")
    with st.expander("1. Edible Mushrooms"):
        st.markdown("""
        - **White Button Mushroom** (*Agaricus bisporus*): Widely consumed; versatile with a mild flavor.  
        - **Portobello Mushroom**: A mature white button mushroom; has a rich, meaty texture.  
        - **Shiitake** (*Lentinula edodes*): A staple in Asian cuisine with a smoky, umami flavor.  
        - **Oyster Mushroom** (*Pleurotus ostreatus*): Fan-shaped, delicate, and mildly flavored.  
        - **Enoki** (*Flammulina velutipes*): Thin, crunchy, and ideal for soups or stir-fries.  
        - **Chanterelle** (*Cantharellus spp.*): Golden-yellow, with a fruity aroma.  
        - **Porcini** (*Boletus edulis*): A prized Italian delicacy with a nutty, earthy flavor.  
        """)

    with st.expander("2. Medicinal Mushrooms"):
        st.markdown("""
        - **Reishi** (*Ganoderma lucidum*): Known as the "mushroom of immortality"; supports immunity and longevity.  
        - **Cordyceps**: Parasitizes insects; boosts energy and vitality.  
        - **Turkey Tail** (*Trametes versicolor*): Enhances immune function, particularly in cancer therapies.  
        - **Lion’s Mane** (*Hericium erinaceus*): Promotes cognitive health and nerve regeneration.  
        """)

    with st.expander("3. Toxic Mushrooms"):
        st.markdown("""
        - **Death Cap** (*Amanita phalloides*): Causes severe liver damage and is responsible for most mushroom poisonings.  
        - **Destroying Angel** (*Amanita bisporigera*): Extremely toxic and often mistaken for edible varieties.  
        - **Fly Agaric** (*Amanita muscaria*): Hallucinogenic in small doses but toxic in larger amounts.  
        - **False Morels** (*Gyromitra spp.*): Resemble edible morels but contain dangerous toxins.  
        """)

    with st.expander("4. Psychedelic Mushrooms"):
        st.markdown("""
        - **Psilocybin Mushrooms** (*Psilocybe spp.*): Contain psilocybin, used in research for treating depression, PTSD, and anxiety.  
        """)

    st.header("Nutritional and Health Benefits")
    st.markdown("""
    - **Low in Calories**: Perfect for weight management.  
    - **Rich in Nutrients**:  
      - **Proteins**: Include all nine essential amino acids, making them an excellent vegetarian option.  
      - **Vitamins**: High in B-complex vitamins and a rare natural source of vitamin D.  
      - **Minerals**: Contain selenium, potassium, copper, and zinc.  
      - **Dietary Fiber**: Promotes gut health.  
    - **Antioxidants**:  
      - **Ergothioneine**: Reduces oxidative stress.  
      - **Glutathione**: Protects cells from damage.  
    - **Immune-Boosting**:  
      - Polysaccharides like beta-glucans enhance immunity.  
    """)

    st.header("Ecological Importance")
    st.markdown("""
    - **Decomposition**: Break down organic material, enriching the soil and recycling nutrients.  
    - **Symbiosis**:  
      - **Mycorrhizal Fungi**: Form partnerships with plant roots, enhancing nutrient absorption.  
      - **Truffle Symbiosis**: Grow in association with tree roots, aiding plant health.  
    - **Habitat Creation**: Provide food and shelter for many organisms.  
    - **Bioremediation**:  
      - Break down pollutants like oil spills and plastics.  
      - Absorb heavy metals from contaminated soil.
    """)

    st.header("Interesting Facts")
    st.markdown("""
    - **Largest Living Organism**: The Honey Fungus (*Armillaria ostoyae*) spans over 2,300 acres in Oregon.  
    - **Bioluminescence**: Mushrooms like *Mycena chlorophos* glow in the dark due to chemical reactions.  
    - **Ancient Fossils**: Fossilized mushrooms over 115 million years old have been found.  
    - **Hallucinogenic History**: Used in ancient spiritual rituals by cultures like the Aztecs.  
    - **Natural Antibiotics**: Penicillin, the first antibiotic, was derived from fungi.  
    """)

    st.header("Warnings for Mushroom Foragers")
    st.markdown("""
    - **Identification Skills**: Many edible mushrooms have toxic look-alikes. Use expert guides or consult professionals.  
    - **Cooking Requirement**: Some edible mushrooms are toxic when raw, such as morels.  
    - **Seasonality**: Mushrooms grow during specific times, often in symbiosis with particular trees.  
    """)

    st.header("Project Overview")
    st.write(
        """
        **Mushroom Classification** is a vital task that involves distinguishing between edible and poisonous mushrooms. This project leverages machine learning techniques to automatically classify mushrooms based on their features. Accurate classification of mushrooms is essential to ensure the safety of people, as many mushrooms can be toxic or deadly if consumed.

        Our system offers two models:
        - **Model 1**: A user-friendly tool where users input characteristics of mushrooms to identify whether they are edible or poisonous.
        - **Model 2**: A dataset-based classifier where users can upload a mushroom dataset to predict the classification of various mushrooms.
        
        This project is a step towards enhancing mushroom safety and making classification more accessible.
        """
    )

    st.header("Why Mushroom Classification is Important")
    st.write(
        """
        Mushrooms are widely consumed as food around the world. However, many species of mushrooms are poisonous and can lead to severe health issues or even death if consumed. 
        Accurate mushroom identification is essential to protect human health and avoid poisoning. 

        The two models developed in this project aim to help:
        - **Identify Edible Mushrooms**: By classifying mushrooms based on physical characteristics, we help users determine which mushrooms are safe for consumption.
        - **Avoid Toxic Mushrooms**: Toxic mushrooms are often mistaken for edible ones, causing dangerous consequences. Our model helps differentiate them based on specific features.
        
        In a broader sense, mushroom classification can also support:
        - **Mushroom Research**: Helping scientists better categorize and study mushrooms.
        - **Mushroom Enthusiasts**: Providing an accessible tool for hobbyists and foragers to safely explore mushrooms in the wild.
        """
    )

    st.header("How the Models Work")
    
    st.subheader("Model 1: User Input-based Classification")
    st.write(
        """
        - This model takes user input of key mushroom features (such as cap color, shape, gill spacing, etc.).
        - Users can simply fill in the details through a series of dropdown menus or text input.
        - The model will then classify the mushroom as either **edible** or **poisonous** based on the given characteristics.
        
        This model is perfect for users who encounter mushrooms in the wild and wish to determine if it is safe to eat. The simplicity of input ensures quick and accurate results.
        
        ### How to use:
        1. Choose the mushroom's physical characteristics from the dropdown menus (e.g., cap shape, cap color, gill spacing).
        2. Press the "Classify" button to see if the mushroom is edible or poisonous.
        """
    )

    st.subheader("Model 2: Dataset-based Classification")
    st.write(
        """
        - This model allows users to upload a dataset of mushrooms containing their features.
        - The model will process the data and classify each mushroom as either edible or poisonous.
        - It is designed for researchers, data scientists, and enthusiasts who have large datasets of mushroom characteristics.

        ### How to use:
        1. Upload a CSV file containing mushroom features (e.g., cap color, shape, odor, etc.).
        2. The model will automatically classify each mushroom in the dataset.
        3. Review the results to determine which mushrooms are safe to eat.
        """
    )

    st.header("Mushroom Dataset Information")
    st.write(
        """
        The dataset used for training the machine learning models contains detailed information about different mushroom species. It includes the following features:
        - **Cap Shape**: The shape of the mushroom's cap (e.g., bell, conical, flat).
        - **Cap Color**: The color of the mushroom's cap (e.g., brown, yellow, white).
        - **Gill Spacing**: How close or far apart the gills are.
        - **Odor**: The scent emitted by the mushroom.
        - **Stipe Color**: The color of the stem.
        - **And many more...**

        These features are combined with the classification labels (edible/poisonous) to train the model. The goal is to predict whether a given mushroom belongs to an edible or poisonous class.

        ### Source of Dataset:
        The dataset comes from multiple public repositories of mushroom datasets, including the famous **UCI Mushroom Dataset** which contains various characteristics of mushrooms collected from different regions.
        """
    )

    st.header("Technologies Behind the Project")
    st.write(
        """
        This project leverages several advanced tools and technologies to deliver an interactive and accurate mushroom classification system. The key technologies include:

        - **Python**: The programming language used to build the app, train the models, and handle data.
        - **Streamlit**: The framework used to create the interactive web application that allows users to interact with the models easily.
        - **Scikit-learn**: A popular machine learning library used to train the classification models.
        - **Pandas**: A library used to manage and process the mushroom dataset for training and predictions.
        - **Firebase**: Used for user authentication and secure login functionality.
        - **Matplotlib/Seaborn**: Libraries for visualizing the dataset and model results.
        """
    )

    st.header("Safety Precautions & Warnings")
    st.write(
        """
        Even though this project aims to classify mushrooms as either edible or poisonous, users should still exercise caution. Our system provides predictions based on input features and machine learning models, but it is not a replacement for expert advice.

        **Always consult an expert mycologist or use additional resources before consuming any wild mushrooms.**

        This tool should be used as an educational aid and a first step in mushroom identification. Don't rely solely on the results from the model—cross-check with trusted resources.
        """
    )

    st.header("Future Improvements and Features")
    st.write(
        """
        While the current models are designed to handle mushroom classification based on features and datasets, there are several improvements we are considering for the future:

        - **Real-Time Image Recognition**: We plan to develop a system that can classify mushrooms using real-time images, enabling users to simply snap a picture of a mushroom and get a prediction.
        - **Model Fine-Tuning**: We aim to improve the accuracy of our models by incorporating more features and training with larger and more diverse datasets.
        - **Mushroom Identification Community**: We're working on a platform where mushroom enthusiasts and researchers can share and contribute their data to improve the system's accuracy.
        """
    )

    st.header("Contact & Collaboration")
    st.write(
        """
        If you are interested in collaborating or have any questions, feel free to reach out to us. We would love to hear from you!
        
        - **Email**: your_email@example.com
        - **GitHub**: [Link to your GitHub repository]
        - **LinkedIn**: [Your LinkedIn profile link]
        """
    )

    st.image(r"D:\Mushroom Project\images\mushroom1.jpg", caption="Exploring the Fascinating World of Mushrooms!")
    # Footer with social links
    st.markdown('<div class="footer">Created with ❤️ by Team </div>', unsafe_allow_html=True)