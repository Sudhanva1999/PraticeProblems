def read_file(filename):
    data = {}
    max_term = 0

    with open(filename, 'r') as file:
        for line in file:
            term, word = line.strip().split()
            term = int(term)
            data[term] = word

            # Find the largest term fitting the given sequence
            while max_term * (max_term + 1) // 2 <= term:
                max_term += 1

    return data, max_term

def generate_secret_message(data, max_term):
    # Check if all terms preceding the max_term are present
    for i in range(1, max_term + 1):
        if i * (i + 1) // 2 not in data:
            print("Incomplete secret message.")
            return

    # Concatenate words in the proper sequence
    secret_message = ''.join(data[i * (i + 1) // 2] for i in range(1, max_term + 1))

    print("Secret Message:", secret_message)


if __name__ == "__main__":
    filename = "sample.txt"  # Replace with the actual file name
    data, max_term = read_file(filename)

    if max_term > 0:
        generate_secret_message(data, max_term)