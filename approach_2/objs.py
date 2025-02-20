pos_to_basic_pos = {
    "ADJ": "Adjective",
    "ADP": "Preposition",
    "ADV": "Adverb",
    "AUX": "Verb",
    "CCONJ": "Conjunction",
    "DET": "Adjective",  # Determiners are considered a subclass of adjectives
    "INTJ": "Interjection",
    "NOUN": "Noun",
    "NUM": "Noun",  # Numerals are often categorized as nouns in basic POS classification
    "PART": "Preposition",  # Particles are close to prepositions in basic classification
    "PRON": "Pronoun",
    "PROPN": "Noun",  # Proper nouns are nouns
    "PUNCT": "Other",  # Not part of traditional POS classification
    "SCONJ": "Conjunction",
    "SYM": "Other",  # Symbols don't fit in traditional POS
    "VERB": "Verb",
    "X": "Other"  # Uncategorized or unknown words
}

basic_pos_to_vector = {
    "Adjective": [1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Preposition": [0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Adverb": [0, 0, 1, 0, 0, 0, 0, 0, 0],
    "Verb": [0, 0, 0, 1, 0, 0, 0, 0, 0],
    "Conjunction": [0, 0, 0, 0, 1, 0, 0, 0, 0],
    "Interjection": [0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Noun": [0, 0, 0, 0, 0, 0, 1, 0, 0],
    "Pronoun": [0, 0, 0, 0, 0, 0, 0, 1, 0],
    "Other": [0, 0, 0, 0, 0, 0, 0, 0, 1]
}


lang_map = {"English": 0, "Hindi": 1}
pred_map = {0 : "English", 1 : "Hindi"}

max_len = 10

