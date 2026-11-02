
import random

# Player information
name = input("What is your name? ")
print("Hello,", name)

# Words in the answer selection
words = [
        "rainbow",
        "computer",
        "science",
        "python",
        "water",
        "player",
        "reverse",
        "mountain",
        "keyboard",
        "elephant",
        "sunshine",
        "thunder",
        "library",
        "dinosaur",
        "galaxy",
        "pancake",
        "volcano",
        "penguin",
        "backpack",
        "treasure",
        "sandwich",
        "dragon",
        "wizard",
        "pumpkin",
        "chocolate",
        "squirrel",
        "tornado",
        "spaceship",
        "waterfall",
        "snowflake",
        "adventure",
        "fireworks",
        "jellyfish",
        "pineapple",
        "octopus",
        "hamburger",
        "starlight",
        "blueberry",
        "headphones",
        "butterfly"
        "software engineering",
        "computer science",
        "artificial intelligence",
        "machine learning",
        "object oriented programming",
        "data structures",
        "algorithm",
        "recursion",
        "debugging",
        "compiler",
        "binary",
        "encryption",
        "cybersecurity",
        "motherboard",
        "microprocessor",
        "virtual machine",
        "operating system",
        "network protocol",
        "database",
        "javascript",
        "typescript",
        "assembly language",
        "memory allocation",
        "stack overflow",
        "infinite loop",
        "segmentation fault",
        "syntax error",
        "exception handling",
        "garbage collection",
        "polymorphism",
        "inheritance",
        "encapsulation",
        "abstraction",
        "multithreading",
        "quantum computing",
        "neural network",
        "source code",
        "version control",
        "unit testing",
        "rubber duck debugging"
        "quincunx",
        "flibbertigibbet",
        "discombobulation",
        "kerfuffle",
        "bamboozle",
        "nincompoop",
        "gobbledygook",
        "hullabaloo",
        "shenanigans",
        "skedaddle",
        "whippersnapper",
        "codswallop",
        "malarkey",
        "lollygag",
        "hornswoggle",
        "cattywampus",
        "snollygoster",
        "collywobbles",
        "bumfuzzle",
        "fuddy duddy",
        "higgledy piggledy",
        "ragamuffin",
        "thingamajig",
        "whatchamacallit",
        "doodad",
        "doohickey",
        "gizmo",
        "flummox",
        "befuddled",
        "guffaw",
        "blubber",
        "wobble",
        "boondoggle",
        "skullduggery",
        "jabberwocky",
        "onomatopoeia",
        "sesquipedalian",
        "poppycock",
        "absquatulate",
        "persnickety"
        "mathematics",
        "physics",
        "chemistry",
        "astronomy",
        "astrophysics",
        "quantum mechanics",
        "thermodynamics",
        "photosynthesis",
        "electromagnetism",
        "gravitational waves",
        "black hole",
        "event horizon",
        "supernova",
        "neutron star",
        "dark matter",
        "periodic table",
        "mitochondria",
        "deoxyribonucleic acid",
        "chromosome",
        "evolution",
        "natural selection",
        "fibonacci sequence",
        "pythagorean theorem",
        "prime number",
        "quadratic equation",
        "trigonometry",
        "calculus",
        "hypotenuse",
        "probability",
        "statistics",
        "hypothesis",
        "experiment",
        "microscope",
        "telescope",
        "particle accelerator",
        "nuclear fusion",
        "nuclear fission",
        "radioactivity",
        "bioluminescence",
        "spectroscopy"
        "the cake is a lie",
        "have you tried turning it off and on again",
        "error between keyboard and chair",
        "it works on my machine",
        "hello world",
        "one does not simply",
        "the rubber duck knows",
        "beware the flying spaghetti monster",
        "my code has become self aware",
        "there is no spoon",
        "you just lost the game",
        "the answer is forty two",
        "never trust a smiling dragon",
        "the squirrels are plotting",
        "send more coffee",
        "keyboard warrior",
        "the floor is lava",
        "this is fine",
        "hold my coffee",
        "may the bugs be ever in your favor",
        "unexpected banana",
        "the goose is loose",
        "beware of the quantum duck",
        "the penguin has escaped",
        "spaghetti code strikes again",
        "not enough coffee",
        "the compiler is judging you",
        "another day another syntax error",
        "i blame the semicolon",
        "the cake has escaped",
        "my brain needs a reboot",
        "the wizard forgot his password",
        "there are no bugs only features",
        "the hamster runs the server",
        "the dragon ate my homework",
        "the matrix needs debugging",
        "too many tabs open",
        "the chickens know too much",
        "the toaster has gained sentience",
        "why is the rum gone"
    ]


# Select random word
word = random.choice(words)

print("\nWelcome to Hangman!")
print("Guess the characters to reveal the hidden word.\n")

# Store all guessed characters
guesses = ''

# Store only correct guesses
correct_guesses = ''

# Number of attempts
turns = 13

# Main Game
while turns > 0:
    failed = 0

    # Display guessed characters vs hidden characters
    for char in word:
        if char == ' ':
            print(" / ", end="")
        elif char in guesses:
            print(char, end="")
        else:
            failed += 1
            print("_", end="")

    print()

    # Display previously guessed correct letters
    if correct_guesses:
        print("Correct letters guessed:",
              ", ".join(correct_guesses))
    else:
        print("Correct letters guessed: None")

    print("Remaining attempts:", turns)
    print()

    # Check if the entire word has been guessed
    if failed == 0:
        print("Congratulations,", name + "!")
        print("You win!")
        print("The word was:", word)
        break

    # User input
    guess = input("Guess a character: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    # Check for duplicate guesses
    if guess in guesses:
        print("You have already guessed this character.\n")
        continue

    # Store the guess
    guesses += guess

    # Check whether the guess is correct
    if guess in word:
        correct_guesses += guess
        print("Correct guess!\n")

    else:
        turns -= 1
        print("Incorrect, try again.")
        print("You have", turns, "guesses left.\n")

        # Check if player has lost
        if turns == 0:
            print("Game Over!")
            print("You have lost the game.")
            print("The word was:", word)
            break
