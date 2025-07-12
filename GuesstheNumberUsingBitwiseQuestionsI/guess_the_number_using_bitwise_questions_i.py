def guess_the_number_bitwise():
    min_val = 1
    max_val = 100

    print(f"Think of a whole number between {min_val} and {max_val} (inclusive).")
    print("I will ask you a series of questions, and I will guess your number!")
    input("Press Enter when you have your number in mind...")

    guessed_number = 0
    num_bits = max_val.bit_length()

    for bit_pos in range(num_bits):
        numbers_with_bit_set = []
        for num in range(min_val, max_val + 1):
            if (num >> bit_pos) & 1:
                numbers_with_bit_set.append(num)

        if not numbers_with_bit_set:
            continue

        print(f"\nIs your number in the following set?")
        
        display_parts = []
        for i, num in enumerate(numbers_with_bit_set):
            display_parts.append(str(num))
            if (i + 1) % 10 == 0 and i < len(numbers_with_bit_set) - 1:
                display_parts.append("\n")
        print(", ".join(display_parts))

        while True:
            answer = input("Enter 'yes' or 'no': ").strip().lower()
            if answer == 'yes':
                guessed_number |= (1 << bit_pos)
                break
            elif answer == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    print(f"\nYour number is {guessed_number}!")
    print("I guessed it!")

if __name__ == "__main__":
    guess_the_number_bitwise()