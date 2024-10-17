# import streamlit as st
# from detector import detection
# import os
# import base64
# import io
# import numpy as np
# from PIL import Image
# from streamlit_option_menu import option_menu

# # Function to encode image to base64
# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# # Set page configuration
# st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# # Load the background image and convert it to base64
# background_image = get_base64_image("./bgimg.jpg")

# # Sidebar Menu
# with st.sidebar:
#     st.image("./logo.jpg", width=150)  # Logo image path
#     selected = option_menu("Main Menu", ["Home", 'Downloads', 'About',  'Contact Us'],
#                         icons=['house', 'cloud-arrow-down', 'info-square', 'envelope', ], menu_icon="cast", default_index=0,
#                         styles={"nav-link-selected": {"background-color": "green"}})

# # Initialize the session state
# # if "page" not in st.session_state:
# #     st.session_state.page = "Home"

# # Home Page
# if selected == "Home":
#     # Custom CSS for background image
#     page_bg_img = f'''
#     <style>
#         .stApp {{
#             background-image: url("data:image/jpg;base64,{background_image}");
#             background-size: cover;
#         }}
#         /* Minimalist Sidebar styling */
#         [data-testid=stSidebar] {{
#             background-color: white;
#             padding: 20px;
#         }}
#         /* Sidebar link styling */
#         .sidebar-link {{
#             display: block;
#             padding: 10px 0;
#             font-size: 18px;
#             color: #333;
#             text-decoration: none;
#         }}
#         .sidebar-link:hover {{
#             color: #ff0000;
#         }}
#         /* Adjust the form's styling */
#         .stForm {{
#             background-color: rgba(255, 255, 255, 0.8);
#             padding: 20px;
#             border-radius: 10px;
#         }}
#         h1 {{
#             color: lightgray;
#         }}
#     </style>
#     '''
#     # Inject custom CSS
#     st.markdown(page_bg_img, unsafe_allow_html=True)

#     st.title("Hand Fracture X-Ray Detection")

#     # Form for patient information and image upload
#     with st.form(key='patient_info_form'):
#         st.subheader("Patient Information")
#         patient_name = st.text_input("Patient Name")
#         age = st.number_input("Age", min_value=0)
#         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

#         # Image Upload
#         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

#         # Detect button
#         detect_button = st.form_submit_button("Detect")

#         if detect_button:
#             if uploaded_image is not None:
#                 with open("temp_image.jpg", "wb") as f:
#                     f.write(uploaded_image.getbuffer())

#                 # Display uploaded image
#                 st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

#                 # Run YOLOv8 detection on the uploaded image
#                 detected_image = detection("temp_image.jpg")

#                 # Display the detected image
#                 st.image(detected_image, caption="Detection Results", use_column_width=False)
#             else:
#                 st.error("Please upload an image.")

#         # X-Ray Details input below images
#         xray_details = st.text_area("X-Ray Details")

#         # Final Submit button to save patient info
#         submit_button = st.form_submit_button("Submit Patient Info")

#         if submit_button:
#             # Write patient information to a text file
#             with open("patient_info.txt", "a") as f:
#                 f.write(f"Patient Name: {patient_name}\n")
#                 f.write(f"Age: {age}\n")
#                 f.write(f"Gender: {gender}\n")
#                 f.write(f"X-Ray Details: {xray_details}\n\n")
#             st.success("Patient information saved successfully.")

# elif selected == 'Downloads':
#     st.header('Downloads', divider='rainbow')
#     st.write(':green[**Dataset:**    **https://www.kaggle.com/code/yousefzidan101/skindiseas/input**]')
#     st.write(':green[**Code:**]')

# elif selected == 'About':
#     st.header('About', divider='rainbow')
#     st.write(':blue[**Draikin is a prediagnostic progressive web app that helps to scan and analyse skin pathology.**]')

# else:
#     st.header('Contact Us', divider='rainbow')
#     st.write(':blue[If you have any questions about this Progressive Web App. You can contact us:]')
#     st.write(':green[**By email: motubas@gmail.com**]')

# st.sidebar.success('Select the above page')


# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# import streamlit as st 
# from detector import detection
# import os
# import base64
# import io
# import numpy as np
# from PIL import Image
# from streamlit_option_menu import option_menu

