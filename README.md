# Password Strength Checker + Hash Generator

A CLI-based Python tool developed for the field training requirements to evaluate the strength of passwords and JWT Secrets, applying software engineering best practices like input validation and cryptographic hashing.

## Features
* **Password Validation:** Checks length, casing (upper/lower), digits, and special characters.
* **JWT Secret Screening:** Blocks common weak defaults (like 'admin' or '123456') and enforces a 16-character minimum.
* **SHA-256 Hashing:** Automatically generates a secure cryptographic digest for valid passwords.

## Technical Concepts Applied

### How Hashing Works
Hashing is a one-way cryptographic function that takes an input (plain text password) and maps it to a fixed-size string of characters (Hash). 

1. **One-Way Function:** Once a password is converted into a hash, it cannot be reversed or decrypted back into the original plain text.
2. **Deterministic:** The same input will always produce the exact same hash output.
3. **Security Purpose:** Databases store hashes instead of plain text passwords. If a security breach occurs, attackers only get useless hashes, keeping user credentials safe during authentication.

## How to Run
To run the tool locally, make sure you have Python installed, then execute:
```bash
python main.py
