# A3.Hashing
## Option A

**A hash bucket system using a fast hashing algorithm.** 
This is the third assignment of this course (`A3`) designed to check the hashing and file storage skills attained. Here is the implementation of option A of this assignment using Python.

## Objective

This project uses an application called `hash_app` which:

- Uses a fast hash function called **xxHash**
- Maps string inputs into **`n` of hash bucket files** (`1.txt` to `n.txt`)
- Allows collisions (multiple values per file)
- Accepts user input in a loop until manually stopped (by CTRL^C)

  ## Getting Started

  ### Prerequisites

  Prerequisites before starting the code include:

- Python 3.7 or above
- The `xxhash` library installation

**Install `xxhash`:**

```
pip install xxhash
```
### 1. Setting up

In this stage, I will add **command-line argument handling** to accept two parameters which are:
- `n` (number of hash buckets)
- `s` (bucket size, unused for now, might be useful for Option B later)

### **Code after the 1st Set-up**
```
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_app.py <num_buckets> <bucket_size>")
        return

    try:
        n = int(sys.argv[1])
        s = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        return

    print(f"Hashing into {n} buckets. Bucket size limit: {s} (not obligated)")

    if __name__ == "__main__":
      main()

### 2. Integrating hashing and adding file storage

  Now, I introduce hashing using xxhash and assign each input to a specific bucket file (like 1.txt, 2.txt, ... n.txt).

### **Code after adding hashing and file storage**
```
import sys
import xxhash

def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_app.py <num_buckets> <bucket_size>")
        return

    try:
        n = int(sys.argv[1])
        s = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        return

    print(f"Hashing into {n} buckets. Bucket size limit: {s} (not enforced in this version)")

    while True:
        user_input = input("Please enter the string: ").strip()
        if user_input == "":
            continue

        # Hashing using xxhash and determining the bucket
        hash_value = xxhash.xxh32(user_input).intdigest()
        bucket_number = (hash_value % n) + 1  # +1 so buckets are 1-indexed
        filename = f"{bucket_number}.txt"

        # Writing to appropriate bucket file
        with open(filename, 'a') as f:
            f.write(user_input + '\n')

        print(f"{user_input} added to {filename}")

    if __name__ == "__main__":
        main()

```
### 3. Interactive Input Loop & Exit Handling

Finally, I add a continuous user input loop, exit with CTRL^C, hash-based bucket allocation using xxhash. 
Furthermore, it will write to 1.txt to n.txt depending on the hash result. As a result, implementing the exit handling and interactive input loop will grant us the completed version of my code.
### **Final version of the code**
```
 import sys
 import xxhash

 def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_app.py <num_buckets> <bucket_size>")
        return

    try:
        n = int(sys.argv[1])
        s = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        return

    print(f"Hashing into {n} buckets. Bucket size limit: {s} (not enforced in this version)")

    try:
        while True:
            user_input = input("Please enter the string: ").strip()
            if user_input == "":
                continue

            # Hashing using xxhash and determining the bucket
            hash_value = xxhash.xxh32(user_input).intdigest()
            bucket_number = (hash_value % n) + 1  # +1 so buckets are 1-indexed
            filename = f"{bucket_number}.txt"

            #  Writing to appropriate bucket file
            with open(filename, 'a') as f:
                f.write(user_input + '\n')

            print(f"{user_input} added to {filename}")
    except KeyboardInterrupt:
        print("\nExiting...")

    if __name__ == "__main__":
      main()
