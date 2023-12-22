import time
from openai import OpenAI
import time
client = OpenAI(api_key='sua-key')

# Marca o tempo de início
tempo_inicio = time.time()

gpt_assistant_prompt = "GPT-4"
gpt_user_prompt = "Calcule o IMC, peso= 70 altura=1.75"
gpt_prompt = gpt_assistant_prompt, gpt_user_prompt
message=[{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": gpt_user_prompt}]
temperature=0.2
max_tokens=256
frequency_penalty=0.0

response = client.chat.completions.create(
    model="gpt-4",
    messages = message,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty
)
print(response.choices[0].message)

# Marca o tempo de término
tempo_fim = time.time()
# calcula o tempo 
tempo_execucao = tempo_fim - tempo_inicio
# Exiba o tempo de processamento
print(f"Tempo de execução: {tempo_execucao} segundos")
