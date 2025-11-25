# CAESAR CIPHER DECRYPTION TOOL (Frequency Analysis & Brute Force)

# Global Constant: 26-letter ALPHABET in order to check or map encrypted messages from user input
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# === FUNDAMENTAL FUNCTIONS ===
def calculate_frequency(alphabet, encrypted_string):
    """
    Calculates the frequency of each character in the encrypted message

    :param alphabet: reference alphabet (a to z)
    :param encrypted_string: user input (ciphertext)
    :return: A dictionary that maps each character to its frequency
    """
    # Initialize the dictionary to store values, all set to zero
    freq_analysis_dict = {letter: 0 for letter in alphabet}

    # Translate all characters to lowercase so frequency accuracy can be improved
    normalized_string = encrypted_string.lower()

    # Count frequences in one pass
    for char in normalized_string:
        if char in freq_analysis_dict:
            freq_analysis_dict[char] += 1
    return freq_analysis_dict

def decrypt_one_shift(alphabet, encrypted_string, shift):
    """
    Decrypts the encrypted message by using a single, specific value for shift

    :param alphabet: reference alphabet (a to z)
    :param encrypted_string: user input (ciphertext)
    :param shift: the number of positions to shift back / to the left
    :return: the decrypted message (plaintext)
    """
    decrypted_string = ""

    for char in encrypted_string:
        # Non-alphabetic characters such as spaces, punctuation, and the like are simply appended
        if char not in alphabet:
            decrypted_string += char
            continue

        # Find the letter's index (0 - 25)
        alphabet_index = alphabet.index(char)

        # Decryption Logic (Modular Arithmetic):
        # Plaintext Index = (Cipertext Index - Shift) MOD 26
        # Using Modulo Operator will give us only positive numbers
        # that don't go beyond the numbers of the alphabet (26)
        decrypted_index = (alphabet_index - shift) % 26

        # Append the resulting letter
        decrypted_string += alphabet[decrypted_index]
    return decrypted_string

def brute_force_decryption(alphabet, encrypted_string):
    """
    Executes brute-force decryption on the encrypted message by trying every possible shift (0-25)
    :param alphabet: reference alphabet (a to z)
    :param encrypted_string: user input (ciphertext)
    :return: A dictionary that contains all 26 decryption results
    """
    all_decrypted_strings = {}

    for shift in range(26):
        # Reuse the single-shift decryption function above
        decrypted_string = decrypt_one_shift(alphabet, encrypted_string, shift)
        all_decrypted_strings[shift] = decrypted_string
        # Output is printed so the user can observe which text is meaningful, thereby discovering the decrypted message
        print(f"Decrypted message {shift}: \n{decrypted_string}")
    return all_decrypted_strings

# Get user input (encrypted message)
encrypted_string = input("Enter encrypted message: ")

# Calculate the letter counts
freq_analysis = calculate_frequency(ALPHABET, encrypted_string)

print("Alphabet: ", ALPHABET)
print("Frequency Analysis: \n", freq_analysis)

print("Encrypted String: ", encrypted_string)

# Find letter that has the highest frequency in the freq_analysis dictionary
most_common_letter = max(freq_analysis, key=freq_analysis.get)

print("Most common letter: ", most_common_letter)

# Calculate the shift which we're assuming it's 'e' since one method of decryption
# is the most common letter decryption method
shift = (ALPHABET.index(most_common_letter) - ALPHABET.index('e')) % 26
print("Shift: ", shift)
print()

# Decrypt user string by using the most common letter shift
decrypted_freq_string = decrypt_one_shift(ALPHABET, encrypted_string, shift)
print("***Frequency Analysis Decryption***")
print("Frequency Decryption: ", decrypted_freq_string)
print()

# Decrypt user string by brute-force, checking all possible shifts (0-25)
print("***Brute-Force Decryption***")
brute_decryptions = brute_force_decryption(ALPHABET, encrypted_string)


