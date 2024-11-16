
def makeFile(filename):
    print(f"File created: {filename}")

def writeToFile(filename, content):
    print(f"Written to {filename}: {content}")


def get_desp(_d:dict, key:int):
    return _d[key]['desp']

def run(_d: dict, key: int):
    # Check if the provided key exists in the dictionary
    if key not in _d:
        print(f"Key {key} not found in the dictionary.")
        return

    print(f"Processing ID: {key}")

    # Retrieve actions for the specified key
    actions = _d[key]
    for action_key, action in actions.items():
        if isinstance(action, str):
            if "makeFile" in action:
                # Execute makeFile dynamically
                eval(action)
            elif "writeToFile" in action:
                # Execute writeToFile dynamically
                eval(action)