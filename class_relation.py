import sys

foreground_to_background = {
    "Aeroplane": ["Sky", "Runway"],
    "Bicycle": ["Road", "Park"],
    "Bird": ["Sky", "Tree Branch"],
    "Boat": ["Water", "Harbor"],
    "Bottle": ["Table", "Kitchen"],
    "Bus": ["Road", "City Street"],
    "Car": ["Road", "Parking Lot"],
    "Cat": ["Indoor", "Garden"],
    "Chair": ["Indoor", "Restaurant"],
    "Cow": ["Grassland", "Farm"],
    "Dining Table": ["Indoor", "Restaurant"],
    "Dog": ["Grass", "Park"],
    "Horse": ["Grassland", "Field"],
    "Motorbike": ["Road", "City Street"],
    "Person": ["Indoor", "Outdoor"],
    "Potted Plant": ["Indoor", "Garden"],
    "Sheep": ["Grassland", "Hillside"],
    "Sofa": ["Indoor", "Living Room"],
    "Train": ["Railway", "Station"],
    "TV Monitor": ["Indoor", "Living Room"]
}

background_to_foreground = {}
for foreground, backgrounds in foreground_to_background.items():
    for background in backgrounds:
        if background not in background_to_foreground:
            background_to_foreground[background] = []
        background_to_foreground[background].append(foreground)

def find_background(foreground):
    if foreground in foreground_to_background:
        return foreground_to_background[foreground]
    else:
        return "No corresponding background found"

def find_foreground(background):
    if background in background_to_foreground:
        return background_to_foreground[background]
    else:
        return "No corresponding foreground found"

def main():
    print("Welcome to the Foreground-Background Matcher!")
    print("Enter 'foreground' to find backgrounds, or 'background' to find foregrounds.")
    choice = input("Your choice: ").strip().lower()

    if choice == "foreground":
        foreground_input = input("Enter a foreground object (e.g., 'Horse'): ").strip()
        backgrounds = find_background(foreground_input)
        print(f"Foreground: {foreground_input} -> Corresponding Backgrounds: {backgrounds}")
    elif choice == "background":
        background_input = input("Enter a background (e.g., 'Grassland'): ").strip()
        foregrounds = find_foreground(background_input)
        print(f"Background: {background_input} -> Possible Foregrounds: {foregrounds}")
    else:
        print("Invalid choice. Please enter 'foreground' or 'background'.")

if __name__ == "__main__":
    main()