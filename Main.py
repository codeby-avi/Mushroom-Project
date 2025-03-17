import streamlit as st
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import streamlit as st
from streamlit_option_menu import option_menu
import base64


def set_bg_hack_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://avi-chavan-96.sirv.com/Mushroom/parasol-4549617_1280.jpg");
            background-size: contain
            background-position: center;
            min-height: 100vh; /* Minimum height to cover the full viewport */
            height: auto; /* Adjust height based on content */
            
        }}
        </style>
        """,
        unsafe_allow_html=True)

set_bg_hack_url()

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Use pbkdf2:sha256 for secure password hashing
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False


# Authenticate a user
def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return check_password_hash(result[0], password)
    return False

# Initialize database
init_db()

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Login function
def login():
    st.markdown("<h2 style='text-align: center;'>🔒 Login</h2>", unsafe_allow_html=True)
    with st.form("Login Form", clear_on_submit=True):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit = st.form_submit_button("Login")

    if submit:
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.current_user = username
            # Persist login state in query params
            st.query_params["authenticated"] = True
            st.query_params["username"] = username
            st.success(f"👋 Welcome Back {username}!")
        else:
            st.error("Invalid username or password!")

# Signup function
def signup():
    st.markdown("<h2 style='text-align: center;'>📝 Sign Up</h2>", unsafe_allow_html=True)
    with st.form("Signup Form", clear_on_submit=True):
        new_username = st.text_input("Choose a Username", placeholder="Create a username")
        new_password = st.text_input("Choose a Password", type="password", placeholder="Create a password")
        submit = st.form_submit_button("Sign Up")

    if submit:
        if not new_username or not new_password:
            st.error("Username and password cannot be empty!")
        elif add_user(new_username, new_password):
            st.success("Account created successfully! Please log in.")
        else:
            st.error("Username already exists!")

# Main application
def app():
    
    st.title(f"Welcome, {st.session_state.current_user}!")
    st.write("")

    
    # Sidebar navigation
    with st.sidebar:

        selected = option_menu(
            menu_title="Mushroom Classifier 🍄",  # Sidebar title
            options=["Home", "Edibility Checker", "Mushroom ML Lab", "Mushroom Wisdom",  "Gallery"],  # Menu options
            icons=["house", "cpu", "cpu", "info-circle", "code-slash"],  # Icons
            menu_icon="chat-text-fill",  # Main menu icon
            default_index=0,  # Default selected option
            styles={
                "container": {"padding": "5px", "background-color": "#00172B"},
                "icon": {"color": "white", "font-size": "22px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#4CAF50",
                },
                "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
            },
        )

    # Load pages dynamically based on selection
    if selected == "Home":
            from views.Home import app
            return app()
    elif selected == "Edibility Checker":
            from views.EdibilityChecker import app
            return app()
    elif selected == "Mushroom ML Lab":
            from views.MushroomMlLab import app
            return app()
    elif selected == "Mushroom Wisdom":
            from views.MushroomWisdom import app
            return app()
    elif selected == "Gallery":
            from views.Gallery import app
            return app()


    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.current_user = None
        # Reset query parameters and reload
        st.query_params.clear()

# Main logic
try:
    authenticated = st.query_params["authenticated"]
    st.session_state.current_user =st.query_params["username"]
    if authenticated:
        app()
except Exception:
    st.sidebar.title("🍄 Mushroom Classifier")
    page = st.sidebar.radio("🔐 Authentication", ["🔒 Login", "📝 Sign Up"])
    if page == "🔒 Login":
        login()
    elif page == "📝 Sign Up":
        signup()

