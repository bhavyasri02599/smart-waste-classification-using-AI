"""
Analytics Page for Smart Waste Classification Dashboard.
Displays detailed charts, statistics, and trend analysis.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np


def render_analytics_page():
    """Render the analytics page with charts and statistics."""
    
    st.markdown("# 📊 Analytics Dashboard")
    st.markdown("---")
    
    # Date range filter
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        start_date = st.date_input(
            "Start Date",
            value=datetime.now() - timedelta(days=30),
            max_value=datetime.now()
        )
    
    with col2:
        end_date = st.date_input(
            "End Date",
            value=datetime.now(),
            max_value=datetime.now()
        )
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Refresh"):
            st.rerun()
    
    st.divider()
    
    # Summary metrics
    st.markdown("## 📈 Summary Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Classifications",
            value="1,247",
            delta="12.5%",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Unique Categories",
            value="7",
            delta=None
        )
    
    with col3:
        st.metric(
            label="Average Confidence",
            value="93.2%",
            delta="2.8%",
            delta_color="normal"
        )
    
    with col4:
        st.metric(
            label="Recycling Rate",
            value="82.5%",
            delta="5.2%",
            delta_color="normal"
        )
    
    st.divider()
    
    # Charts row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🥧 Category Distribution")
        
        categories = ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others']
        values = [425, 312, 187, 124, 98, 63, 38]
        colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B', '#44BBA4', '#E94F37']
        
        fig = px.pie(
            values=values,
            names=categories,
            color_discrete_sequence=colors,
            hole=0.4,
            labels={'value': 'Count'}
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Category Comparison")
        
        fig = px.bar(
            x=categories,
            y=values,
            color=categories,
            color_discrete_sequence=colors,
            labels={'x': 'Category', 'y': 'Count'}
        )
        fig.update_layout(height=350, margin=dict(t=20, b=20), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Charts row 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Daily Trend (Last 30 Days)")
        
        dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30, freq='D')
        np.random.seed(42)
        daily_counts = np.random.poisson(lam=40, size=30) + np.arange(30) * 2
        
        df_trend = pd.DataFrame({
            'Date': dates,
            'Classifications': daily_counts
        })
        
        fig = px.line(
            df_trend,
            x='Date',
            y='Classifications',
            line_shape='spline',
            color_discrete_sequence=['#2E86AB']
        )
        fig.update_traces(fill='tozeroy', fillcolor='rgba(46, 134, 171, 0.2)')
        fig.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🕐 Hourly Distribution")
        
        hours = list(range(24))
        hourly_data = [5, 2, 1, 0, 0, 1, 3, 8, 15, 20, 25, 30,
                       35, 32, 28, 25, 22, 20, 18, 15, 12, 10, 8, 6]
        
        fig = px.bar(
            x=hours,
            y=hourly_data,
            labels={'x': 'Hour of Day', 'y': 'Uploads'},
            color_discrete_sequence=['#A23B72']
        )
        fig.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    # Charts row 3
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Confidence Distribution")
        
        confidence_ranges = ['80-85%', '85-90%', '90-95%', '95-100%']
        confidence_counts = [45, 120, 380, 702]
        
        fig = px.bar(
            x=confidence_ranges,
            y=confidence_counts,
            color_discrete_sequence=['#F18F01'],
            labels={'x': 'Confidence Range', 'y': 'Count'}
        )
        fig.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📅 Weekly Pattern")
        
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekly_data = [180, 195, 210, 185, 170, 120, 87]
        
        fig = px.line_polar(
            r=weekly_data,
            theta=days,
            line_close=True,
            color_discrete_sequence=['#44BBA4']
        )
        fig.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed statistics table
    st.markdown("### 📋 Detailed Statistics")
    
    stats_data = pd.DataFrame({
        'Category': ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others'],
        'Total': [425, 312, 187, 124, 98, 63, 38],
        'Avg Confidence': ['95.2%', '93.8%', '91.5%', '89.2%', '87.8%', '85.5%', '82.3%'],
        'Recycling Rate': ['85%', '92%', '78%', '82%', '95%', '45%', '35%'],
        'Trend': ['↑ +12%', '↑ +8%', '→ +2%', '↓ -3%', '↑ +15%', '↑ +25%', '↓ -5%'],
        'Avg Processing Time': ['0.23s', '0.21s', '0.25s', '0.22s', '0.20s', '0.28s', '0.19s']
    })
    
    st.dataframe(
        stats_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Total": st.column_config.NumberColumn(format="%d"),
            "Trend": st.column_config.TextColumn()
        }
    )
    
    # Export options
    st.markdown("---")
    st.markdown("### 📥 Export Data")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Export as CSV"):
            csv = stats_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="analytics_data.csv",
                mime="text/csv"
            )
    
    with col2:
        if st.button("📊 Export as Excel"):
            st.info("Excel export coming soon!")
    
    with col3:
        if st.button("📈 Generate Report"):
            st.info("PDF report generation coming soon!")


if __name__ == "__main__":
    render_analytics_page()
