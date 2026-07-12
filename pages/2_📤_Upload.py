"""
Upload Page for Smart Waste Classification Dashboard.
Handles image upload and displays classification results.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random
import time


def render_upload_page():
    """Render the upload page with image classification."""
    
    # Initialize session state if not present
    if 'predictions' not in st.session_state:
        st.session_state.predictions = []
    if 'total_uploads' not in st.session_state:
        st.session_state.total_uploads = 0
    
    st.markdown("# 📤 Upload Waste Image")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📁 Upload Image")
        
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png", "bmp"],
            help="Upload an image of waste for AI classification",
            key="waste_uploader"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            # File info
            st.markdown("**File Information:**")
            st.markdown(f"- **Filename:** {uploaded_file.name}")
            st.markdown(f"- **Size:** {uploaded_file.size / 1024:.2f} KB")
            st.markdown(f"- **Type:** {uploaded_file.type}")
            
            st.divider()
            
            # Classification options
            st.markdown("### ⚙️ Classification Options")
            
            confidence_threshold = st.slider(
                "Confidence Threshold",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                step=0.05,
                help="Minimum confidence score for predictions"
            )
            
            auto_save = st.checkbox("Auto-save to database", value=True)
            
            st.divider()
            
            # Classify button
            if st.button("🔍 Classify Waste", type="primary"):
                with st.spinner("Analyzing image with AI model..."):
                    # Simulate processing time
                    progress_bar = st.progress(0)
                    for percent in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(percent + 1)
                    
                    # Simulate prediction
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
                        'timestamp': datetime.now(),
                        'file_size': uploaded_file.size
                    }
                    st.session_state.predictions.append(prediction)
                    st.session_state.total_uploads += 1
                    
                    st.success("✅ Classification complete!")
                    st.rerun()
    
    with col2:
        st.markdown("### 📊 Classification Results")
        
        if st.session_state.predictions:
            latest = st.session_state.predictions[-1]
            
            # Category display with badge
            category = latest['category']
            category_emojis = {
                'plastic': '♻️',
                'paper': '📄',
                'glass': '🍶',
                'metal': '🥫',
                'organic': '🌱',
                'e-waste': '💻',
                'others': '🗑️'
            }
            
            st.markdown(f"""
            <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86AB;'>
                <h3 style='margin: 0;'>{category_emojis.get(category, '🗑️')} {category.upper()}</h3>
                <p style='margin: 5px 0 0 0; color: #666;'>Waste Category</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Confidence score
            confidence = latest['confidence']
            
            st.markdown("**Confidence Score:**")
            
            # Color-coded progress bar
            if confidence >= 0.9:
                bar_color = "🟢"
            elif confidence >= 0.7:
                bar_color = "🟡"
            else:
                bar_color = "🔴"
            
            st.progress(confidence)
            st.markdown(f"{bar_color} **{confidence:.1%}**")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Disposal recommendation
            recommendations = {
                'plastic': {
                    'title': 'Recycling Bin',
                    'description': 'Place in the recycling bin. Rinse containers before disposal. Check local recycling guidelines for specific plastic types.',
                    'icon': '♻️'
                },
                'paper': {
                    'title': 'Paper Recycling',
                    'description': 'Place in the paper recycling bin. Remove any plastic windows or bindings. Shred sensitive documents.',
                    'icon': '📄'
                },
                'glass': {
                    'title': 'Glass Recycling',
                    'description': 'Place in the glass recycling bin. Separate by color if required locally. Do not break glass items.',
                    'icon': '🍶'
                },
                'metal': {
                    'title': 'Metal Recycling',
                    'description': 'Place in the metal recycling bin. Aluminum cans and tin cans are recyclable. Rinse before disposal.',
                    'icon': '🥫'
                },
                'organic': {
                    'title': 'Compost Bin',
                    'description': 'Place in the compost bin or organic waste collection. Can be composted at home or in community gardens.',
                    'icon': '🌱'
                },
                'e-waste': {
                    'title': 'E-Waste Collection',
                    'description': 'Do NOT place in regular trash. Take to designated e-waste collection centers. Contains hazardous materials.',
                    'icon': '💻'
                },
                'others': {
                    'title': 'General Waste',
                    'description': 'Check local waste management guidelines. Some items may be recyclable or require special disposal.',
                    'icon': '🗑️'
                }
            }
            
            rec = recommendations.get(category, recommendations['others'])
            
            st.markdown(f"""
            <div style='background-color: #e8f4f8; padding: 20px; border-radius: 10px; border-left: 5px solid #44BBA4;'>
                <h4 style='margin: 0 0 10px 0;'>{rec['icon']} Disposal: {rec['title']}</h4>
                <p style='margin: 0; color: #555;'>{rec['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Action buttons
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("💾 Save to Database"):
                    st.success("Saved to database!")
            
            with col2:
                if st.button("📤 Share Result"):
                    st.info("Share functionality coming soon!")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Prediction history for this session
            st.markdown("### 📜 Session Predictions")
            
            if len(st.session_state.predictions) > 1:
                session_df = pd.DataFrame(st.session_state.predictions[-5:])
                st.dataframe(
                    session_df[['category', 'confidence', 'timestamp']],
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("This is your first prediction in this session.")
        
        else:
            # Empty state
            st.markdown("""
            <div style='text-align: center; padding: 40px; background-color: #f8f9fa; border-radius: 10px;'>
                <h3 style='color: #666;'>No Predictions Yet</h3>
                <p style='color: #888;'>Upload an image to classify waste using AI</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Tips
            st.markdown("### 💡 Tips for Best Results")
            st.markdown("""
            - Use clear, well-lit images
            - Center the waste item in the frame
            - Avoid blurry or dark images
            - Single items work better than mixed waste
            - Supported formats: JPG, PNG, BMP
            """)
    
    st.divider()
    
    # Quick classification guide
    st.markdown("### 📚 Waste Categories Guide")
    
    categories_info = pd.DataFrame({
        'Category': ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic', 'E-Waste', 'Others'],
        'Examples': [
            'Bottles, bags, containers',
            'Newspapers, cardboard, books',
            'Bottles, jars, window glass',
            'Cans, foil, appliances',
            'Food scraps, leaves, wood',
            'Electronics, batteries, cables',
            'Textiles, rubber, mixed'
        ],
        'Recyclable': ['✅ Yes', '✅ Yes', '✅ Yes', '✅ Yes', '🌱 Compost', '⚠️ Special', '❓ Check'],
        'Bin Color': ['Yellow', 'Blue', 'Green', 'Gray', 'Brown', 'Red', 'Black']
    })
    
    st.dataframe(categories_info, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    render_upload_page()
