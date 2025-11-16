"""
LLM utilities for AI Lesson Planner
"""
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from ..config.settings import Settings


def LLM_Setup(prompt):
    """Setup and invoke LLM with given prompt"""
    if not Settings.GROQ_API_KEY or Settings.GROQ_API_KEY == 'your_groq_api_key_here':
        st.error("❌ Groq API key not found. Please set your API key in the .env file.")
        st.info("💡 **How to fix:**\n1. Create a `.env` file in the project root\n2. Add: `key=your_actual_groq_api_key`\n3. Get your API key from: https://console.groq.com/")
        st.stop()
    
    model = ChatGroq(
        model=Settings.GROQ_MODEL,
        groq_api_key=Settings.GROQ_API_KEY,
        temperature=Settings.GROQ_TEMPERATURE
    )
    parser = StrOutputParser()
    output = model | parser
    output = output.invoke(prompt)
    return output


def generate_notes_and_quiz(plan_content, subject, topic, grade):
    """Generate comprehensive notes and quiz from lesson plan"""
    prompt = f"""Based on the following lesson plan for {subject} - {topic} (Grade/Level: {grade}), generate:

1. **Comprehensive Study Notes** - Detailed notes that students can use for studying, including:
   - Key concepts and definitions
   - Important points and explanations
   - Examples and illustrations
   - Summary of main topics
   - Important formulas/theorems (if applicable)

2. **Quiz/Assessment Questions** - Create a quiz with:
   - 10-15 multiple choice questions (with 4 options each)
   - 5-7 short answer questions
   - 2-3 essay/long answer questions
   - Answer key with explanations

Format the response in Markdown with clear sections:
- # Study Notes
- # Quiz Questions
- # Answer Key

Make it appropriate for {grade} level students.

Lesson Plan Content:
{plan_content[:2000]}  # Limit to avoid token issues

Generate comprehensive, well-structured notes and quiz questions."""
    
    return LLM_Setup(prompt)

