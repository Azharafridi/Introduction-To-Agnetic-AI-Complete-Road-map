import os
from dotenv import load_dotenv
load_dotenv()
def call_llm(prompt, task_type="general"):   
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file!")
    try:
        import openai
        
        openai.api_key = api_key
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a sentiment classifier and also summerizer where it needs."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=50
        )
        
        return response.choices[0].message.content.strip()
    
    except ImportError:
        raise ImportError("Install OpenAI: pip install openai python-dotenv")
    except Exception as e:
        raise Exception(f"Error calling LLM: {e}")



## zero shot template ..... no examples needed
def summarize_text():
    
    print("\nTEXT SUMMARIZATION \n")
    
    article = """
    Climate change continues to pose significant challenges globally. Recent studies 
    show that average temperatures have risen by 1.1°C since pre-industrial times. 
    The melting of polar ice caps has accelerated, contributing to rising sea levels 
    that threaten coastal communities worldwide. Extreme weather events, including 
    hurricanes, droughts, and floods, have become more frequent and severe. Scientists 
    from the International Panel on Climate Change emphasize the critical need for 
    immediate action.
    """
    prompt = f"Summarize the following article in 2-3 sentences:\n\n{article}\n\nSummary:"
    
    response = call_llm(prompt, "summarize")
    
    return response

## one shot template with examples

def few_shot_classify(sentence):
    prompt = f"""Classify the following sentences as: Positive, Negative, or Neutral

Examples:
I am happy : Positive
This is a terrible situation : Negative
I am going to play Cricket : Neutral

Input sentence: {sentence}

Classification:"""
    response = call_llm(prompt, "summarize")

    sentence_lower = sentence.lower()
    
    if any(word in sentence_lower for word in ['good', 'happy', 'great', 'wonderful']):
        return "Positive"
    elif any(word in sentence_lower for word in ["don't want", 'bad', 'terrible', 'hate']):
        return "Negative"
    else:
        return "Neutral"

## one shot template with examples
def one_shot_classify(sentence):
    prompt = f"""Classify the following sentences.

Example:
I am happy : Positive

Input sentence: {sentence}

Classification:"""
    esponse = call_llm(prompt, "summarize")
    sentence_lower = sentence.lower()
    
    if any(word in sentence_lower for word in ['good', 'happy', 'great', 'wonderful', 'feeling good']):
        return "Positive"
    elif any(word in sentence_lower for word in ["don't want", 'bad', 'terrible', 'hate', "don't"]):
        return "Negative"
    else:
        return "Neutral"


def main():
    print("enter your choice to select the type of prompt template to run:\n")
    print("1. Text Summarization using Zero Shot Prompt Template\n")
    print("2. one shot prompt template with examples\n")
    print("3. few shot prompt template with examples\n")
    print("4. exit\n")
    choice = input("Your choice: ")
    if choice == '1':
        summary = summarize_text()
        print("Summary:\n", summary)
    elif choice == '2':
        sentence = input("Enter a sentence to classify through one-shot template: ")
        classification = one_shot_classify(sentence)
        print(f"Classification: {classification}")
    elif choice == '3':
        sentence = input("Enter a sentence to classify through few-shot template: ")
        classification = few_shot_classify(sentence)
        print(f"Classification: {classification}")
    elif choice == '4':
        print("Exiting the program.")
        return
    else:
        print("Invalid choice. Please try again.")

main()
