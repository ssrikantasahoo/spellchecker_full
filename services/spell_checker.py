from spellchecker import SpellChecker
import re

class SpellCheckerService:
    def __init__(self):
        self.spell = SpellChecker()

    def tokenize(self, text: str):
        # Split into words + punctuation
        return re.findall(r"\w+|[^\w\s]", text)

    def check(self, text: str):
        # Ensure text exists
        if not text:
            return {
                "original": "",
                "misspelled": [],
                "suggestions": {},
                "corrected": ""
            }

        tokens = self.tokenize(text)

        # Only alphabetic tokens for spellchecking
        words_only = [t for t in tokens if t.isalpha()]

        misspelled = self.spell.unknown(words_only)

        corrected_tokens = []
        suggestions = {}

        # Create corrected sentence
        for token in tokens:
            if token in misspelled:
                corr = self.spell.correction(token)
                if corr is None:
                    corr = token
                suggestions[token] = corr
                corrected_tokens.append(corr)
            else:
                corrected_tokens.append(token)

        corrected_text = " ".join(corrected_tokens)

        return {
            "original": text,                     
            "misspelled": list(suggestions.keys()),
            "suggestions": suggestions,
            "corrected": corrected_text           
        }