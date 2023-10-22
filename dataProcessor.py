import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def avgAgeCountry(data, country, age_transform_func=None):
    if age_transform_func is None:
        age_transform_func = lambda age: age if age is not None else 0 # Função de transformação padrão, não faz nada

    total_age = 0
    count = 0

    for person in data:
        if "country" in person and person["country"] == country and "age" in person:
            age = age_transform_func(person["age"])
            if age is not None:  # Verifica se o valor transformado não é None
                total_age += age
                count += 1

    if count == 0:
        return 0  

    return total_age / count

if __name__ == "__main__":
    # Exemplo de uso da função avgAgeCountry
    data = read_json_file("users.json")
    avg_age_us = avgAgeCountry(data, "US")
    print(f"A idade media nos EUA e {avg_age_us} anos.")