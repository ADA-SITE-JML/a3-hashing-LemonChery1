# A3.Hashing
## Option A

**A hash bucket system using a fast hashing algorithm.** 
This is the third assignment of this course (`A3`) designed to check the hashing and file storage skills attained.

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

### Setting up

In this stage, I will add **command-line argument handling** to accept two parameters which are:
- `n` (number of hash buckets)
- `s` (bucket size, unused for now, might be useful for Option B later)

### **Code after the 1st Set-up**
```python
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

  
