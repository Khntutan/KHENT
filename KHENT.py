import streamlit as st
from PIL import Image

def create_biography():
    # Header for the app
    st.title("Khent Lorenz Paqueros Biography")

    # Pre-fill personal information
    st.header("Personal Information")
    name = st.text_input("Full Name:", "Khent Lorenz Paqueros")
    birth_date = st.date_input("Date of Birth:", value="2005-11-06")
    birth_place = st.text_input("Place of Birth:", "Baleguian, Jabonga, Agusan del Norte")

    # Collect details for career, education, and achievements
    st.header("Background Details")
    education = st.text_area("Education:", "Graduate at Taganto National High School")
    achievements = st.text_area("Achievements:", "Honor Student, 2nd Pingpong Player in Intramurals")
    
    # Collect hobbies and family details
    st.header("Hobbies and Family")
    hobbies = st.text_area("Hobbies:", "Cooking, Watching Movies, Playing Online Games")
    family_info = st.text_area("Family:", "Father: Nino M. Paqueros, Mother: Florencita B. Paqueros\nSiblings: Francis Ivan B. Paqueros, Khyn Dexter B. Paqueros")

    # Image upload for profile picture
    st.header("Profile Picture (Optional)")
    image_file = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"])

    # Display a default image if none is uploaded
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    else:
        # Default image URL (replace with your image if desired)
        default_image = "https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/462617095_885906273639494_5384351385961036595_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeEo4FhRajkDbb-17-1R_GZzlP8O3xJa6vSU_w7fElrq9ApvZtlOoGOR2n4t96ZIR8pB8NY3N3z39843ACNxvKCm&_nc_ohc=OnUwvwWI32QQ7kNvgF0JCLL&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=A3b8_mJymsNQnZTBj1kaUPU&oh=00_AYAh8wlVuMTPnSC75k3UMT6XbBmvq4eqDw_W5j8ipECXlQ&oe=674B6FCD"
        st.image(default_image, caption="Default Image", use_column_width=True)

    # Generate the biography once the user presses the button
    if st.button("Generate Biography"):
        # Format the biography with user inputs
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
        {family_info}
        """
        
        # Display the biography in markdown format
        st.markdown(biography)

# Run the function to create the app
create_biography()
