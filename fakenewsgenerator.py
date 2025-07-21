import random
from datetime import datetime
from collections import Counter

FAKENEWS = "headlines_log.txt"

# Data pools
subjects = [
    "Shahrukh Khan", "Virat Kohli", "Nirmala Sitharaman", 
    "a Mumbai cat", "a group of monkeys", "Prime Minister Modi", 
    "an auto-rickshaw driver from Delhi"
]

actions = [
    "launches", "cancels", "dances with", "eats", 
    "declares war on", "orders", "celebrates"
]

places_or_things = [
    "at Red Fort", "in a Mumbai local train", "a plate of samosa", 
    "inside Parliament", "at Ganga Ghat", "during IPL match", 
    "at India Gate"
]

# Generating fake headlines
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)
    return f"BREAKING NEWS: {subject} {action} {place}"

# Save headlines to a file
def save_headline_to_file(headline, filename=FAKENEWS):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {headline}\n")

# Viewing all headlines
def show_saved_headlines(filename=FAKENEWS):
    print("\n🗂️  Previous Headlines:\n")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No headlines saved yet.")
            else:
                for line in reversed(lines):
                    print("•", line.strip())
    except FileNotFoundError:
        print("No saved headlines found.")

# Search headlines by keyword
def search_headlines(keyword, filename=FAKENEWS):
    print(f"\n🔍 Searching for headlines containing: '{keyword}'\n")
    found = False
    try:
        with open(filename, "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print("•", line.strip())
                    found = True
        if not found:
            print("No headlines found with that keyword.")
    except FileNotFoundError:
        print("No saved headlines found.")

# Showing statistics
def show_statistics(filename=FAKENEWS):
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file.readlines()]
            if not lines:
                print("No data available.")
                return

        print("\n📊 Headline Statistics:\n")
        print(f"Total headlines: {len(lines)}")

        subject_counter = Counter()
        action_counter = Counter()

        for line in lines:
            parts = line.split("BREAKING NEWS: ")[-1].split()
            subject = ' '.join(parts[:2]) if parts[1].islower() else parts[0]
            action = parts[2] if parts[1].islower() else parts[1]
            subject_counter[subject] += 1
            action_counter[action] += 1

        print(f"Top 3 subjects: {subject_counter.most_common(3)}")
        print(f"Top 3 actions: {action_counter.most_common(3)}")
        
    except FileNotFoundError:
        print("No saved headlines to analyze.")


def run_news_generator():
    print("📰 Welcome to the Fake News Headline Generator (Python Edition) 🐍")

    while True:
        print("\nMenu:")
        print("1. Generate a fake headline")
        print("2. View saved headlines")
        print("3. Search headlines by keyword")
        print("4. Show headline statistics")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            headline = generate_headline()
            print("\n" + headline)
            save_headline_to_file(headline)
        elif choice == "2":
            show_saved_headlines()
        elif choice == "3":
            keyword = input("Enter keyword to search: ").strip()
            if keyword:
                search_headlines(keyword)
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            print("\nThank you for using the Fake News Headline Generator. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_news_generator()


