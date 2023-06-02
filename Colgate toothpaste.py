import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'TU_CLAVE_DE_API'  # Reemplaza con una API válida


def generar_informacion():
    prompt = "Generate information about Colgate toothpaste."

    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )

    informacion_generada = respuesta.choices[0].text.strip().split("\n")[0]

    return informacion_generada


# Generar información sobre Colgate toothpaste utilizando GPT-3.5 Turbo
informacion = generar_informacion()

print("Información sobre Colgate toothpaste:")
print(informacion)
