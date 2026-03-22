import time
while True:
    target_word = "hello"

    print(f"Type the word: {target_word}")
    print("Timer starts when you enter the first letter and ends when you enter the letter.\n")

    typed = ""
    start_time = None

    while True:
        if typed.strip() == target_word or len(typed.strip()) > len(target_word)n:
            break:
            break
        
        char = input("Enter next character: ")

        if not char:
            continue
        if typed == "":
            char = char[0]

        if start_time is None:
            start_time = time.time()

        if char == " ":
            end_time = time.time()
            break

        typed += char
    end_time = time.time()
    elapsed = end_time - start_time

    print("\n--- Result ---")
    print(f"Your input: {typed}")
    print(f"Target word: {target_word}")
    print(f"Time taken: {elapsed:.3f} seconds")

    if typed.strip() == target_word:
        print("Correct!")
    else:
        print("Incorrect.")