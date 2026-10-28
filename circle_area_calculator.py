"""
circle_area_calculator.py
-------------------------
Use case 1: Simple Calculator for Area of a Circle

Asks the user for the radius of a circle and prints its area using
    Area = pi * radius^2      (pi = 3.14, as suggested in the assignment)

The program applies all three focus areas:
  * Input Handling      - clear prompts; the radius must be a positive number,
                          and the user is asked again until it is valid.
  * String Manipulation - the input is stripped and split so a unit can be typed
                          with the number (e.g. "5 cm"); the unit is cleaned up
                          (lowercased, length-checked); results are formatted with
                          f-strings and a summary table is built with ljust/rjust.
  * Exception Handling  - try/except catches non-numbers (ValueError), results
                          too large to compute (OverflowError), and Ctrl+C / end
                          of input (KeyboardInterrupt, EOFError), with friendly
                          messages and a chance to retry.
"""

import math

PI = 3.14                 # value of pi suggested by the assignment
MAX_UNIT_LENGTH = 10      # longest unit name accepted, e.g. "kilometers"
DEFAULT_UNIT = "units"    # used when the user types only a number


def parse_radius(text):
    """
    Turn text such as "5", "2.5 cm" or "  10  Meters " into (radius, unit).
    Raises ValueError with a friendly message if the text isn't valid.
    """
    parts = text.strip().split()          # strip spaces, then split into words

    if len(parts) == 0:
        raise ValueError("You didn't type anything.")
    if len(parts) > 2:
        raise ValueError("Type a number, optionally followed by one unit (e.g. 5 cm).")

    try:
        radius = float(parts[0])          # risky step: "abc" raises ValueError
    except ValueError:
        raise ValueError(f"'{parts[0]}' is not a number.") from None

    if not math.isfinite(radius):         # rejects "inf" and "nan"
        raise ValueError("The radius must be a real, finite number.")
    if radius <= 0:
        raise ValueError("The radius must be greater than zero.")

    unit = parts[1].lower() if len(parts) == 2 else DEFAULT_UNIT
    if not unit.isalpha():
        raise ValueError(f"The unit '{parts[1]}' should contain letters only.")
    if len(unit) > MAX_UNIT_LENGTH:
        raise ValueError(f"Please keep the unit to {MAX_UNIT_LENGTH} letters or fewer.")

    return radius, unit


def circle_area(radius):
    """Return the area of a circle. Raises OverflowError if it's too large."""
    return PI * radius ** 2


def get_yes_no(prompt):
    """Ask a yes/no question until the answer is y/yes/n/no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please answer 'y' or 'n'.")


def print_summary(results):
    """Print every calculation as a neatly aligned table."""
    if not results:
        return
    print("\n" + " Summary ".center(40, "="))
    print("Radius".ljust(18) + "Area".rjust(22))
    print("-" * 40)
    for radius, unit, area in results:
        radius_text = f"{radius:g} {unit}"
        area_text = f"{area:,.2f} sq {unit}"
        print(radius_text.ljust(18) + area_text.rjust(22))
    print("=" * 40)


def main():
    print("=== Circle Area Calculator ===")
    print(f"Area = pi x radius^2   (using pi = {PI})")
    print("You can add a unit after the number, e.g. 5 cm\n")

    results = []    # list of (radius, unit, area) tuples

    try:
        while True:
            text = input("Enter the radius of the circle: ")

            try:
                radius, unit = parse_radius(text)
                area = circle_area(radius)
            except ValueError as err:
                print(f"  Invalid input: {err} Please try again.\n")
                continue                    # go back and ask again
            except OverflowError:
                print("  That radius is too large to calculate. Try a smaller number.\n")
                continue

            results.append((radius, unit, area))
            print(f"  A circle with radius {radius:g} {unit} has an area of "
                  f"{area:,.2f} square {unit}.\n")

            if not get_yes_no("Calculate another? (y/n): "):
                break
            print()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D: stop cleanly instead of showing a traceback.
        print("\n\nStopped by user.")

    print_summary(results)
    print("Goodbye!")


if __name__ == "__main__":
    main()
