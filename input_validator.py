"""
input_validator.py
 
Repeatedly prompts the user until they enter a valid whole number
within a given range, then confirms the accepted value.
"""
 
MIN_VALUE = 1
MAX_VALUE = 100
 
 
def get_valid_integer(prompt: str, low: int, high: int) -> int:
    """Keep asking until the user enters an integer between low and high (inclusive)."""
    while True:
        raw = input(prompt).strip()
 
        if raw == "":
            print("Input cannot be empty. Please try again.")
            continue
 
        try:
            value = int(raw)
        except ValueError:
            print(f"'{raw}' is not a whole number. Please try again.")
            continue
 
        if value < low or value > high:
            print(f"{value} is out of range. Enter a number from {low} to {high}.")
            continue
 
        return value
 
 
def main() -> None:
    number = get_valid_integer(
        f"Enter a whole number between {MIN_VALUE} and {MAX_VALUE}: ",
        MIN_VALUE,
        MAX_VALUE,
    )
    print(f"Thanks! {number} is valid.")
 
 
if __name__ == "__main__":
    main()
 
