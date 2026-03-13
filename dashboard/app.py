import streamlit as st
import requests

st.set_page_config(page_title="CureForge AI – Autonomous Research Institute", layout="wide")

st.title("🔬 CureForge AI Dashboard")
st.write("Autonomous clinical research, knowledge graphs, and multi-level validation.")

with st.form("simulation_form"):
    topic = st.text_input("Enter Research Topic", value="Neurodegeneration therapy")
    submitted = st.form_submit_button("Run 6-Step Research Cycle")

if submitted:
    with st.spinner("Spawning Global Director and running 6-Step Pipeline..."):
        try:
            res = requests.post("http://localhost:8000/simulate", json={"topic": topic})
            if res.status_code == 200:
                data = res.json()
                st.success("Research Cycle Complete!")
                
                # Expandable sections for each layer response
                with st.expander("🌐 Domain Research Results", expanded=True):
                    domain_data = data.get("domain_results", {})
                    st.write(f"**Domain Supervisor:** {domain_data.get('domain')}")
                    st.write(f"**Summary:** {domain_data.get('summary')}")
                    st.json(domain_data.get('worker_outputs', []))

                with st.expander("🧪 Hypothesis & Validation (Levels 1-5)", expanded=True):
                    st.write(f"**Generated Hypothesis:** {data.get('hypothesis')}")
                    val_data = data.get("validation_framework", {})
                    st.metric(label="Overall Plausibility Score", value=f"{val_data.get('overall_score', 0)*100}%")
                    st.json(val_data)
                
                with st.expander("🧬 Digital Twin Simulation", expanded=False):
                    st.json(data.get("simulation", {}))
                
                with st.expander("🕸️ Knowledge Graph Archive", expanded=False):
                    st.info(data.get("knowledge_graph_status"))
            else:
                st.error(f"API Error: {res.status_code}")
        except Exception as e:
            st.warning("API server might not be running. Run `python main.py` first.")
            st.error(str(e))
