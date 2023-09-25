def Billboard(str1, str2):
    val_arr = [None]*4

    sz1 = len(str1)
    sz2 = len(str2)

    up_arr = whole_board[0]
    down_arr = whole_board[1]
    for i in range(len(str1)):
        up_arr[i] = str1[i]
        if ord(str1[i]) >= 65 and ord(str1[i]) <= 90:
            s1 = i

    for i in range(len(str2)):
        down_arr[i] = str2[i]
        if ord(str2[i]) >= 65 and ord(str2[i]) <= 90:
            s2 = i
    val_arr[0] = whole_board[0][s1]
    val_arr[1] = s1
    val_arr[2] = whole_board[1][s2]
    val_arr[3] = s2

    print("Top Board Start Character:", val_arr[0])
    print("Top Board Start Index:", val_arr[1])
    print("Bottom Board Start:", val_arr[2])
    print("Bottom Board Start Index:", val_arr[3])

    output(whole_board, s1, s2, sz1, sz2, val_arr)


def output(arr, s1, s2, sz1, sz2, val_arr):
    logic = True
    k = s1
    l = s2
    while logic:
        take_in = input("Press any key and then press enter to continue!!!")
        if take_in=="q" or take_in=="Q":
            print("Top Board Start Character:", val_arr[0])
            print("Top Board Start Index:", val_arr[1])
            print("Bottom Board Start:", val_arr[2])
            print("Bottom Board Start Index:", val_arr[3])

            break


        print("\n")
        for i in range(len(arr[0])):
            print(arr[0][k], end="")
            k = (k-1)%len(arr[0])
            if k==-1:
                k = len(arr[0])-1

        print('\n')

        for i in range(len(arr[1])):
            print(arr[1][l], end="")
            l = (l+1)%len(arr[1])

        print("\n")

        k = k-1
        if k==-1:
            k = len(arr[0])-1
        l = (l+1)%len(arr[1])


user_input1 = input()
user_input2 = input()



if len(user_input1)>10 or len(user_input2)>10:
    print("Invalid Input Size!!!")

else:
    print("Your input is valid. Press any key and then press enter to continue!!!")
    whole_board = [[""]*10, [""]*10]

    Billboard(user_input1, user_input2)



