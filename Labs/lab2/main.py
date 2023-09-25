def main():
    input1 = input("Enter first line of text: ")
    input2 = input("Enter second line of text: ")

    # Validate input length
    if len(input1) > 10 or len(input2) > 10:
        print("Invalid Input Size")
        return

    billboard = [[""] * 10, [""] * 10]

    # Store input in the billboard array
    for i in range(len(input1)):
        billboard[0][i] = input1[i]

    for i in range(len(input2)):
        billboard[1][i] = input2[i]

    # Find the starting index and starting character of each dimension
    start_index = [0, 0]
    start_char = ["", ""]
    for i in range(2):
        for j in range(10):
            if ord(billboard[i][j]) >= 65 and ord(billboard[i][j]) <= 90:
                start_index[i] = j
                start_char[i] = billboard[i][j]
                break

    print("Starting index of top row:", start_index[0])
    print("Starting character of top row:", start_char[0])
    print("Starting index of bottom row:", start_index[1])
    print("Starting character of bottom row:", start_char[1])

    # Loop to display the billboard
    while True:
        user_input = input("Enter any character (Q to quit): ")
        if user_input.lower() == "q":
            break

        # Shift the top row to the left and the bottom row to the right
        start_index[0] = (start_index[0] - 1 + 10) % 10
        start_index[1] = (start_index[1] + 1) % 10

        # Display the billboard
        for i in range(2):
            row = billboard[i][start_index[i]:] + billboard[i][:start_index[i]]
            print("".join(row))

    # Display the final state of the billboard
    print("Final state of the billboard:")
    print("Starting index of top row:", start_index[0])
    print("Starting character of top row:", start_char[0])
    print("Starting index of bottom row:", start_index[1])
    print("Starting character of bottom row:", start_char[1])


main()