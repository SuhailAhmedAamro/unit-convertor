import streamlit as st

# Custom CSS for styling the profile card
st.markdown("""
    <style>
        .profile-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 50%;
            margin: auto;
        }
        .profile-pic {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            border: 3px solid #007bff;
        }
        .name {
            font-size: 24px;
            font-weight: bold;
            color: #007bff;
        }
        .bio {
            font-size: 16px;
            color: #555;
        }
        .button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Profile Card
st.markdown("""
    <div class="profile-container">
        <img src="https://via.placeholder.com/150" class="profile-pic">
        <p class="name">Suhail Ahmed Aamro</p>
        <p class="bio">Web Developer | AI Enthusiast | Tech Explorer</p>
        <a href="https://github.com" target="_blank">
            <button class="button">Visit My GitHub</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# User Interaction
if st.button("Click to Say Hello"):
    st.success("Hello, welcome to my Streamlit App! 🎉")
