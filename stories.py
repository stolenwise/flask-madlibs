"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    [
        "place", "time_of_day", "noun", "verb", "adjective", 
        "plural_noun", "emotion", "adverb", "animal", "sound"
    ],
      """
    On a {adjective} morning in the faraway {place}, the {animal} 
    woke up feeling {emotion}. It was {time_of_day}, and the sun was 
    just starting to rise, casting a {adjective} glow over the {plural_noun}.

    The {animal}, named Fluffy, decided to {verb} {adverb} towards the 
    nearest {noun}. Suddenly, a loud {sound} echoed through the air, 
    startling Fluffy.

    "What could that be?" Fluffy wondered, {adverb}. Determined to 
    find out, it ventured deeper into the {place}, where an adventure 
    like no other awaited.
    """
)
