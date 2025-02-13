import requests
import json

def obtener_codigos_pais(api_key, guardar_en_json=False):
    url = f"https://api.countrylayer.com/v2/all?access_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        countries = response.json()
        # Extraer datos relevantes para cada país
        country_codes = [
            {
                "name": country["name"],
                "calling_code": f"+{country['callingCodes'][0]}" if country["callingCodes"] else "N/A",
                "flag": country.get("flag", "N/A")  # Usa 'N/A' si 'flag' no existe
            }
            for country in countries
        ]
        
        # Guardar en JSON si se indica
        if guardar_en_json:
            with open("country_codes.json", "w", encoding="utf-8") as json_file:
                json.dump(country_codes, json_file, ensure_ascii=False, indent=4)
            print("Datos guardados en country_codes.json")
        
        return country_codes
    else:
        print("Error al obtener los datos de países")
        return []


# Ejemplo de uso
api_key = "0a12c784297568acf4f9fad9695c7831"  # Reemplaza con tu clave de API
country_codes = obtener_codigos_pais(api_key, guardar_en_json=True)
for country in country_codes[:5]:  # Muestra los primeros 5 países
    print(country)
