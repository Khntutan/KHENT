import streamlit as st
from PIL import Image

def create_biography():
    # Title for the app
    st.title("My Biography")

    # Personal information section
    st.header("Personal Information")
    name = st.text_input("Full Name", "Khent Lorenz Paqueros")
    birth_date = st.date_input("Date of Birth", value="2005-11-06")
    birth_place = st.text_input("Place of Birth", "Baleguian, Jabonga, Agusan del Norte")

    # Career, education, and achievements section
    st.header("Background Details")
    education = st.text_area("Education", "Graduate at Taganito National High School")
    achievements = st.text_area("Achievements", "Honor Student")

    # Hobbies and family details section
    st.header("Hobbies and Family")
    hobbies = st.text_area("Hobbies", "Cooking and Watching Movies")
    family = st.text_area("Family", "Dad: Nino M. Paqueros, Mom: Florencita B. Paqueros")

    # Image upload section for profile picture
    st.header("Profile Picture (Optional)")
    image_file = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"])

    if image_file is not None:
        # Load and display the uploaded image
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Button to generate and display the biography
    if st.button("Generate Biography"):
        biography = f"""
        **Biography of {name}:**
        ---------------------
        **Name:** {name}
        **Date of Birth:** {birth_date.strftime('%B %d, %Y')}
        **Place
