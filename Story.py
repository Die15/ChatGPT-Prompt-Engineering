import openai

# Configurar la clave de API
openai.api_key = 'TU_CLAVE_DE_API'  # Reemplaza con una API válida

# Definir la función para generar texto con GPT-3.5-turbo


def generar_texto(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Utilizando GPT-3.5-turbo
        prompt=prompt,
        max_tokens=100  # Número máximo de tokens en la respuesta generada
    )
    return response.choices[0].text.strip()


# Ejemplo de uso
prompt = 'Una vez upon a time'
texto_generado = generar_texto(prompt)
print(texto_generado)
