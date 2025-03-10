import streamlit as st
import google.generativeai as genai  

# Configure API key
genai.configure(api_key="Your_Gemini_API_Key")  

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Streamlit App Title
st.title("NutriGen 🍽 - Personalized AI Meal Planner")

st.write("Get a customized, healthy meal plan based on your dietary needs!")

# User Inputs
st.subheader("Tell us about your dietary preferences:")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
    dietary_restrictions = st.text_input("Dietary Restrictions (e.g., vegan, keto, gluten-free):")
    allergies = st.text_input("Allergies (e.g., nuts, dairy, seafood):")

with col2:
    health_conditions = st.text_input("Health Conditions (e.g., diabetes, heart health):")
    activity_level = st.selectbox("Activity Level:", ["Sedentary", "Lightly active", "Moderately active", "Very active"])

taste_preferences = st.text_area("Taste Preferences (e.g., spicy food, Mediterranean cuisine, dislike broccoli):")

# Function to get a personalized meal plan
def get_meal_plan(gender, restrictions, allergies, health, activity, taste):
    prompt = f"""
    Create a detailed 7-day personalized meal plan with recipes, a grocery list, and a breakdown of key nutrients for each meal.
    
    User Preferences:
    - Gender: {gender}
    - Dietary Restrictions: {restrictions} (Ensure all meals strictly follow these restrictions.)
    - Allergies: {allergies} (Exclude any ingredients that contain these allergens.)
    - Health Conditions: {health}
    - Activity Level: {activity}
    - Taste Preferences: {taste}
    
    Each meal should include:
    - Breakfast, Lunch, Dinner, and Snacks
    - A short recipe for preparation
    - A nutrient breakdown including Calories, Protein, Carbs, Fats, Fiber, Vitamins, and Minerals
    
    Ensure meals are balanced, nutritious, and enjoyable.
    
    Only return the 7-day meal plan in a structured format, fully expanded for user convenience. Do not include any additional suggestions or comments at the end.
    """
    
    # Generate response using Gemini AI
    response = model.generate_content(prompt)
     
    return response.text if response else "No meal plan could be generated. Try again."

# Display Output
if st.button("Generate Meal Plan"):
    with st.spinner("Creating your personalized meal plan..."):
        meal_plan = get_meal_plan(gender, dietary_restrictions, allergies, health_conditions, activity_level, taste_preferences)
        st.subheader("Your AI-Generated Meal Plan 🍽")
        st.write(meal_plan)
