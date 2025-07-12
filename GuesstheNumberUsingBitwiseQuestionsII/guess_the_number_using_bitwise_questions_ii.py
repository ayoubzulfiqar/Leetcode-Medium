def guess_the_number_bitwise():
    print("Think of a whole number between 1 and 100 (inclusive).")
    print("I will try to guess it by asking you questions.")
    print("Please answer 'yes' or 'no'.")

    min_val = 1
    max_val = 100
    
    num_bits = (max_val).bit_length()

    current_guess = 0

    for i in range(num_bits - 1, -1, -1):
        bit_value = 1 << i
        
        hypothetical_guess = current_guess | bit_value

        if hypothetical_guess > max_val:
            continue

        while True:
            question_val = current_guess + bit_value
            response = input(f"Is your number greater than or equal to {question_val}? (yes/no): ").lower().strip()

            if response == 'yes':
                current_guess += bit_value
                break
            elif response == 'no':
                break
            else:
                print("Please answer 'yes' or 'no'.")

    if current_guess < min_val or current_guess > max_val:
        print(f"I couldn't guess your number within the range {min_val}-{max_val}, or you might have given inconsistent answers.")
        print(f"My final guess based on your answers was: {current_guess}")
    else:
        print(f"Is your number {current_guess}?")
        final_response = input("(yes/no): ").lower().strip()
        if final_response == 'yes':
            print("Great! I guessed it!")
        else:
            print("Oh no! I seem to have made a mistake, or perhaps there was an inconsistency in your answers.")
            print(f"My final guess was {current_guess}.")

guess_the_number_bitwise()