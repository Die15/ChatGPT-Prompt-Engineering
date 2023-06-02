import openai
# Configura tu clave de API de OpenAI
openai.api_key = 'TU_CLAVE_DE_API'  # Reemplaza con una API válida


def generar_resena_pelicula(nombre_pelicula):
    prompt = f"Title: \"{nombre_pelicula}\"\n\nReview:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )

    review = response.choices[0].text.strip()

    return review


# Nombre de la película ingresada por el usuario
nombre_pelicula = input("Enter the name of the movie ")

# Generar y mostrar la reseña de la película
reseña = generar_resena_pelicula(nombre_pelicula)
print(f"\nReseña de \"{nombre_pelicula}\":\n{reseña}")
