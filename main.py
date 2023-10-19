import openai

api = "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"

openai.api_key = api

def main():
    messages = [
        {"role":"system","content":"You are a coding assistant. you will answer questions about programming an how to make, fix and debug stuff."},
        {"role":"user","content":"please introduce yourself"}
    ]

    while True:
        print("AI thinking...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        if 'choices' in response:
            message = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": message})
            print(f"AI: {message}\n")
        elif 'error' in response:
            print("Error:", response['error']['message'])
        else:
            print("Unknown error occurred.")
        
        i = input("YOU: ")
        messages.append({"role": "user", "content": i})
    
    
if __name__ == "__main__":
    main()