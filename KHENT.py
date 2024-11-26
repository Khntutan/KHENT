import streamlit as st
from PIL import Image

def create_biography():
    # Header for the app
    st.title("My Own Biography")

    # Collect basic information
    st.header("Personal Information")
    name = st.text_input("Full Name", "Khent Lorenz Paqueros")
    birth_date = st.date_input("Date of Birth", value="2005-11-06")
    birth_place = st.text_input("Place of Birth", "Baleguian, Jabonga, Agusan del Norte")

    # Collect details for career, education, and achievements
    st.header("Background Details")
    education = st.text_area("Education", "Graduate at Taganito National High School")
    achievements = st.text_area("Achievements", "Honor Student")

    # Collect hobbies and family details
    st.header("Hobbies and Family")
    hobbies = st.text_area("Hobbies", "Cooking and Watching Movies")
    family = st.text_area("Family", "Dad: Nino M. Paqueros, Mom: Florencita B. Paqueros")

    # Image upload for profile picture
    st.header("Profile Picture (Optional)")
    image_file = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"])

    if image_file is not None:
        # Load and display the image
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate the biography once the user presses the button
    if st.button("Generate Biography"):
        biography = f"""
        **Biography of {name}:**
        ---------------------
        **Name:** {name}
        **Date of Birth:** {birth_date.strftime('%B %d, %Y')}
        **Place of Birth:** {birth_place}
        
        **Education:**
        {education}
        
        **Achievements:**
        {achievements}
        
        **Hobbies/Interests:**
        {hobbies}
        
        **Family:**
        {family}
        """
        
        # Display the biography in markdown format
        st.markdown(biography)

# Run the function to create the app
create_biography()
