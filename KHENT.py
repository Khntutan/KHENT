import streamlit as st
from PIL import Image

def create_biography():
    # Title for the app
    st.title("My Biography")

    # Collect basic information
    name = st.text_input("Full Name", "Khent Lorenz Paqueros")
    birth_date = st.date_input("Date of Birth", value="2005-11-06")
    birth_place = st.text_input("Place of Birth", "Baleguian, Jabonga, Agusan del Norte")

    # Collect education and achievements
    education = st.text_input("Education", "Taganito National High School Graduate")
    achievements = st.text_input("Achievements", "Honor Student")

    # Collect hobbies and family info
    hobbies = st.text_input("Hobbies", "Cooking and Watching Movies")
    family = st.text_input("Family", "Dad: Nino M. Paqueros, Mom: Florencita B. Paqueros")

    # Image upload for profile picture
    image_file = st.file_uploader("https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/462617095_885906273639494_5384351385961036595_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeEo4FhRajkDbb-17-1R_GZzlP8O3xJa6vSU_w7fElrq9ApvZtlOoGOR2n4t96ZIR8pB8NY3N3z39843ACNxvKCm&_nc_ohc=OnUwvwWI32QQ7kNvgF0JCLL&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=AaEP6EsvCx5DiJdmLGphIPw&oh=00_AYDhTYZjMNVCpply3hat1pqS_1c7b3nzmPXsKz1oqHsElQ&oe=674B6FCD", type=["jpg", "png", "jpeg"])

    if image_file is not None:
        # Load and display the image
        image = Image.open(image_file)
        st.image(image, caption="Profile Picture", use_column_width=True)

    # Button to generate and display the biography
    if st.button("Generate Biography"):
        biography = f"""
        **Biography of {name}:**
        ---------------------
        **Name:** {name}
        **Date of Birth:** {birth_date}
        **Place of Birth:** {birth_place}
        
        **Education:** {education}
        **Achievements:** {achievements}
        
        **Hobbies/Interests:** {hobbies}
        **Family:** {family}
        """
        
        # Display the biography
        st.markdown(biography)

# Run the function to create the app
create_biography()
