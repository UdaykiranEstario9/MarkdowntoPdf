import streamlit as st

# 1. Page Config
st.set_page_config(page_title="PDF Generator", page_icon="📄", layout="wide")

# 2. Session State (Keeps your text safe when switching views)
if "content" not in st.session_state:
    st.session_state["content"] = r"""
# Engineering Thesis
**Author:** Student Name

## 1. Introduction
This document demonstrates the rendering of complex **LaTeX** equations.

## 2. Theoretical Framework
The core physics is described by the time-dependent Schrödinger equation:

$$ i\hbar \frac{\partial}{\partial t} \Psi(\mathbf{r},t) = \hat{H} \Psi(\mathbf{r},t) $$

Where the Hamiltonian $\hat{H}$ is:
$$ \hat{H} = -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r},t) $$

## 3. Results
* [x] Theory Verified
* [ ] Experiment Pending
"""

# 3. CSS for Layout & Printing
# This removes the top spacing and ensures a clean print
css = """
<style>
    /* A. REMOVE TOP PADDING (The "Space" at the top) */
    .block-container {
        padding-top: 1rem !important; /* Reduce huge default top padding */
        padding-bottom: 0rem !important;
        max-width: 100% !important;
    }

    /* B. PRINT STYLING */
    @media print {
        /* Hide sidebar, header, footer, navigation */
        [data-testid="stSidebar"], header, .stAppHeader, footer, [data-testid="stRadio"] {
            display: none !important;
        }

        /* Reset background to pure white */
        .stApp {
            background: white !important;
        }
        
        /* Force text to black */
        body, p, h1, h2, h3, li, span, div {
            color: black !important;
        }
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 4. Sidebar Navigation
page = st.sidebar.radio("Navigate", ["✏️ Editor", "🖨️ Print Preview"], label_visibility="collapsed")

# --- VIEW 1: EDITOR ---
if page == "✏️ Editor":
    st.subheader("✏️ Editor")
    
    # Input Area
    new_content = st.text_area(
        "Markdown Input",
        value=st.session_state["content"],
        height=700,
        label_visibility="collapsed"
    )
    
    # Auto-Save
    if new_content != st.session_state["content"]:
        st.session_state["content"] = new_content
        st.rerun()

# --- VIEW 2: PREVIEW ---
elif page == "🖨️ Print Preview":
    # Sidebar Instructions for this view
    with st.sidebar:
        st.info("👇 **To Save as PDF:**")
        st.markdown("1. Press **Ctrl + P** (Cmd + P).")
        st.markdown("2. Select **Save as PDF**.")
        st.markdown("3. Check 'Background graphics' if math lines are missing.")

    # Render Content Directly (No extra containers/borders)
    st.markdown(st.session_state["content"])