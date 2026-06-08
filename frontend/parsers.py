#Zahlen input
def parse_amount(user_input):
    user_input = user_input.strip()

    try:
        return int(user_input)
    except ValueError:
        return None

#Listen Input
def parse_list(user_input):
    parts = user_input.strip().split()

    if len(parts) == 0:
        return None

    values = []

    for part in parts:
        value = parse_amount(part)

        if value is None:
            return None

        if value <= 0:
            return None

        values.append(value)

    return values

#Positiv
def parse_positive_amount(user_input):
    amount = parse_amount(user_input)

    if amount is None:
        return None

    if amount <= 0:
        return None

    return amount

#Str Input
def parse_name(user_input):
    name = user_input.strip().lower().capitalize()

    if len(name.split()) != 1:
        return None

    if not name.isalpha():
        return None

    return name

#Index
def parse_index(user_input):
    index = parse_positive_amount(user_input)

    if index is None:
        return None

    return index - 1

#Choice in run
def parse_choice(user_input, allowed_choices):
    choice = parse_positive_amount(user_input)  #Check if positive

    if choice is None:
        return None

    if choice not in allowed_choices:
        return None

    return choice

#Yes or No Auswahl
##change
def parse_yes_no(user_input):
    answer = parse_name(user_input)

    if answer in ["Yes", "Y"]:
        return True

    if answer in ["No", "N"]:
        return False

    return None

#Parse_Text
def parse_text(user_input):
    text = user_input.strip()

    if text == "":
        return None

    return text