# # Function to encode image to base64
# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# # Set page configuration
# st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# # Load the background image and convert it to base64
# background_image = get_base64_image("./bgimg.jpg")



# page_bg_img = f'''
# <style>
#         /* Minimalist Sidebar styling */
#         [data-testid=stSidebar] {{
#             background-color: white;
#             padding: 20px;
#         }}
#         /* Sidebar link styling */
#         .sidebar-link {{
#             display: block;
#             padding: 10px 0;
#             font-size: 18px;
#             color: #333;
#             text-decoration: none;
#         }}
#         .sidebar-link:hover {{
#             color: #ff0000;
#         }}
# </style>
# '''

# # Inject custom CSS
# st.markdown(page_bg_img, unsafe_allow_html=True)



# # Sidebar Menu
# with st.sidebar:
#     # Custom CSS to adjust the logo position
#     st.markdown(
#         '''
#         <style>
#             /* Move the logo upwards by 100px */
#             img {
#                 margin-top: -100px;  
#             }
#         </style>
#         ''',
#         unsafe_allow_html=True
#     )
#     # Increase logo width
#     st.image("./logo.jpg", width=200, use_column_width=False, output_format="auto", caption="")  # Increase logo width
#     selected = option_menu("Main Menu", ["Home", 'Downloads', 'About',  'Contact Us'],
#                         icons=['house', 'cloud-arrow-down', 'info-square', 'envelope', ], menu_icon="cast", default_index=0,
#                         styles={"nav-link-selected": {"background-color": "green"}})

# # Initialize the session state
# # if "page" not in st.session_state:
# #     st.session_state.page = "Home"

# # Home Page
# if selected == "Home":
#     # Custom CSS for background image
#     page_bg_img = f'''
#     <style>
#         .stApp {{
#             background-image: url("data:image/jpg;base64,{background_image}");
#             background-size: cover;
#         }}
#         /* Minimalist Sidebar styling */
#         [data-testid=stSidebar] {{
#             background-color: white;
#             padding: 20px;
#         }}
#         /* Sidebar link styling */
#         .sidebar-link {{
#             display: block;
#             padding: 10px 0;
#             font-size: 18px;
#             color: #333;
#             text-decoration: none;
#         }}
#         .sidebar-link:hover {{
#             color: #ff0000;
#         }}
#         /* Adjust the form's styling */
#         .stForm {{
#             background-color: rgba(255, 255, 255, 0.8);
#             padding: 20px;
#             border-radius: 10px;
#         }}
#         h1 {{
#             color: lightgray;
#         }}
#     </style>
#     '''
#     # Inject custom CSS
#     st.markdown(page_bg_img, unsafe_allow_html=True)

#     st.title("Hand Fracture X-Ray Detection")

#     # Form for patient information and image upload
#     with st.form(key='patient_info_form'):
#         st.subheader("Patient Information")
#         patient_name = st.text_input("Patient Name")
#         age = st.number_input("Age", min_value=0)
#         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

#         # Image Upload
#         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

#         # Detect button
#         detect_button = st.form_submit_button("Detect")

#         if detect_button:
#             if uploaded_image is not None:
#                 with open("temp_image.jpg", "wb") as f:
#                     f.write(uploaded_image.getbuffer())

#                 # Display uploaded image
#                 st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

#                 # Run YOLOv8 detection on the uploaded image
#                 detected_image = detection("temp_image.jpg")

#                 # Display the detected image
#                 st.image(detected_image, caption="Detection Results", use_column_width=False)
#             else:
#                 st.error("Please upload an image.")

#         # X-Ray Details input below images
#         xray_details = st.text_area("X-Ray Details")

#         # Final Submit button to save patient info
#         submit_button = st.form_submit_button("Submit Patient Info")

#         if submit_button:
#             # Write patient information to a text file
#             with open("patient_info.txt", "a") as f:
#                 f.write(f"Patient Name: {patient_name}\n")
#                 f.write(f"Age: {age}\n")
#                 f.write(f"Gender: {gender}\n")
#                 f.write(f"X-Ray Details: {xray_details}\n\n")
#             st.success("Patient information saved successfully.")

