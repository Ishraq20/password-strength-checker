# Password Strength Checker + Hash Generator

A CLI-based Python tool developed for the field training requirements at Irbid National University to evaluate the strength of passwords and JWT Secrets, and generate SHA-256 hashes for secure password storage.

## How Hashing Works
Hashing is a one-way cryptographic function that takes an input (plain text password) and maps it to a fixed-size string of characters (Hash). 

### Key Concepts:
1. **One-Way Function:** Once a password is converted into a hash, it cannot be reversed or decrypted back into the original plain text.
2. **Deterministic:** The same input will always produce the exact same hash output.
3. **Security Purpose:** Databases store hashes instead of plain text passwords. If a security breach occurs, attackers only get useless hashes, keeping user credentials safe during authentication.
