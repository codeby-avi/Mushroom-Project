import streamlit as st

def app():
    # Set Background
    def set_bg():
        st.markdown(
            """
            <style>
                .stApp {
                    background: url("https://avi-chavan-96.sirv.com/Mushroom/mushroom-7570693_1280.jpg") no-repeat center center fixed;
                    background-size: cover;
                }
                .team-card {
                    background-color: #f9f9f9;
                    border-radius: 12px;
                    padding: 15px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    transition: transform 0.2s ease;
                    cursor: pointer;
                }
                .team-card:hover {
                    transform: scale(1.05);
                }
                .footer {
                    margin-top: 20px;
                    text-align: center;
                    color: #555;
                    font-size: 14px;
                }
                .header {
                    color: #4CAF50;
                    font-size: 24px;
                    font-weight: bold;
                    text-align: center;
                    margin-bottom: 20px;
                }
                .sub-header {
                    font-size: 20px;
                    font-weight: bold;
                    color: #333;
                    margin-top: 10px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg()

    # Page Title and Introduction
    st.markdown('<div class="header">🍄 About Us</div>', unsafe_allow_html=True)
    st.write(
        """
        Welcome to the **Mushroom Classification Project**!  
        Our goal is to make mushroom identification **safer**, **smarter**, and **accessible** to everyone.  
        Whether you're a nature enthusiast, a forager, or a data scientist, this project is designed with you in mind.  
        """
    )

    # Vision and Mission Section
    with st.expander("📌 **Our Vision and Mission**"):
        st.write(
            """
            ### 🌍 Vision:
            - To create a safer environment for mushroom foragers and enthusiasts by providing reliable identification tools.
            
            ### 🚀 Mission:
            - To leverage cutting-edge machine learning and user-friendly interfaces for accurate mushroom classification.
            - To educate users about the fascinating world of mushrooms and ensure safety in foraging practices.
            """
        )

    # Project Overview
    st.markdown('<div class="header">🚀 Project Overview</div>', unsafe_allow_html=True)
    st.write(
        """
        **🍄 Mushroom Classification** is a vital task that involves distinguishing between edible and poisonous mushrooms.  
        This project leverages **machine learning** 🤖 techniques to automatically classify mushrooms based on their features.  

        ### 🏆 Our system offers two models:
        - **🛠️ Model 1**: User input-based classification for real-time foragers.  
        - **📊 Model 2**: Dataset-based classification for researchers and data scientists.  

        This project enhances mushroom safety 🌍 and makes classification more **accessible** 🌐.
        """
    )

    # How the Models Work
    st.markdown('<div class="header">⚙️ How the Models Work</div>', unsafe_allow_html=True)

    st.subheader("Model 1: User Input-based Classification")
    st.write(
        """
        - Takes user input of mushroom features (cap color, shape, gill spacing, etc.).  
        - Uses dropdown menus or text input for simplicity.  
        - Classifies the mushroom as either **edible** or **poisonous**.  
        
        **How to use:**  
        1. Choose the mushroom's physical characteristics.  
        2. Press "Classify" to see if the mushroom is edible or poisonous.  
        """
    )

    st.subheader("Model 2: Dataset-based Classification")
    st.write(
        """
        - Allows users to upload a dataset of mushrooms containing their features.  
        - Processes the data and classifies each mushroom as edible or poisonous.  
        - Designed for researchers and data scientists handling large datasets.  

        **How to use:**  
        1. Upload a CSV file with mushroom features.  
        2. The model classifies the mushrooms.  
        3. Review the results to determine safety.  
        """
    )

    # Technologies and Features
    st.markdown('<div class="header">🔧 Technologies and Features</div>', unsafe_allow_html=True)
    st.write(
        """
        **🛠️ Technologies Used:**  
        - Python  
        - Streamlit  
        - Scikit-learn  
        - Pandas  
        - Firebase  

        **🌟 Features:**  
        - Accurate classification models  
        - User-friendly interface  
        - Dataset processing  
        - Secure user authentication  
        """
    )

    # Future Plans
    st.markdown('<div class="header">🚀 Future Plans</div>', unsafe_allow_html=True)
    st.write(
        """
        - **Real-Time Image Recognition** – Classify mushrooms using real-time images.  
        - **Model Fine-Tuning** – Improve accuracy with larger datasets.  
        - **Community Contribution** – Build a platform for mushroom enthusiasts to share data.  
        """
    )

    # Meet the Team Section
    st.markdown('<div class="header">🌟 Meet the Team</div>', unsafe_allow_html=True)

    head_members = [
        {"name": "Alice Smith", "role": "Project Lead", "bio": "Expert in AI and data science.", "image": "D:/Mushroom Project/images/mushroom2.jpg"},
        {"name": "Bob Johnson", "role": "ML Engineer", "bio": "Focused on building robust models.", "image": "D:/Mushroom Project/images/mushroom2.jpg"}
    ]

    team_members = [
        {"name": "Chavan Avinash", "role": "Project Lead", "bio": "Expert in AI and data science.", "image": "D:/Mushroom Project/images/mushroom2.jpg"},
        {"name": "Pratiksha Irole", "role": "ML Engineer", "bio": "Focused on building robust models.", "image": "D:/Mushroom Project/images/mushroom2.jpg"},
        {"name": "Sneha Shinde", "role": "Frontend Developer", "bio": "Designed the user interface.", "image": "D:/Mushroom Project/images/mushroom2.jpg"},
        {"name": "Samarth Garde", "role": "Researcher", "bio": "Provided mycology expertise.", "image": "https://avi-chavan-96.sirv.com/Mushroom/mushroom-7570693_1280.jpg"}
    ]

    # Display Head Members
    cols = st.columns(len(head_members))
    for col, member in zip(cols, head_members):
        with col:
            st.image(member["image"], use_container_width=True)
            st.subheader(member["name"])
            st.write(f"**{member['role']}**")
            st.write(member["bio"])

    # Display Team Members
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            st.image(member["image"], use_container_width=True)
            st.subheader(member["name"])
            st.write(f"**{member['role']}**")
            st.write(member["bio"])

    # Contact Section
    st.markdown('<div class="header">📬 Get in Touch</div>', unsafe_allow_html=True)
    st.write(
        """
        - **GitHub**: [Repository](https://github.com/)  
        - **Email**: developerhub@example.com  
        - **LinkedIn**: [Profile](https://linkedin.com/)  
        """
    )

    # Footer
    st.markdown('<div class="footer">Created with ❤️ by Strategic Synergists</div>', unsafe_allow_html=True)

