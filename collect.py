def display():
    """
    Displays the contents of the hub/collect.py file.
    """
    with open(__file__, 'r') as file:
        content = file.read()
        print(content)