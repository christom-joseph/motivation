from flask import Flask, render_template
from quotegenerator import QuoteGenerator
import random

app = Flask(__name__)
quote_gen = QuoteGenerator()

@app.route('/')
def home():
    # Generate a new quote
    raw_quote = quote_gen.generate_quote()
    quote_data = quote_gen.parse_quote(raw_quote)
    
    # Optional: Add some background colors
    background_colors = [
        '#F0F4F8', '#E6F2E6', '#FFF4E6', 
        '#F0E6FF', '#E6F3FF', '#FFF0F0'
    ]
    
    return render_template(
        'index.html', 
        quote=quote_data['quote'],
        author=quote_data['author'],
        bg_color=random.choice(background_colors)
    )

if __name__ == '__main__':
    app.run(debug=True)