"""
History Page for Smart Waste Classification Dashboard.
Displays prediction history with search, filter, and export functionality.
"""

import streamlit as st
import pandas as pd
from datetime import datetime


def render_history_page():
    """Render the history page with prediction records."""
    
    # Initialize session state if not present
    if 'predictions' not in st.session_state:
        st.session_state.predictions = []
    if 'total_uploads' not in st.session_state:
        st.session_state.total_uploads = 0
    
    st.markdown("# 📜 Prediction History")
    st.markdown("---")
    
    # Search and filter section
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        search_term = st.text_input(
            "🔍 Search",
            placeholder="Search by filename...",
            key="search_history"
        )
    
    with col2:
        category_filter = st.selectbox(
            "Filter by Category",
            ['All', 'Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others'],
            key="filter_category"
        )
    
    with col3:
        sort_by = st.selectbox(
            "Sort by",
            ['Newest First', 'Oldest First', 'Highest Confidence', 'Lowest Confidence'],
            key="sort_by"
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
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Predictions", len(df))
        
        with col2:
            st.metric("Average Confidence", f"{df['confidence'].mean():.1%}")
        
        with col3:
            unique_categories = df['category'].nunique()
            st.metric("Unique Categories", unique_categories)
        
        with col4:
            st.metric("Session Uploads", st.session_state.total_uploads)
        
        st.divider()
        
        # Display table
        st.markdown("### 📋 Predictions Table")
        
        # Format the dataframe for display
        display_df = df[['id', 'filename', 'category', 'confidence', 'timestamp']].copy()
        display_df['confidence'] = display_df['confidence'].apply(lambda x: f"{x:.1%}")
        display_df['timestamp'] = display_df['timestamp'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
        
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "id": st.column_config.NumberColumn("ID", width="small"),
                "filename": st.column_config.TextColumn("Filename", width="medium"),
                "category": st.column_config.TextColumn("Category", width="small"),
                "confidence": st.column_config.TextColumn("Confidence", width="small"),
                "timestamp": st.column_config.TextColumn("Timestamp", width="medium")
            }
        )
        
        st.divider()
        
        # Export options
        st.markdown("### 📥 Export Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Export as CSV", key="export_csv"):
                csv = df.to_csv(index=False)
                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv,
                    file_name="waste_classifications.csv",
                    mime="text/csv",
                    key="download_csv"
                )
        
        with col2:
            if st.button("📊 Export as Excel", key="export_excel"):
                st.info("Excel export coming soon!")
        
        with col3:
            if st.button("🗑️ Clear History", key="clear_history"):
                st.session_state.predictions = []
                st.session_state.total_uploads = 0
                st.rerun()
        
        # Category breakdown
        st.markdown("### 📊 Category Breakdown")
        
        category_counts = df['category'].value_counts()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.bar_chart(category_counts)
        
        with col2:
            st.markdown("**Distribution:**")
            for category, count in category_counts.items():
                percentage = (count / len(df)) * 100
                st.markdown(f"- **{category.title()}**: {count} ({percentage:.1f}%)")
    
    else:
        # Empty state
        st.markdown("""
        <div style='text-align: center; padding: 60px; background-color: #f8f9fa; border-radius: 10px;'>
            <h2 style='color: #666;'>📭 No History Yet</h2>
            <p style='color: #888; font-size: 1.1em;'>Start by uploading waste images to see your prediction history here.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Call to action
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("📤 Go to Upload Page", type="primary"):
                st.switch_page("pages/2_📤_Upload.py")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Tips
        st.markdown("### 💡 What You'll See Here")
        st.markdown("""
        - **Complete history** of all waste classifications
        - **Search and filter** by filename or category
        - **Sort** by date or confidence score
        - **Export** your data for analysis
        - **Category breakdown** charts
        """)


if __name__ == "__main__":
    render_history_page()
