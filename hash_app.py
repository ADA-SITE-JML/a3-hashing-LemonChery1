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

            # Hash using xxhash and determine the bucket
            hash_value = xxhash.xxh32(user_input).intdigest()
            bucket_number = (hash_value % n) + 1  # +1 so buckets are 1-indexed
            filename = f"{bucket_number}.txt"

            # Write to appropriate bucket file
            with open(filename, 'a') as f:
                f.write(user_input + '\n')

            print(f"{user_input} added to {filename}")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
