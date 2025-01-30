import requests

def fetch_astronauts():
    """
    Fetch data about people currently in space.
    Returns:
        A dictionary containing the data or None if the request fails.
    """
    url = "http://api.open-notify.org/astros.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print("JSON: ")
        print(response.json())
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"🚨 An error occurred while fetching the data: {e}")
        return None

def display_astronauts(data):
    """
    Display the names of astronauts currently in space.
    Args:
        data (dict): The JSON data containing astronaut information.
    """
    if not data or "people" not in data:
        print("🚀 No data available to display.")
        return

    print("\n👩‍🚀 Astronauts Currently in Space:")
    for i, person in enumerate(data["people"], start=1):
        print(f"{i}. {person['name']} (Craft: {person['craft']})")

    print(f"\n🌌 Total Astronauts in Space: {data['number']}")

def main():
    """
    Main function to run the program.
    """
    print("Fetching data about astronauts currently in space...\n")
    data = fetch_astronauts()

    if data:
        display_astronauts(data)
    else:
        print("⚠️ Could not retrieve astronaut data. Please try again later.")

# Run the program
if __name__ == "__main__":
    main()
