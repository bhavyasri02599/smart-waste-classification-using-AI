"""
Smart Waste Classification Dashboard
Main Streamlit application with multi-page navigation.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Smart Waste Classification Dashboard",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E86AB;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #2E86AB;
        margin-bottom: 1rem;
    }
    
    .stMetric > div {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .category-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .plastic { background-color: #d4edda; color: #155724; }
    .paper { background-color: #fff3cd; color: #856404; }
    .glass { background-color: #cce5ff; color: #004085; }
    .metal { background-color: #e2e3e5; color: #383d41; }
    .organic { background-color: #d1ecf1; color: #0c5460; }
    .e-waste { background-color: #f8d7da; color: #721c24; }
    .others { background-color: #e2e3e5; color: #383d41; }
    
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    div[data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    
    .recommendation-box {
        background-color: #e8f4f8;
        border-left: 4px solid #2E86AB;
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables."""
    if 'predictions' not in st.session_state:
        st.session_state.predictions = []
    if 'total_uploads' not in st.session_state:
        st.session_state.total_uploads = 0


def home_page():
    """Home page with overview metrics and charts."""
    st.markdown('<h1 class="main-header">♻️ Smart Waste Classification Dashboard</h1>', unsafe_allow_html=True)
    
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🗑️ Total Waste Detected",
            value=st.session_state.total_uploads,
            delta=1
        )
    
    with col2:
        st.metric(
            label="📤 Today's Uploads",
            value=5,
            delta=2
        )
    
    with col3:
        st.metric(
            label="🎯 Model Accuracy",
            value="94.2%",
            delta="2.1%"
        )
    
    with col4:
        st.metric(
            label="♻️ Recycling Rate",
            value="78.5%",
            delta="5.3%"
        )
    
    st.divider()
    
    # Charts row
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Category Distribution")
        # Sample data for pie chart
        categories = ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others']
        values = [35, 25, 15, 10, 8, 5, 2]
        colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B', '#44BBA4', '#E94F37']
        
        fig = px.pie(
            values=values,
            names=categories,
            color_discrete_sequence=colors,
            hole=0.4
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Daily Upload Trends")
        # Sample data for line chart
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        uploads = [10, 12, 15, 18, 22, 25, 28, 30, 35, 40,
                   42, 45, 48, 50, 55, 58, 60, 65, 68, 70,
                   72, 75, 78, 80, 82, 85, 88, 90, 92, 95]
        
        df_trends = pd.DataFrame({
            'Date': dates,
            'Uploads': uploads
        })
        
        fig = px.line(
            df_trends,
            x='Date',
            y='Uploads',
            line_shape='spline',
            color_discrete_sequence=['#2E86AB']
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Recent activity
    st.subheader("🕒 Recent Activity")
    
    recent_data = pd.DataFrame({
        'Time': ['2 min ago', '5 min ago', '10 min ago', '15 min ago', '20 min ago'],
        'Category': ['Plastic', 'Paper', 'Glass', 'Organic', 'Metal'],
        'Confidence': ['98.5%', '95.2%', '92.8%', '89.5%', '87.3%'],
        'Action': ['♻️ Recycle', '📄 Recycle', '🍶 Recycle', '🌱 Compost', '🥫 Recycle']
    })
    
    st.dataframe(recent_data, use_container_width=True, hide_index=True)


def upload_page():
    """Upload page for classifying waste images."""
    st.markdown('<h1 class="main-header">📤 Upload Waste Image</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Upload Image")
        
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png"],
            help="Upload an image of waste for classification"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            # Classify button
            if st.button("🔍 Classify Waste", type="primary"):
                with st.spinner("Analyzing image..."):
                    # Simulate prediction (in real app, call API)
                    import random
                    categories = ['plastic', 'paper', 'glass', 'metal', 'organic', 'e-waste', 'others']
                    weights = [0.35, 0.25, 0.15, 0.10, 0.08, 0.05, 0.02]
                    
                    category = random.choices(categories, weights=weights)[0]
                    confidence = random.uniform(0.85, 0.99)
                    
                    # Store in session state
                    prediction = {
                        'id': len(st.session_state.predictions) + 1,
                        'filename': uploaded_file.name,
                        'category': category,
                        'confidence': confidence,
                        'timestamp': datetime.now()
                    }
                    st.session_state.predictions.append(prediction)
                    st.session_state.total_uploads += 1
                    
                    st.success("Classification complete!")
                    st.rerun()
    
    with col2:
        st.subheader("Classification Results")
        
        if st.session_state.predictions:
            latest = st.session_state.predictions[-1]
            
            # Category badge
            category = latest['category']
            st.markdown(f"**Category:** <span class='category-badge {category}'>{category.upper()}</span>", 
                       unsafe_allow_html=True)
            
            # Confidence
            confidence = latest['confidence']
            st.metric("Confidence Score", f"{confidence:.1%}")
            
            # Progress bar for confidence
            st.progress(confidence)
            
            # Recommendation
            recommendations = {
                'plastic': '♻️ Place in the recycling bin. Rinse containers before disposal.',
                'paper': '📄 Place in the paper recycling bin. Remove any plastic windows.',
                'glass': '🍶 Place in the glass recycling bin. Do not break glass items.',
                'metal': '🥫 Place in the metal recycling bin. Rinse before disposal.',
                'organic': '🌱 Place in the compost bin. Can be composted at home.',
                'e-waste': '💻 Take to designated e-waste collection centers. Contains hazardous materials.',
                'others': '🗑️ Check local waste management guidelines.'
            }
            
            st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
            st.markdown(f"**Disposal Recommendation:**")
            st.info(recommendations.get(category, recommendations['others']))
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Save to database
            st.button("💾 Save to Database")
        else:
            st.info("No predictions yet. Upload an image to classify waste.")


def analytics_page():
    """Analytics page with charts and statistics."""
    st.markdown('<h1 class="main-header">📊 Analytics Dashboard</h1>', unsafe_allow_html=True)
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        date_range = st.date_input(
            "Date Range",
            value=(datetime.now() - timedelta(days=30), datetime.now())
        )
    
    with col2:
        category_filter = st.multiselect(
            "Filter by Category",
            ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others'],
            default=['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others']
        )
    
    with col3:
        chart_type = st.selectbox(
            "Chart Type",
            ['Pie Chart', 'Bar Chart', 'Line Chart', 'Heatmap']
        )
    
    st.divider()
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Category Distribution")
        
        categories = ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others']
        values = [35, 25, 15, 10, 8, 5, 2]
        colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B', '#44BBA4', '#E94F37']
        
        if chart_type == 'Pie Chart':
            fig = px.pie(values=values, names=categories, color_discrete_sequence=colors, hole=0.4)
        elif chart_type == 'Bar Chart':
            fig = px.bar(x=categories, y=values, color=categories, color_discrete_sequence=colors)
        else:
            fig = px.line(x=categories, y=values, markers=True, color_discrete_sequence=['#2E86AB'])
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Hourly Distribution")
        
        hours = list(range(24))
        hourly_data = [5, 2, 1, 0, 0, 1, 3, 8, 15, 20, 25, 30,
                       35, 32, 28, 25, 22, 20, 18, 15, 12, 10, 8, 6]
        
        fig = px.bar(x=hours, y=hourly_data, 
                    labels={'x': 'Hour', 'y': 'Uploads'},
                    color_discrete_sequence=['#2E86AB'])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed statistics
    st.subheader("📋 Detailed Statistics")
    
    stats_data = pd.DataFrame({
        'Category': ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others'],
        'Total': [350, 250, 150, 100, 80, 50, 20],
        'Avg Confidence': ['95.2%', '93.8%', '91.5%', '89.2%', '87.8%', '85.5%', '82.3%'],
        'Recycling Rate': ['85%', '90%', '75%', '80%', '95%', '40%', '30%'],
        'Trend': ['↑', '↑', '→', '↓', '↑', '↑', '↓']
    })
    
    st.dataframe(stats_data, use_container_width=True, hide_index=True)
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Classifications", "1,000", "12%")
    
    with col2:
        st.metric("Average Confidence", "92.5%", "3.2%")
    
    with col3:
        st.metric("Recycling Rate", "78.5%", "5.3%")


def history_page():
    """History page with prediction records."""
    st.markdown('<h1 class="main-header">📜 Prediction History</h1>', unsafe_allow_html=True)
    
    # Search and filter
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("🔍 Search", placeholder="Search by filename...")
    
    with col2:
        category_filter = st.selectbox(
            "Filter by Category",
            ['All', 'Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others']
        )
    
    with col3:
        sort_by = st.selectbox(
            "Sort by",
            ['Newest First', 'Oldest First', 'Highest Confidence', 'Lowest Confidence']
        )
    
    st.divider()
    
    # History table
    if st.session_state.predictions:
        df = pd.DataFrame(st.session_state.predictions)
        
        # Apply filters
        if search_term:
            df = df[df['filename'].str.contains(search_term, case=False, na=False)]
        
        if category_filter != 'All':
            df = df[df['category'] == category_filter.lower()]
        
        # Apply sorting
        if sort_by == 'Newest First':
            df = df.sort_values('timestamp', ascending=False)
        elif sort_by == 'Oldest First':
            df = df.sort_values('timestamp', ascending=True)
        elif sort_by == 'Highest Confidence':
            df = df.sort_values('confidence', ascending=False)
        else:
            df = df.sort_values('confidence', ascending=True)
        
        # Display table
        st.dataframe(
            df[['id', 'filename', 'category', 'confidence', 'timestamp']],
            use_container_width=True,
            hide_index=True
        )
        
        # Export options
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Export as CSV"):
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="waste_classifications.csv",
                    mime="text/csv"
                )
        
        with col2:
            if st.button("🗑️ Clear History"):
                st.session_state.predictions = []
                st.session_state.total_uploads = 0
                st.rerun()
    else:
        st.info("No prediction history yet. Upload an image to get started!")


def settings_page():
    """Settings page for configuration."""
    st.markdown('<h1 class="main-header">⚙️ Settings</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔧 Model Settings")
        
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
            ['YOLOv8n (Nano)', 'YOLOv8s (Small)', 'YOLOv8m (Medium)', 'YOLOv8l (Large)']
        )
        
        st.button("🔄 Reset to Defaults")
    
    with col2:
        st.subheader("🎨 Display Settings")
        
        theme = st.selectbox(
            "Theme",
            ['Light', 'Dark', 'Auto']
        )
        
        show_confidence = st.checkbox("Show Confidence Score", value=True)
        show_recommendation = st.checkbox("Show Disposal Recommendation", value=True)
        
        st.button("💾 Save Settings")
    
    st.divider()
    
    st.subheader("ℹ️ About")
    st.markdown("""
    **Smart Waste Classification Dashboard** v1.0.0
    
    An AI-powered waste classification system that helps identify and sort waste materials.
    
    **Features:**
    - Real-time waste classification using YOLO
    - Interactive dashboard with charts and analytics
    - History tracking and export functionality
    
    **Technology Stack:**
    - AI Model: YOLOv8
    - Backend: FastAPI
    - Database: SQLite
    - Dashboard: Streamlit
    - Charts: Plotly
    """)


def main():
    """Main application entry point."""
    init_session_state()
    
    # Sidebar navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/recycle.png", width=80)
        st.title("♻️ Waste Classifier")
        st.divider()
        
        # Navigation menu
        page = st.radio(
            "Navigation",
            ["🏠 Home", "📤 Upload", "📊 Analytics", "📜 History", "⚙️ Settings"],
            index=0
        )
        
        st.divider()
        
        # Quick stats
        st.markdown("### Quick Stats")
        st.metric("Total Uploads", st.session_state.total_uploads)
        st.metric("Categories", "7")
        
        st.divider()
        
        # Footer
        st.markdown("---")
        st.markdown("Built with ❤️ using Streamlit")
    
    # Route to selected page
    if page == "🏠 Home":
        home_page()
    elif page == "📤 Upload":
        upload_page()
    elif page == "📊 Analytics":
        analytics_page()
    elif page == "📜 History":
        history_page()
    elif page == "⚙️ Settings":
        settings_page()


if __name__ == "__main__":
    main()
