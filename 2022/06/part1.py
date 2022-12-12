

if __name__ == "__main__":
    from _utils import load_data, load_example_data, detect_packet

    filename = "input.dat"
    if filename.endswith("example.dat"):
        sequences = load_example_data(filename)
    else:
        sequences = [load_data(filename)]

    for sequence in sequences:
        answer = detect_packet(sequence)
        question = "How many characters need to be processed before the first start-of-packet marker is detected?"

        print(f"{question} {answer}")
