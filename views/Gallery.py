import streamlit as st
import base64

def app():


    # About Us Page Header
    st.title("🍄 About Us")
    st.write(
        """
        Welcome to the **Mushroom Classification Project**! Our goal is to make mushroom identification safer, smarter, and accessible to everyone. 
        Whether you're a nature enthusiast, a forager, or a data scientist, this project is designed with you in mind.
        """
    )

    # Interactive Vision and Mission Section
    with st.expander("📌 **Our Vision and Mission**"):
        st.write(
            """
            ### Vision:
            - To create a safer environment for mushroom foragers and enthusiasts by providing reliable identification tools.
            
            ### Mission:
            - To leverage cutting-edge machine learning and user-friendly interfaces for accurate mushroom classification.
            - To educate users about the fascinating world of mushrooms and ensure safety in foraging practices.
            """
        )

    # Project Overview Section
    st.header("🌟 Project Overview")
    st.write(
        """
        The **Mushroom Classification Project** focuses on differentiating between edible and poisonous mushrooms using machine learning. This is achieved through two unique models:
        
        - **Model 1**: A user-friendly classifier where you input physical characteristics of a mushroom (e.g., cap shape, color, and odor) to determine its safety.
        - **Model 2**: A dataset-driven classifier that processes large datasets of mushroom features and predicts their edibility in batches.
        
        This system ensures both individual users and researchers can safely classify mushrooms with ease.
        """
    )

    # Technologies and Features Section
    st.header("🔧 Technologies and Features")
    st.write(
        """
        We utilize state-of-the-art technologies to bring this project to life:
        
        - **Python**: For implementing the machine learning models and backend logic.
        - **Streamlit**: To create an interactive and user-friendly interface.
        - **Scikit-learn**: The backbone of our classification models.
        - **Pandas**: For dataset processing and analysis.
        - **Firebase**: For secure authentication and data management.
        
        **Features**:
        - Accurate classification models trained on real-world datasets.
        - A clean, easy-to-use interface with dropdowns and dataset upload options.
        - Visualizations of classification results and feature importance.
        """
    )

    # Developer Hub Section
    st.header("👨‍💻 Developer Hub")
    st.write(
        """
        Welcome to the Developer Hub! This page dives into the technical and creative minds that made the **Mushroom Classification Project** possible.
        Here, you'll learn about our unique contributions, behind-the-scenes insights, and how we tackled challenges to bring this vision to life.
        """
    )

    # Section: Developer Journey
    st.header("🚀 Developer Journey")
    st.write(
        """
        Every project has a story, and here’s ours:
        
        - **Conceptualization**: From initial brainstorming, we envisioned a tool that combines mycology with machine learning.
        - **Research**: Deep dives into mushroom biology and data collection formed the foundation of this project.
        - **Prototyping**: Our iterative design involved testing multiple models and refining user workflows.
        - **Execution**: Streamlined implementation with focus on user experience and performance.
        
        Each stage brought new challenges, learning opportunities, and achievements!
        """
    )

    # Section: Key Contributions (Interactive Accordion Style)
    with st.expander("📌 **Key Contributions**"):
        st.write(
            """
            - **Alice Smith**: Developed and optimized machine learning models, ensuring high accuracy and reliability.
            - **Bob Johnson**: Engineered scalable pipelines for data processing and feature extraction.
            - **Carla Davis**: Crafted the intuitive and interactive interface to make classification user-friendly.
            - **David Lee**: Provided domain expertise in mycology and created the training datasets.
            """
        )

    # Section: Behind the Scenes
    st.header("🎬 Behind the Scenes")
    st.write(
        """
        This project combines cutting-edge technology with practical applications in both machine learning and mycology. Here's an inside look at some of the work that went into bringing this project to life:
        
        - **Data Processing**: We cleaned, analyzed, and transformed raw mushroom datasets into structured formats suitable for machine learning. Advanced feature engineering allowed us to extract meaningful insights.
        - **Model Development**: Utilizing algorithms like Decision Trees, Random Forests, and Neural Networks, we fine-tuned models to deliver high classification accuracy.
        - **User Experience Design**: The interface was carefully designed to ensure ease of use while maintaining a visually engaging aesthetic.
        - **Workflow Automation**: Automated pipelines for training, testing, and deploying models ensured seamless integration between back-end logic and the front-end application.
        """
    )

    # Team Section
    st.header("🌟 Meet the Team")
    st.write(
        """
        Our dedicated team brings expertise in machine learning, software development, and mycology to create an impactful project. Here's a closer look at our team members:
        """
    )

    head_members = [
        {
            "name": "Alice Smith",
            "role": "Project Lead and Data Scientist",
            "bio": "Alice specializes in data-driven solutions and model optimization. She ensures the project's success with her leadership and expertise in AI.",
            "image": "D:\Mushroom Project\images\mushroom2.jpg"
        },
        {
            "name": "Bob Johnson",
            "role": "Machine Learning Engineer",
            "bio": "Bob focuses on building robust and efficient machine learning models, ensuring high accuracy and reliability in predictions.",
            "image": "D:\Mushroom Project\images\mushroom2.jpg"
        }
    ]
    # Create team member profiles
    team_members = [
        {
            "name": "Alice Smith",
            "role": "Project Lead and Data Scientist",
            "bio": "Alice specializes in data-driven solutions and model optimization. She ensures the project's success with her leadership and expertise in AI.",
            "image": "D:\Mushroom Project\images\mushroom2.jpg"
        },
        {
            "name": "Bob Johnson",
            "role": "Machine Learning Engineer",
            "bio": "Bob focuses on building robust and efficient machine learning models, ensuring high accuracy and reliability in predictions.",
            "image": "D:\Mushroom Project\images\mushroom2.jpg"
        },
        {
            "name": "Carla Davis",
            "role": "Frontend Developer and UI Designer",
            "bio": "Carla designs user-friendly interfaces that make the app accessible to everyone. Her creativity brings the project to life.",
            "image": "D:\Mushroom Project\images\mushroom2.jpg"
        },
        {
            "name": "David Lee",
            "role": "Researcher and Mushroom Expert",
            "bio": "David brings extensive knowledge of mycology and ensures the accuracy of mushroom classifications through his research.",
            "image": "D:\Mushroom Project\images\mushroom2.jpg"
        }
    ]


    #display head members 
    cols = st.columns(len(head_members))
    for col, member in zip(cols, head_members):
        with col:
            st.image(member["image"], use_container_width=True, caption=member["name"])
            st.subheader(member["name"])
            st.write(f"**{member['role']}**")
            st.write(member["bio"])
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

    # Display team members in columns
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            st.image(member["image"], use_container_width=True, caption=member["name"])
            st.subheader(member["name"])
            st.write(f"**{member['role']}**")
            st.write(member["bio"])

    # Contact Section
    st.header("📬 Get in Touch")
    st.write(
        """
        Connect with us:
        
        - **GitHub Repository**: [Visit Here](https://github.com/)
        - **Email**: developerhub@example.com
        - **LinkedIn**: [Our Profile](https://linkedin.com/)
        """
    )

    # Footer with social links
    st.markdown('<div class="footer">Created with ❤️ byTeam</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    app()
