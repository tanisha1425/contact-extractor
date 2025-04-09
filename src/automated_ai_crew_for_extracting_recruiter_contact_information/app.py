import streamlit as st
from crew import AutomatedAiCrewForExtractingRecruiterContactInformationCrew

st.set_page_config(page_title="Recruiter Info Extractor", layout="centered")
st.title("🎯 Recruiter Contact Extractor")

company_name = st.text_input("Enter Company Name", placeholder="e.g., Microsoft Hyderabad")

if st.button("Run AI Crew"):
    if company_name:
        with st.spinner("🔄 Running Crew AI..."):
            try:
                crew_instance = AutomatedAiCrewForExtractingRecruiterContactInformationCrew()
                output = crew_instance.crew().kickoff(inputs={'company_name': company_name})
                st.success("✅ Done!")

                st.markdown("### Output:")
                st.markdown(output if isinstance(output, str) else str(output))

                st.download_button("Download Output", str(output), file_name="output.md")
            except Exception as e:
                st.error(f"❌ Something went wrong:\n\n{str(e)}")
    else:
        st.warning("⚠️ Please enter a company name first.")
