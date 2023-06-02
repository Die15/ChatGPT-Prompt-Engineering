import random
import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'TU_CLAVE_DE_API'  # Reemplaza con una API válida


def generar_expresion():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operador = random.choice(['+', '-', '*', '/'])
    expresion = f"{num1} {operador} {num2}"
    return expresion


def calcular_expresion(expresion):
    # Concatenar la expresión en un prompt de conversación
    prompt = "User: " + expresion + "\nAI: "

    # Llamar a la API de OpenAI para generar una respuesta
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )

    # Obtener la respuesta generada por GPT-3.5 Turbo
    respuesta_generada = respuesta.choices[0].text.strip().split("\n")[0]

    return respuesta_generada


# Generar una expresión aleatoria
expresion = generar_expresion()

# Calcular el resultado utilizando GPT-3.5 Turbo
resultado = calcular_expresion(expresion)

print("Expresión:", expresion)
print("Resultado:", resultado)
