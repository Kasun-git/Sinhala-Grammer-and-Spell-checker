import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the API key from environment variables
token = os.getenv("GITHUB_TOKEN")  
base_url = "https://models.inference.ai.azure.com" 
model_name = "gpt-4o" 

def main():
    try:
        # Configure the OpenAI client
        openai.api_key = token
        openai.api_base = base_url

        # Create a chat completion request
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":"තොරන, වාර්තාකරනය, විසිකරණවා, තෝරණවා, විෂේෂත්වය, අනවෂේෂයෙන්, ප්‍රකාශණය, විමර්ශණ, තාක්ෂනය, දක්ෂින.when sentence started from මම then must be end with මී. when sentence started from අපි then must be end with මු. fullstop(.) is indicate the end of the sentence. Subject-Verb Agreement: Subject and verb must agree in number, gender, and person. Word Forms: Singular and plural words influence verb conjugation. Person Variations: First, second, and third person dictate sentence structure. Tense: Sentences should not mix past and non-past tenses. Gender Variations: Verb forms vary for masculine, feminine, and neutral genders. Case Roles: Focus determines sentence emphasis (active/passive). use these 8 grammer rules for correct the given sinhala paragraph. display the original sentence , spelling erroes, grammer errors and most suitable corrected paragraph and give only thoes thins using sinhala language, others give in english language.print the accuracy also."},
            ],
            temperature=1,
            max_tokens=4096,
            top_p=1,
        ) 

        # Output the assistant's response
        print(response['choices'][0]['message']['content'])
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
