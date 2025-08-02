import google.generativeai as genai
genai.configure(api_key="AIzaSyBaEj-GS-_xQSQ7Q9fSHWJntalc1FadjRU")
available_models = genai.list_models()
for model in available_models:
    print(model.name)

