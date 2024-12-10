import os
import google.generativeai as genai
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

class QuoteGenerator:
    def __init__(self):
        # Configure the Gemini API
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        # Create the model
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Define multiple prompt templates to increase variability
        self.prompt_templates = [
            """Create an inspiring motivational quote that:
            - Is original and unique
            - Focuses on personal growth
            - Encourages resilience and hope
            - Is no more than 20 words long
            
            Provide the quote and an optional author name.""",
            
            """Design a powerful motivational quote that:
            - Sparks inner strength
            - Addresses overcoming challenges
            - Provides a fresh perspective
            - Stays concise (under 20 words)
            
            Format with quote and potential author.""",
            
            """Compose a motivational quote that:
            - Inspires self-improvement
            - Highlights the power of perseverance
            - Offers a new insight into personal development
            - Remains brief and impactful
            
            Include quote and possible attribution."""
        ]
    
    def generate_quote(self):
        """Generate a unique motivational quote using Gemini 1.5 Flash"""
        # Randomly select a prompt template
        prompt = random.choice(self.prompt_templates)
        
        try:
            # Add randomness by varying the generation parameters
            generation_config = {
                'temperature': 2,  # Slight randomness
                'max_output_tokens': 500
            }
            
            response = self.model.generate_content(
                prompt, 
                generation_config=generation_config
            )
            
            # Clean and format the quote
            quote_text = response.text.strip()
            
            # Ensure we have a quote and author
            if "Quote:" not in quote_text and "Author:" not in quote_text:
                # If the response doesn't match our desired format, we'll format it
                quote_text = f"Quote: {quote_text}"
            
            return quote_text
        
        except Exception as e:
            return f"Quote Generation Error: {str(e)}"
    
    def parse_quote(self, quote_text):
        """Parse the quote text into a more structured format"""
        try:
            # Split the quote into quote and author parts
            parts = quote_text.split('\n')
            quote = parts[0].replace('Quote: ', '').strip()
            author = parts[1].replace('Author: ', '').strip() if len(parts) > 1 else 'Anonymous'
            
            return {
                'quote': quote,
                'author': author
            }
        except Exception:
            return {
                'quote': quote_text,
                
            }