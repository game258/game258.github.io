import random
import json
import os

# Create a dictionary to store questions, options, and answers
quiz_questions = {
    "What is the capital of France?": {
        "A": "Paris",
        "B": "London",
        "C": "Berlin",
        "D": "Rome",
        "answer": "A"
    },
    "Who painted the Mona Lisa?": {
        "A": "Leonardo da Vinci",
        "B": "Michelangelo",
        "C": "Raphael",
        "D": "Caravaggio",
        "answer": "A"
    },
    "What is the largest planet in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "answer": "C"
    },
    "What is the chemical symbol for gold?": {
        "A": "Ag",
        "B": "Au",
        "C": "Hg",
        "D": "Pb",
        "answer": "B"
    },
    "Who wrote Romeo and Juliet?": {
        "A": "William Shakespeare",
        "B": "Jane Austen",
        "C": "J.K. Rowling",
        "D": "Charles Dickens",
        "answer": "A"
    },
    "What is the smallest country in the world?": {
        "A": "Vatican City",
        "B": "Monaco",
        "C": "Nauru",
        "D": "Tuvalu",
        "answer": "A"
    },
    "What is the largest mammal on Earth?": {
        "A": "Blue whale",
        "B": "Fin whale",
        "C": "Humpback whale",
        "D": "Sperm whale",
        "answer": "A"
    },
    "Who was the first president of the United States?": {
        "A": "George Washington",
        "B": "Thomas Jefferson",
        "C": "Abraham Lincoln",
        "D": "Franklin D. Roosevelt",
        "answer": "A"
    },
    "What is the highest mountain peak in the world?": {
        "A": "Mount Everest",
        "B": "K2",
        "C": "Kilimanjaro",
        "D": "Mount Olympus",
        "answer": "A"
    },
    "Who wrote the famous novel 'To Kill a Mockingbird'?": {
        "A": "F. Scott Fitzgerald",
        "B": "Harper Lee",
        "C": "Jane Austen",
        "D": "J.K. Rowling",
        "answer": "B"
    },
    "What is the chemical symbol for silver?": {
        "A": "Ag",
        "B": "Au",
        "C": "Hg",
        "D": "Pb",
        "answer": "A"
    },
    "Who was the ancient Greek philosopher who taught that 'know thyself'?": {
        "A": "Socrates",
        "B": "Plato",
        "C": "Aristotle",
        "D": "Epicurus",
        "answer": "A"
    },
    "What is the largest living structure on Earth?": {
        "A": "The Great Barrier Reef",
        "B": "The Amazon Rainforest",
        "C": "The Grand Canyon",
        "D": "The Great Wall of China",
        "answer": "A"
    },
    "Who was the first woman to fly solo across the Atlantic Ocean?": {
        "A": "Amelia Earhart",
        "B": "Charles Lindbergh",
        "C": "Wright Brothers",
        "D": "Jacqueline Cochran",
        "answer": "A"
    },
    "What is the chemical symbol for copper?": {
        "A": "Cu",
        "B": "Ag",
        "C": "Au",
        "D": "Pb",
        "answer": "A"
    },
    "Who wrote the famous play 'Hamlet'?": {
        "A": "William Shakespeare",
        "B": "Christopher Marlowe",
        "C": "John Webster",
        "D": "Ben Jonson",
        "answer": "A"
    },
    "What is the deepest part of the ocean?": {
        "A": "The Mariana Trench",
        "B": "The Great Blue Hole",
        "C": "The Challenger Deep",
        "D": "The Red Sea",
        "answer": "A"
    },
    "Who was the ancient Egyptian pharaoh who built the Great Pyramid of Giza?": {
        "A": "Khufu",
        "B": "Khafre",
        "C": "Menkaure",
        "D": "Ramses II",
        "answer": "A"
    },
    "What is the chemical symbol for lead?": {
        "A": "Pb",
        "B": "Hg",
        "C": "Cu",
        "D": "Ag",
        "answer": "A"
    },
    "Who was the famous physicist who developed the theory of relativity?": {
        "A": "Albert Einstein",
        "B": "Isaac Newton",
        "C": "Marie Curie",
        "D": "Galileo Galilei",
        "answer": "A"
    },
    "What is the largest desert in the world?": {
        "A": "Sahara Desert",
        "B": "Gobi Desert",
        "C": "Mojave Desert",
        "D": "Atacama Desert",
        "answer": "A"
    },
    "Who was the ancient Greek historian who wrote 'The Histories'?": {
        "A": "Herodotus",
        "B": "Thucydides",
        "C": "Xenophon",
        "D": "Polybius",
        "answer": "A"
    }
}

# Function to add a new question to the quiz
def add_question():
    question = input("Enter the question: ")
    options = {}
    for i in ["A", "B", "C", "D"]:
        options[i] = input(f"Enter option {i}: ")
    answer = input("Enter the correct answer (A/B/C/D): ")
    quiz_questions[question] = options
    quiz_questions[question]["answer"] = answer.upper()
    save_questions()

# Function to save questions to a JSON file
def save_questions():
    with open("questions.json", "w") as f:
        json.dump(quiz_questions, f)

# Function to load questions from a JSON file
def load_questions():
    global quiz_questions
    if os.path.exists("questions.json"):
        with open("questions.json", "r") as f:
            quiz_questions = json.load(f)

# Function to play the quiz
def play_quiz():
    score = 0
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    for question in questions:
        print(question)
        options = quiz_questions[question]
        for option, value in options.items():
            if option != "answer":
                print(f"{option}: {value}")
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == options["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {options['answer']}.\n")
    print(f"Quiz finished. Your score is {score}/{len(questions)}")

# Function to view all questions
def view_questions():
    for question, options in quiz_questions.items():
        print(question)
        for option, value in options.items():
            if option != "answer":
                print(f"{option}: {value}")
        print(f"Answer: {options['answer']}\n")

# Main function
def main():
    load_questions()
    while True:
        print("1. Play Quiz")
        print("2. Add Question")
        print("3. View Questions")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            play_quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            view_questions()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
