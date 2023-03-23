def main():

    encoder = {"1":"4", "2":"5", "3":"6", "4":"7", "5":"8", "6":"9", "7":"0", "8":"1", "9":"2", "0":"3"}
    decoder = {"0":"7", "1":"8", "2":"9", "3":"0", "4":"1", "5":"2", "6":"3", "7":"4", "8":"5", "9":"6"}
    encoded = ""
    decoded = ""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ", end=(""))
        choice = input()

        if choice == "1":
            pass_to_encode = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            for num in pass_to_encode:
                encoded = encoded + encoder[num]

        elif choice == "2":

            for num in encoded:
                decoded = decoded + decoder[num]
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")

        elif choice == "3":
            pass






if __name__ == "__main__":
    main()