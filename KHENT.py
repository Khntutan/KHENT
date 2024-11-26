import streamlit as st
from PIL import Image
import io

def create_biography():
    # Header for the app
    st.title("Interactive Biography Generator")

    # Collect basic information
    st.header("Personal Information")
    name = st.text_input("Enter your full name:")
    birth_date = st.date_input("Select your date of birth:")
    birth_place = st.text_input("Enter your place of birth:")

    # Collect details for career, education, and achievements
    st.header("Background Details")
    education = st.text_area("Enter your education background:")
    career = st.text_area("Enter your career details:")
    achievements = st.text_area("Enter your achievements:")
    
    # Collect hobbies and family details
    st.header("Hobbies and Family")
    hobbies = st.text_area("Enter your hobbies or interests:")
    family = st.text_area("Enter your family details (optional):")
    
    # Optional additional information
    st.header("Additional Information")
    additional_info = st.text_area("Enter any additional information (optional):")
    
    # Image upload for profile picture
    st.header("Profile Picture (Optional)")
    image_file = st.file_uploader("https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/462617095_885906273639494_5384351385961036595_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeEo4FhRajkDbb-17-1R_GZzlP8O3xJa6vSU_w7fElrq9ApvZtlOoGOR2n4t96ZIR8pB8NY3N3z39843ACNxvKCm&_nc_ohc=OnUwvwWI32QQ7kNvgF0JCLL&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=A3b8_mJymsNQnZTBj1kaUPU&oh=00_AYAh8wlVuMTPnSC75k3UMT6XbBmvq4eqDw_W5j8ipECXlQ&oe=674B6FCD", type=["jpg", "png", "jpeg"])
    
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
        
        **Career:**
        {career}
        
        **Achievements:**
        {achievements}
        
        **Hobbies/Interests:**
        {hobbies}
        
        **Family:**
        {family}
        
        **Additional Information:**
        {additional_info}
        """
        
        # Display the biography in markdown format
        st.markdown(biography)

# Run the function to create the app
create_biography()
