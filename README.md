# Random Password Generator (Beginner-Friendly)

This is a simple Python program that generates a random password using numbers, symbols, uppercase, and lowercase letters.  
It’s written in a beginner-friendly way, building the password one character at a time.

## How It Works
1. **Import libraries**  
   - `string` → gives us letters, numbers, and symbols without typing them manually.  
   - `random` → lets us pick characters randomly.

2. **Create the character pool**  
   ```python
   characters = string.digits + string.punctuation + string.ascii_letters
   ```

3. **Set the password length** <br>
    -length = 12

4. **Build the password**<br>
   -Start with an empty string password = "".
   -Loop length times.
   -Each time, pick a random character from the pool and add it to the password.
   


**How the password building works in the loop** <br>
   Start: ""<br> 
Loop 1 → pick "A" → "A"<br>
Loop 2 → pick "7" → "A7"<br>
Loop 3 → pick "!" → "A7!"<br>
Loop 4 → pick "q" → "A7!q"<br>
Loop 5 → pick "M" → "A7!qM"<br>
...<br>
Loop 12 → pick "z" → "A7!qM...z" <br>

**Why we initially set the password variable as empty string "" and not as 0**
Becase we need it to be a string, as the characters are a string hence we will get an error if we add password and characters if both arent string.

