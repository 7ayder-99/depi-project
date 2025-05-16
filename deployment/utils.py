def predict(model, encoder, raw_input):
    encoded_input = encoder.transform([raw_input])
    return model.predict(encoded_input)[0]