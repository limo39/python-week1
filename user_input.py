
def get_user_input(prompt):
    return input(prompt)

def main():
    # Ask name
    name = get_user_input("What is your name? ")

    # Ask age
    age = get_user_input("How old are you? ")

    # Ask location
    location = get_user_input("Where do you live? ")

    # Print 
    print(f"Hello {name}, you are {age} years old and live in {location}.")

if __name__ == "__main__":
    main()
