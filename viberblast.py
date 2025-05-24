import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Initialize session state
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False
if 'button3_clicked' not in st.session_state:
    st.session_state.button3_clicked = False
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'menu_open' not in st.session_state:
    st.session_state.menu_open = False

# Set page configuration
st.set_page_config(page_title="WORKLOADS-AUTOMATED", page_icon="📊", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    /* Monochromatic theme (refined grays) */
    .main-content {
        padding: 20px;
        background-color: #f5f5f5; /* Lighter gray */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #2b2b2b; /* Darker gray text */
        margin-bottom: 20px;
    }
    /* Sidebar styling */
    .css-1lcbmhc { 
        background-color: #e0e0e0; /* Slightly lighter gray */
        padding: 20px; 
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    /* Button styling */
    .stButton > button {
        width: 100%;
        margin-bottom: 10px;
        background-color: #b0b0b0; /* Medium gray */
        color: #2b2b2b; /* Darker text */
        border: none;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #909090; /* Darker gray on hover */
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    /* Download button styling */
    .stDownloadButton > button {
        background-color: #b0b0b0;
        color: #2b2b2b;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease;
    }
    .stDownloadButton > button:hover {
        background-color: #909090;
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    /* Center title */
    h1 {
        text-align: center;
        color: #2b2b2b;
    }
    /* Burger menu button */
    .burger-button {
        font-size: 24px;
        cursor: pointer;
        color: #2b2b2b;
        margin-bottom: 10px;
        background: none;
        border: none;
        padding: 5px;
    }
    /* Sidebar content */
    .sidebar-content {
        display: none;
    }
    .sidebar-content.active {
        display: block;
    }
    /* Dataframe styling */
    .stDataFrame {
        border: 1px solid #d0d0d0;
        border-radius: 5px;
        background-color: #ffffff;
    }
    /* Footer */
    .footer {
        text-align: center;
        color: #666666;
        margin-top: 20px;
        font-size: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# List of revised motivational quotes, all attributed to Zieg
motivational_quotes = [
    "Trust in your inner strength—you’ve already crossed half the journey. – Zieg",
    "Exceptional work blooms from a heart that loves its craft. – Zieg",
    "True success lies in the bravery to press forward despite challenges. – Zieg",
    "The boundaries you see are merely shadows of your own imagination. – Zieg",
    "Set grand goals, toil relentlessly, remain steadfast, and choose wise companions. – Zieg",
    "Tomorrow is crafted by those who envision their dreams with wonder. – Zieg",
    "Don’t follow the ticking clock—mirror its persistence and keep advancing. – Zieg",
    "No age can stop you from pursuing new dreams or crafting fresh ambitions. – Zieg",
    "The greatest prize of your achievements is the person you grow into. – Zieg",
    "Launch from your current place, with your present tools, and give your all. – Zieg"
]

# Select a random quote
random_quote = random.choice(motivational_quotes)

# Header section with dynamic motivational quote
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.title(random_quote)

# Sidebar with burger menu
with st.sidebar:
    # Toggle button for sidebar (burger icon ☰)
    if st.session_state.menu_open:
        if st.button("✕ Close", key="close_menu", help="Close the menu"):
            st.session_state.menu_open = False
    else:
        if st.button("☰", key="burger_menu", help="Open the menu"):
            st.session_state.menu_open = True

    # Sidebar content
    if st.session_state.menu_open:
        st.markdown('<div class="sidebar-content active">', unsafe_allow_html=True)
        
        # Buttons with hover and shadow
        if st.button("VIBER BLAST", help="Access Viber Blast CSV Uploader"):
            st.session_state.button1_clicked = True
            st.session_state.button2_clicked = False
            st.session_state.button3_clicked = False
        if st.button("EMAIL BLAST", help="Placeholder for future feature"):
            st.session_state.button1_clicked = False
            st.session_state.button2_clicked = True
            st.session_state.button3_clicked = False
        if st.button("REPORT", help="Placeholder for future feature"):
            st.session_state.button1_clicked = False
            st.session_state.button2_clicked = False
            st.session_state.button3_clicked = True
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Main content
with st.container():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Default welcome message
    if not (st.session_state.button1_clicked or st.session_state.button2_clicked or st.session_state.button3_clicked):
        st.subheader("Welcome")
        st.write("Click the ☰ menu in the sidebar and select a feature to begin.")
    elif st.session_state.button1_clicked:
        # Viber Blast functionality under VIBER BLAST
        st.subheader("Viber Blast CSV Uploader")
        
        # File uploader
        uploaded_file = st.file_uploader("📤 Choose a CSV file", type=["csv"], key="viber_blast_uploader", help="Upload a CSV with columns: Client, Account No., Debtor Name, Contact No.")
        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
            st.success("File uploaded successfully!")

        # Reset button
        if st.session_state.uploaded_file is not None:
            if st.button("🔄 Reset", help="Clear the uploaded file and reset"):
                st.session_state.uploaded_file = None
                st.session_state.button1_clicked = False
                st.experimental_rerun()

        # Sample data
        sample_data = {
            "Campaign": ["SAMPLE", "SAMPLE", "SAMPLE", "SAMPLE"],
            "CH Code": ["12345", "123456", "1234567", "12345678"],
            "First Name": ["", "", "", ""],
            "Full Name": ["Richard Arenas", "Jinnggoy Dela Cruz", "Roman Dalisay", "Edwin Paras"],
            "Last Name": ["", "", "", ""],
            "Mobile Number": ["09274186327", "09760368821", "09088925110", "09175791122"],
            "OB": ["", "", "", ""]
        }
        sample_df = pd.DataFrame(sample_data)

        # Dynamic filename (updated to current date and time)
        current_date = datetime.now().strftime("VIBER BLAST %b %d %Y %I:%M %p PST").upper()

        if st.session_state.uploaded_file is not None:
            try:
                # Read the CSV file
                df = pd.read_csv(st.session_state.uploaded_file)
                
                # Check for required columns
                required_columns = ["Client", "Account No.", "Debtor Name", "Contact No."]
                missing_columns = [col for col in required_columns if col not in df.columns]
                
                if missing_columns:
                    st.error(f"The following required columns are missing: {', '.join(missing_columns)}")
                else:
                    # Process Contact No. and Account No.
                    df["Contact No."] = df["Contact No."].astype(str).str.strip().replace("nan", "")
                    df["Account No."] = df["Account No."].astype(str).str.strip().replace("nan", "")
                    
                    # Check for invalid Contact No.
                    invalid_contact_no = df[df["Contact No."].str.len() != 11]
                    if not invalid_contact_no.empty:
                        st.warning(f"Found {len(invalid_contact_no)} rows where Contact No. is not 11 digits. These rows are still included but may need review.")
                    
                    # Remove rows with "BEL" in Account No.
                    initial_row_count_bel = len(df)
                    df = df[~df["Account No."].str.contains("BEL", case=False, na=False)]
                    if initial_row_count_bel != len(df):
                        st.info(f"Removed {initial_row_count_bel - len(df)} rows where Account No. contains 'BEL'.")
                    
                    # Remove duplicates based on Account No.
                    initial_row_count = len(df)
                    df = df.drop_duplicates(subset=["Account No."], keep="first")
                    if initial_row_count != len(df):
                        st.info(f"Removed {initial_row_count - len(df)} duplicate rows based on 'Account No.'.")
                    
                    # Check if any rows remain
                    if len(df) == 0:
                        st.warning("No rows remain after filtering. Showing sample data only.")
                    
                    # Create summary table
                    summary_df = pd.DataFrame({
                        "Campaign": df["Client"],
                        "CH Code": df["Account No."],
                        "First Name": [""] * len(df),
                        "Full Name": df["Debtor Name"],
                        "Last Name": [""] * len(df),
                        "Mobile Number": df["Contact No."],
                        "OB": [""] * len(df)
                    })
                    
                    # Concatenate with sample data
                    summary_df = pd.concat([summary_df, sample_df], ignore_index=True)
                    
                    # Display summary table
                    st.subheader("Summary Table")
                    st.dataframe(summary_df, use_container_width=True)
                    
                    # Download button for summary table
                    csv = summary_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download Summary Table as CSV",
                        data=csv,
                        file_name=f"{current_date}.csv",
                        mime="text/csv",
                        key="download_summary"
                    )
                    
            except Exception as e:
                st.error(f"An error occurred while processing the file: {str(e)}")
        else:
            # Display sample data if no file is uploaded
            st.subheader("Sample Summary Table")
            st.dataframe(sample_df, use_container_width=True)
            csv = sample_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download",
                data=csv,
                file_name=f"{current_date}.csv",
                mime="text/csv",
                key="download_sample"
            )
            st.info("Please upload a CSV file to generate the summary table with your data.")
    elif st.session_state.button2_clicked:
        # Blank UI for EMAIL BLAST
        pass
    elif st.session_state.button3_clicked:
        # Blank UI for REPORT
        pass
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Viber Blast Uploader | Version 1.0 | May 24, 2025 11:40 AM PST</div>', unsafe_allow_html=True)
