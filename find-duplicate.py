
ssn_name_pairs = {'123': 'Carlos', '234': 'Joao', '345': 'Nina', '456': 'Tina', '345': 'Nina', '123': 'Carlos'}

def find_duplicate_names(ssn_name_dict: dict) -> dict:
    result = {}
    names = list(ssn_name_dict.values())

    for (ssn, name) in ssn_name_dict.items():
        if names.count(name) > 1:
            result[name] = result.get(name, [])
    
    return result

duplicate_name_ssns = find_duplicate_names(ssn_name_pairs)

for (name, ssn) in duplicate_name_ssns.items():
    print(f"Found duplicate name {name} with SSN: {ssn}")
