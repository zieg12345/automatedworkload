import streamlit as st
import pandas as pd
import io
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
       ubtext-align: center;
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
            st.session_state.uploaded_file = None
        if st.button("EMAIL BLAST", help="Access Email Blast File Uploader"):
            st.session_state.button1_clicked = False
            st.session_state.button2_clicked = True
            st.session_state.button3_clicked = False
            st.session_state.uploaded_file = None
        if st.button("REPORT", help="Placeholder for future feature"):
            st.session_state.button1_clicked = False
            st.session_state.button2_clicked = False
            st.session_state.button3_clicked = True
            st.session_state.uploaded_file = None
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
        # Viber Blast functionality
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
                st.rerun()

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

        # Dynamic filename
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
                    
                    # Download button for summary table (CSV UTF-8 with BOM)
                    csv_content = summary_df.to_csv(index=False)
                    csv_with_bom = '\ufeff' + csv_content  # Add UTF-8 BOM
                    st.download_button(
                        label="📥 Download Summary Table as CSV",
                        data=csv_with_bom.encode('utf-8'),
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
            # Download button for sample data (CSV UTF-8 with BOM)
            csv_content = sample_df.to_csv(index=False)
            csv_with_bom = '\ufeff' + csv_content  # Add UTF-8 BOM
            st.download_button(
                label="📥 Download",
                data=csv_with_bom.encode('utf-8'),
                file_name=f"{current_date}.csv",
                mime="text/csv",
                key="download_sample"
            )
            st.info("Please upload a CSV file to generate the summary table with your data.")
    elif st.session_state.button2_clicked:
        # Email Blast functionality
        st.subheader("Email Blast File Uploader")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "📤 Choose a CSV or Excel file",
            type=["csv", "xlsx"],
            key="email_blast_uploader",
            help="Upload a CSV or Excel (.xlsx) file with columns: Contract Number, Email, {{chname}}, Statement Balance (OB), Statement Overdue Amount (MYP), Statement Minimum Payment (MAD), Assignment Date, TEMPLATE 1 D1, TEMPLATE 1 D2, etc."
        )
        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
            st.success("File uploaded successfully!")

        # Reset button
        if st.session_state.uploaded_file is not None:
            if st.button("🔄 Reset", help="Clear the uploaded file and reset"):
                st.session_state.uploaded_file = None
                st.session_state.button2_clicked = False
                st.rerun()

        if st.session_state.uploaded_file is not None:
            try:
                # Determine file type and read accordingly
                if st.session_state.uploaded_file.name.endswith('.csv'):
                    # Read CSV and explicitly set Contract Number as string
                    df = pd.read_csv(st.session_state.uploaded_file, dtype={"Contract Number": str})
                elif st.session_state.uploaded_file.name.endswith('.xlsx'):
                    # Read Excel and explicitly set Contract Number as string
                    df = pd.read_excel(st.session_state.uploaded_file, engine='openpyxl', dtype={"Contract Number": str})

                # Debug: Display detected column names in an expander
                with st.expander("🔍 Show Detected Column Names"):
                    st.write("Detected Column Names:", list(df.columns))

                # Define the required columns for the summary table
                required_columns = [
                    "Contract Number", "Email", "{{chname}}", "Statement Balance (OB)",
                    "Statement Overdue Amount (MYP)", "Statement Minimum Payment (MAD)",
                    "Assignment Date", "TEMPLATE 1 D1", "TEMPLATE 1 D2", "TEMPLATE 2 D1",
                    "TEMPLATE 2 D2", "TEMPLATE 3 D1", "TEMPLATE 3 D2", "TEMPLATE 4 D1",
                    "TEMPLATE 4 D2", "TEMPLATE 5 D1", "TEMPLATE 5 D2", "TEMPLATE 6 D1",
                    "TEMPLATE 6 D2"
                ]

                # Check if all required columns exist
                missing_columns = [col for col in required_columns if col not in df.columns]
                if missing_columns:
                    st.error(f"The following required columns are missing in the file: {', '.join(missing_columns)}")
                else:
                    # Create the summary table DataFrame
                    summary_df = pd.DataFrame()

                    # Populate the summary table
                    summary_df["Contract Number"] = df["Contract Number"]  # Already string, no conversion needed
                    summary_df["Email"] = df["Email"]
                    summary_df["{{chname}}"] = df["{{chname}}"]
                    summary_df["{{agentcode}}"] = ""  # Leave blank
                    summary_df["{{ID}}"] = ""  # Leave blank
                    
                    # Convert to numeric and format with thousand separators, 2 decimals
                    summary_df["{{OB}}"] = pd.to_numeric(df["Statement Balance (OB)"], errors='coerce').apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
                    summary_df["{{MYP}}"] = pd.to_numeric(df["Statement Overdue Amount (MYP)"], errors='coerce').apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
                    summary_df["{{MAD}}"] = pd.to_numeric(df["Statement Minimum Payment (MAD)"], errors='coerce').apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
                   682                    summary_df["{{OB+CF}}"] = pd.to_numeric(df["Statement Balance (OB)"], errors='coerce') * 1.2
                    summary_df["{{OB+CF}}"] = summary_df["{{OB+CF}}"].apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
                    summary_df["{{MAD+CF}}"] = pd.to_numeric(df["Statement Minimum Payment (MAD)"], errors='coerce') * 1.2
                    summary_df["{{MAD+CF}}"] = summary_df["{{MAD+CF}}"].apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
                    summary_df["{{MYP+CF}}"] = pd.to_numeric(df["Statement Overdue Amount (MYP)"], errors='coerce') * 1.2
                    summary_df["{{MYP+CF}}"] = summary_df["{{MYP+CF}}"].apply(lambda x: f"{x:,.2f}" if pd.notnull(x) else "")
                    
                    summary_df["Assignment Date"] = ""  # Leave blank
                    summary_df["TEMPLATE 1 D1"] = df["TEMPLATE 1 D1"]
                    summary_df["TEMPLATE 1 D2"] = df["TEMPLATE 1 D2"]
                    summary_df["TEMPLATE 2 D1"] = df["TEMPLATE 2 D1"]
                    summary_df["TEMPLATE 2 D2"] = df["TEMPLATE 2 D2"]
                    summary_df["TEMPLATE 3 D1"] = df["TEMPLATE 3 D1"]
                    summary_df["TEMPLATE 3 D2"] = df["TEMPLATE 3 D2"]
                    summary_df["TEMPLATE 4 D1"] = df["TEMPLATE 4 D1"]
                    summary_df["TEMPLATE 4 D2"] = df["TEMPLATE 4 D2"]
                    summary_df["TEMPLATE 5 D1"] = df["TEMPLATE 5 D1"]
                    summary_df["TEMPLATE 5 D2"] = df["TEMPLATE 5 D2"]
                    summary_df["TEMPLATE 6 D1"] = df["TEMPLATE 6 D1"]
                    summary_df["TEMPLATE 6 D2"] = df["TEMPLATE 6 D2"]

                    # Define columns to check for blank or None values
                    columns_to_check = [
                        "Email", "{{chname}}", "{{OB}}", "{{MYP}}", "{{MAD}}",
                        "{{OB+CF}}", "{{MAD+CF}}", "{{MYP+CF}}"
                    ]

                    # Remove rows where any specified column is None or blank
                    summary_df = summary_df.dropna(subset=columns_to_check)
                    summary_df = summary_df[~(summary_df[columns_to_check] == "").any(axis=1)]

                    # Display the summary table
                    st.subheader("Summary Table")
                    if not summary_df.empty:
                        st.dataframe(summary_df, use_container_width=True)
                        # Add spacing
                        st.markdown("<br>", unsafe_allow_html=True)
                        # Provide download option for Excel
                        output = io.BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            summary_df.to_excel(writer, index=False, sheet_name='Summary')
                        excel_data = output.getvalue()
                        today = datetime.now().strftime("%B %d %Y")
                        file_name = f"B2 Email blasting {today}.xlsx"
                        st.download_button(
                            label="📥 Download Summary Table as Excel Workbook",
                            data=excel_data,
                            file_name=file_name,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key="download_email_summary",
                            use_container_width=True
                        )
                    else:
                        st.warning("No rows remain after removing those with blank or None values in Email, {{chname}}, {{OB}}, {{MYP}}, {{MAD}}, {{OB+CF}}, {{MAD+CF}}, or {{MYP+CF}} fields.")
            except Exception as e:
                st.error(f"An error occurred while processing the file: {str(e)}")
        else:
            st.info("Please upload a CSV or Excel file to generate the summary table.")
    elif st.session_state.button3_clicked:
        # Placeholder for REPORT
        st.subheader("Report")
        st.info("This feature is under development.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Viber Blast Uploader | Version 1.0 | May 27, 2025 05:20 PM PST</div>', unsafe_allow_html=True)
