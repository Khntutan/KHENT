
import streamlit as st
from PIL import Image
import io

def create_biography():
    # Header for the app
    st.title("My own Biography")

    # Collect basic information
    st.header("Personal Information")
    name = st.text_input("Khent lorenz paqueros:")
    birth_date = st.date_input("November, 06, 2005:")
    birth_place = st.text_input("Baleguian, Jabonga, Agusan del Norte")

    # Collect details for career, education, and achievements
    st.header("Background Details")
    education = st.text_area("Graduate at Taganto National High School")
    achievements = st.text_area("Honor Student")
    
    # Collect hobbies and family details
    st.header("Hobbies and Family")
    hobbies = st.text_area("Cooking and Watching movie")
    
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
        **Date of Birth:** {Novemtber, 06, 2005.}
        **Place of Birth:** {Baleguian, Jabonga, Agusan del Norte}
        
        **Education:**
        {Graduate in Taganito National High School}
        
        **Achievements:**
        {Honor Student and 2nd Pingpong player in Intramurals}
        
        **Hobbies/Interests:**
        {I like cooking, reading books, writing peoms, and playing online games}
        
        **Family:**
        {My dad is Nino M. Paqueros and my mom is Florencita B. Paquerod}
        
        **Additional Information:**
        {My siblings name are Francis Ivan B. Paqueros and Khyn Dexter B. Paqueros}
        """
        
        # Display the biography in markdown format
        st.markdown(biography)

# Run the function to create the app
create_biography()
