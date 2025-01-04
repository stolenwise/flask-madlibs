# Making a Madlibs app using Flask
from flask import Flask, render_template, request
from stories import story  # Import the Story instance from stories.py

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_form():
    """Show the form to collect user inputs for Madlibs."""
    return render_template('form.html', prompts=story.prompts)

@app.route('/story', methods=['POST'])
def generate_story():
    """Generate and display the Madlibs story."""
    # Collect answers from the form
    answers = {prompt: request.form.get(prompt) for prompt in story.prompts}
    
    # Generate the story using the Story class
    madlibs_story = story.generate(answers)

    return render_template('story.html', story=madlibs_story)

if __name__ == '__main__':
    app.run(debug=True)