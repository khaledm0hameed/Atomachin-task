import time

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    print("You will have 1 minute to type as many words as you can.")
    print("Start typing after the countdown.")

    # Countdown before starting
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    start_time = time.time()

    # User types
    typed_words = input("Start typing: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Count the number of words typed
    word_count = len(typed_words.split())

    # Calculate words per minute
    wpm = word_count / (elapsed_time / 60)

    print(f"\nWords per minute: {wpm:.2f}")

# Run the typing speed test
typing_speed_test()
