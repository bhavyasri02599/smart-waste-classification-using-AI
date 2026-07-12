"""
Settings Page for Smart Waste Classification Dashboard.
Configuration options for model, display, and application settings.
"""

import streamlit as st
from datetime import datetime


def render_settings_page():
    """Render the settings page with configuration options."""
    
    st.markdown("# ⚙️ Settings")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🤖 Model Settings")
        
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help="Minimum confidence score for predictions"
        )
        
        model_version = st.selectbox(
            "Model Version",
            ['YOLOv8n (Nano) - Fastest', 'YOLOv8s (Small)', 'YOLOv8m (Medium)', 'YOLOv8l (Large) - Most Accurate'],
            help="Select the YOLO model variant"
        )
        
        max_image_size = st.number_input(
            "Max Image Size (MB)",
            min_value=1,
            max_value=50,
            value=10,
            help="Maximum upload file size in megabytes"
        )
        
        auto_classify = st.checkbox(
            "Auto-classify on upload",
            value=True,
            help="Automatically classify images when uploaded"
        )
        
        st.divider()
        
        st.markdown("### 🎨 Display Settings")
        
        theme = st.selectbox(
            "Theme",
            ['Light', 'Dark', 'Auto'],
            help="Application color theme"
        )
        
        show_confidence = st.checkbox(
            "Show Confidence Score",
            value=True,
            help="Display confidence percentage in results"
        )
        
        show_recommendation = st.checkbox(
            "Show Disposal Recommendation",
            value=True,
            help="Display disposal instructions"
        )
        
        show_bounding_boxes = st.checkbox(
            "Show Bounding Boxes",
            value=True,
            help="Display detection bounding boxes on images"
        )
        
        animations = st.checkbox(
            "Enable Animations",
            value=True,
            help="Enable smooth transitions and animations"
        )
    
    with col2:
        st.markdown("### 💾 Data Settings")
        
        auto_save = st.checkbox(
            "Auto-save Predictions",
            value=True,
            help="Automatically save predictions to database"
        )
        
        retention_days = st.number_input(
            "Data Retention (days)",
            min_value=7,
            max_value=365,
            value=90,
            help="How long to keep prediction history"
        )
        
        export_format = st.selectbox(
            "Default Export Format",
            ['CSV', 'Excel', 'JSON'],
            help="Default format for data exports"
        )
        
        st.divider()
        
        st.markdown("### 🔔 Notification Settings")
        
        email_notifications = st.checkbox(
            "Email Notifications",
            value=False,
            help="Receive email alerts for system events"
        )
        
        if email_notifications:
            email = st.text_input(
                "Email Address",
                placeholder="your@email.com",
                help="Email address for notifications"
            )
        
        desktop_notifications = st.checkbox(
            "Desktop Notifications",
            value=True,
            help="Show browser notifications"
        )
        
        st.divider()
        
        st.markdown("### 🔧 Advanced Settings")
        
        debug_mode = st.checkbox(
            "Debug Mode",
            value=False,
            help="Enable debug logging and information"
        )
        
        api_timeout = st.number_input(
            "API Timeout (seconds)",
            min_value=5,
            max_value=120,
            value=30,
            help="Timeout for API requests"
        )
        
        cache_results = st.checkbox(
            "Cache Prediction Results",
            value=True,
            help="Cache results to improve performance"
        )
    
    st.divider()
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💾 Save Settings", type="primary"):
            st.success("✅ Settings saved successfully!")
            st.balloons()
    
    with col2:
        if st.button("🔄 Reset to Defaults"):
            st.warning("Settings reset to defaults")
            st.rerun()
    
    with col3:
        if st.button("📤 Export Settings"):
            st.info("Settings export coming soon!")
    
    st.divider()
    
    # System information
    st.markdown("### ℹ️ System Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Application Version:** 1.0.0  
        **Last Updated:** {date}  
        **Python Version:** 3.10+  
        **Streamlit Version:** 1.28.0+
        """.format(date=datetime.now().strftime("%Y-%m-%d")))
    
    with col2:
        st.markdown("""
        **AI Model:** YOLOv8  
        **Backend:** FastAPI  
        **Database:** SQLite  
        **Charts:** Plotly
        """)
    
    st.divider()
    
    # About section
    st.markdown("### 📚 About")
    
    st.markdown("""
    **Smart Waste Classification Dashboard** is an AI-powered system that helps identify and sort waste materials using computer vision.
    
    **Features:**
    - 🤖 Real-time waste classification using YOLO
    - 📊 Interactive dashboard with charts and analytics
    - 📜 History tracking and export functionality
    - ⚙️ Customizable settings and preferences
    
    **Technology Stack:**
    - **AI Model:** YOLOv8 for object detection and classification
    - **Backend:** FastAPI for REST API endpoints
    - **Database:** SQLite for data storage
    - **Dashboard:** Streamlit for interactive UI
    - **Charts:** Plotly for data visualization
    
    **Built with ❤️ for sustainable waste management**
    """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #888;'>"
        "© 2024 Smart Waste Classification System | Made with Streamlit"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    render_settings_page()
