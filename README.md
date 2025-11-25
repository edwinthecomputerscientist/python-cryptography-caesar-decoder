# python-cryptography-caesar-decoder
Python cryptanalysis tool that breaks Caesar ciphers using frequency analysis and brute-force.

## Overview

This Python tool performs classical cryptanalysis on Caesar ciphers.  
It identifies the most frequent character in the ciphertext, estimates the most likely shift based on English letter distribution (assuming **'e'** is most common), and attempts decryption.  
It also performs a complete brute-force attack (all 26 shifts) and prints every possible plaintext.


### Features

- Counts frequency of each letter (a–z)

- Identifies the most common letter in the ciphertext

- Calculates the likely shift and decrypts automatically

- Brute-force mode that prints all 26 possible decryptions

- Handles spaces and non-alphabet characters gracefully

- Clean, modular function design

### Concepts Demonstrated

- Classical cryptography (Caesar cipher)

- Frequency analysis and cryptanalytic reasoning

- Modular arithmetic

- Algorithm design in Python

- Brute-force attack automation

## Example Output
Enter encrypted message: ymnx nx f xjhwjy  
Most common letter: x  
Calculated shift (freq guess): 19   # frequency-guess may be wrong on short texts  
Frequency Decryption (using guessed shift): ... (may be incorrect)  

***Brute-Force Decryption***  
Decrypted message 0: ymnx nx f xjhwjy  
Decrypted message 1: xlmw mw e wigvix  
Decrypted message 2: wklv lv d vhfuhw  
Decrypted message 3: vjku ku c ugetgv  
Decrypted message 4: uijt jt b tfdsfu  
Decrypted message 5: this is a secret  
...  
Decrypted message 25: znoy oy g ykixkz  
