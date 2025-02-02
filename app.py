import streamlit as st  # Import the Streamlit library for building web apps
from pdf_extract_to_excel.generate_excel import populate_excel  # Import the pdf_processing function from the extract_pdf_to_json module
import io  # Import io for handling file streams
import tempfile

# Setup Streamlit
st.set_page_config(page_title="Extraction", page_icon=":tada", layout="wide")  # Set the page configuration for the Streamlit app
st.title(f"AutAudit : extraire les données des bails commerciaux")  # Display the title of the app
# Create a container for the file uploader and button
with st.container():
    st.write("---")  # Add a horizontal line separator
    uploaded_file = st.file_uploader('Upload a .pdf file', type="pdf")  # Create a file uploader for PDF files
    st.write("---")  # Add another horizontal line separator

go = st.button("Go!")  # Create a button labeled "Go!"

# Check if the "Go!" button is clicked
excel_filename = "Tableau_audit_immo_modele.xlsx"  # Define the name of the Excel file
if go and uploaded_file is not None:
    st.toast("Extraction") # Display a toast message
    
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    out_path = io.BytesIO()
    populate_excel(excel_filename, out_path, pdfs_path=[temp_file_path])  # Pass the path of the temporary file
    out_path.seek(0)

    st.download_button(
        label="Download Excel",
        data=out_path,
        file_name=excel_filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )  # Create a download button for the Excel file