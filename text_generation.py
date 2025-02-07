import re
import streamlit as st

def generate_story(user_prompt, text_generator, max_length=300):
    """
    Generates a comic-style story divided into four parts:
    Introduction, Storyline, Climax, and Moral.
    """
    prompt = (
        f"Write a short comic-style story based on: {user_prompt}.\n"
        "Format it as follows:\n"
        "Introduction:\n"
        "Storyline:\n"
        "Climax:\n"
        "Moral:\n"
    )
    
    generated = text_generator(prompt, max_length=max_length, do_sample=True, temperature=0.8, num_return_sequences=1)
    story_text = generated[0]['generated_text']

    # Regex to extract sections
    pattern = r"Introduction:(.*?)(?:Storyline:|$)(.*?)(?:Climax:|$)(.*?)(?:Moral:|$)(.*)"
    match = re.search(pattern, story_text, re.DOTALL | re.IGNORECASE)

    if match:
        parts = {
            "Introduction": match.group(1).strip(),
            "Storyline": match.group(2).strip(),
            "Climax": match.group(3).strip(),
            "Moral": match.group(4).strip()
        }
    else:
        st.warning("⚠️ Could not parse story. Returning empty sections.")
        parts = {"Introduction": "", "Storyline": "", "Climax": "", "Moral": ""}
    
    return parts
