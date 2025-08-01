import requests
def get_weather(city:str)-> str:#Tipo de dato strip
    base_url = f"https://wttr.in/{city}?format=%t" #f"" de format
    response = requests.get(base_url)#metodo get
    
    if response.status_code == 200:#Información del servidor funciona "200"
        return response.text.strip()#el return guarda el dato y lo muestra en donde uno quiere y print("") lo muestra en la terminal
    else:
        return "No se pudo obtener información del clima de su ciudad, intentelo mas tarde"

def frase_1() -> str:
    base_url = f"https://zenquotes.io/api/random"
    respuesta = requests.get(base_url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        frase = data[0]["q"]
        autor = data[0]["a"]
        return f'"{frase}" - {autor}'
    return "No se pudo obtener una frase en este momento. Intentalo más tarde."


def get_quote() -> str:
    base_url = f"https://api.quotable.io/random"
    respuesta = requests.get(base_url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        frase = data["content"]
        author = data["author"] 
        return f'"{frase}" - {author}'
    return "No se pudo obtener una cita en este momento. Inténtalo más tarde."
