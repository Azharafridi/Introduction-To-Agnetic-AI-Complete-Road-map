import os
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from datetime import date

green = "\033[0;32m"
white = "\033[0;39m"

print(f"{green}1. Prompt Template with pure strings --------{white}")
prompt_template = PromptTemplate.from_template(
    'Tell me a funny joke about elephants.'
)
print(prompt_template.format())

print(f"\n{green}2. Prompt Template with variables --------{white}")
prompt_template = PromptTemplate.from_template(
    'Tell me a {adjective} joke about {content}'
)
print(prompt_template.format(adjective='funny', content='chickens'))

print(f"\n{green}3. Creating Prompt Templates via the Constructor --------{white}")
prompt_template = PromptTemplate(
    template='Tell me a {adjective} joke about {content}',
    input_variables=['adjective', 'cotent']
)
print(prompt_template.format(adjective='funny', content='chickens'))

print(f"\n{green}4. Prompt Templates with Multiline Strings and Variables --------{white}")
template = '''You are a joke generating chatbot.
Provide funny jokes based on the themes requested.

Question: Tell me a {adjective} joke about {content}'

Answer: '''

prompt_template = PromptTemplate.from_template(template)
print(prompt_template.format(adjective='funny', content='chickens'))

print(f"\n{green}5. Prompt Template with f-string and Variables --------{white}")
prompt_template = PromptTemplate.from_template(
    f'Tell me a {{adjective}} joke about {{content}}'
)
print(prompt_template.format(adjective="funny", content="chickens"))


print(f"\n{green}6. Prompt Template with f-string and template and python variables --------{white}")
today = date.today()

prompt_template = PromptTemplate.from_template(
    f'Todays Date: {today}: Tell me a {{adjective}} joke about {{content}}'
)
print(prompt_template.format(adjective="funny", content="chickens"))

print(f"\n{green}7. Prompt Template with Multiline f-string and Variables --------{white}")
template = f'''You are a joke generating chatbot.
Provide funny jokes based on the themes requested.

Question: Tell me a {{adjective}} joke about {{content}}'

Answer: '''

prompt_template = PromptTemplate.from_template(template)
print(prompt_template.format(adjective='funny', content='chickens'))