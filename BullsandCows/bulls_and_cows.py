def getHint(secret: str, guess: str) -> str:
    bulls = 0
    cows = 0
    
    secret_counts = [0] * 10
    guess_counts = [0] * 10
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_digit = int(secret[i])
            guess_digit = int(guess[i])
            
            secret_counts[secret_digit] += 1
            guess_counts[guess_digit] += 1
            
    for i in range(10):
        cows += min(secret_counts[i], guess_counts[i])
            
    return f"{bulls}A{cows}B"