from tensorflow.keras.models import load_model
from objs import max_len, pred_map, basic_pos_to_vector, pos_to_basic_pos
import numpy as np
import string
import stanza
import spacy
import logging


def is_hindi(token):
    return all("\u0900" <= char <= "\u097F" for char in token)

def get_pos_tags(sentence):

    st_logger = logging.getLogger("stanza")
    st_logger.setLevel(logging.ERROR)

    nlp_en = spacy.load("en_core_web_sm")
    nlp_hi = stanza.Pipeline("hi", download_method=None)

    tokens = sentence.split()
    tokens = [token.strip(string.punctuation + chr(2404)) for token in tokens] # chr(2404) = Hindi fullstop (।)
    pos_sequence = []

    for token in tokens:
        if is_hindi(token):
            doc = nlp_hi(token)
            pos_sequence.append(pos_to_basic_pos.get(doc.sentences[0].words[0].upos, "other"))
        else:
            doc = nlp_en(token)
            pos_sequence.extend([pos_to_basic_pos.get(token.pos_, "other") for token in doc])

    del nlp_en, nlp_hi

    return pos_sequence

def predict(input):
    
    pos_sequence = get_pos_tags(input)

    vectorized_pos_seq = [basic_pos_to_vector[token] for token in pos_sequence]

    if len(vectorized_pos_seq) < max_len:
        padding = [[0] * 9] * (max_len - len(vectorized_pos_seq))
        vectorized_pos_seq += padding
    else:
        vectorized_pos_seq = vectorized_pos_seq[:max_len]

    inp = np.array([vectorized_pos_seq])

    model = load_model("dominant_language_model_2.keras")
    pred = list(model.predict(inp, verbose=0)[0])
    
    return pred_map[pred.index(max(pred))]


# predict("यह जगह बहुत essential है।")