# elif selected == 'Downloads':
#     st.header('Downloads', divider='rainbow')
#     st.write(':green[**Dataset:**    **https://www.kaggle.com/code/yousefzidan101/skindiseas/input**]')
#     st.write(':green[**Code:**]')

# elif selected == 'About':
#     st.header('About', divider='rainbow')
#     st.write(':blue[**Draikin is a prediagnostic progressive web app that helps to scan and analyse skin pathology.**]')

# else:
#     st.header('Contact Us', divider='rainbow')
#     st.write(':blue[If you have any questions about this Progressive Web App. You can contact us:]')
#     st.write(':green[**By email: motubas@gmail.com**]')

# st.sidebar.success('Select the above page')



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import streamlit as st 
from detector import detection
import base64
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page configuration
st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# Load the background image and convert it to base64
background_image = get_base64_image("./bgimg.jpg")

# Custom CSS for styling
page_bg_img = f'''
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image}");
        background-size: cover;
    }}
    /* Minimalist Sidebar styling */
    [data-testid=stSidebar] {{
        background-color: white;
        padding: 20px;
    }}
    /* Sidebar link styling */
    .sidebar-link {{
        display: block;
        padding: 10px 0;
        font-size: 18px;
        color: #333;
        text-decoration: none;
    }}
    .sidebar-link:hover {{
        color: #ff0000;
    }}
</style>
'''

# Inject custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    # Custom CSS to adjust the logo position
    st.markdown(
        '''
        <style>
            /* Move the logo upwards by 100px */
            img {{
                margin-top: -100px;  
            }}
        </style>
        ''',
        unsafe_allow_html=True
    )
    # Increase logo width
    st.image("./logo.jpg", width=200, caption="")  # Increase logo width
    selected = option_menu("Main Menu", ["Home", 'Downloads', 'About',  'Contact Us'],
                        icons=['house', 'cloud-arrow-down', 'info-square', 'envelope'], 
                        menu_icon="cast", default_index=0,
                        styles={"nav-link-selected": {"background-color": "green"}})

# Home Page
if selected == "Home":
    st.title("Hand Fracture X-Ray Detection")

    # Form for patient information and image upload
    with st.form(key='patient_info_form'):
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0)
        gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

        # Image Upload
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

        # Detect button
        detect_button = st.form_submit_button("Detect")

        if detect_button:
            if uploaded_image is not None:
                with open("temp_image.jpg", "wb") as f:
                    f.write(uploaded_image.getbuffer())

                # Display uploaded image
                st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

                # Run YOLOv8 detection on the uploaded image
                detected_image = detection("temp_image.jpg")  # Get the annotated image

                # Check if detected_image is not None before displaying
                if detected_image is not None:
                    # Display the detected image
                    st.image(detected_image, caption="Detection Results", use_column_width=False)
                else:
                    st.error("Detection failed. Please try again.")
            else:
                st.error("Please upload an image.")

        # X-Ray Details input below images
        xray_details = st.text_area("X-Ray Details")

        # Final Submit button to save patient info
        submit_button = st.form_submit_button("Submit Patient Info")

        if submit_button:
            # Write patient information to a text file
            with open("patient_info.txt", "a") as f:
                f.write(f"Patient Name: {patient_name}\n")
                f.write(f"Age: {age}\n")
                f.write(f"Gender: {gender}\n")
                f.write(f"X-Ray Details: {xray_details}\n\n")
            st.success("Patient information saved successfully.")

elif selected == 'Downloads':
    st.header('Downloads', divider='rainbow')
    st.write(':green[**Dataset:**    **https://www.kaggle.com/code/yousefzidan101/skindiseas/input**]')
    st.write(':green[**Code:**]')

elif selected == 'About':
    st.header('About', divider='rainbow')
    st.write(':blue[**Draikin is a prediagnostic progressive web app that helps to scan and analyse skin pathology.**]')

else:
    st.header('Contact Us', divider='rainbow')
    st.write(':blue[If you have any questions about this Progressive Web App. You can contact us:]')
    st.write(':green[**By email: motubas@gmail.com**]')

st.sidebar.success('Select the above page')