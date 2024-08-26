import tkinter as tk


def binary_to_ddn():
    octet1 = 0
    octet2 = 0
    octet3 = 0
    octet4 = 0
    binaryNumber = userField.get()

    if binaryNumber[0] == "1":
        octet1 += 128
    if binaryNumber[1] == "1":
        octet1 += 64
    if binaryNumber[2] == "1":
        octet1 += 32
    if binaryNumber[3] == "1":
        octet1 += 16
    if binaryNumber[4] == "1":
        octet1 += 8
    if binaryNumber[5] == "1":
        octet1 += 4
    if binaryNumber[6] == "1":
        octet1 += 2
    if binaryNumber[7] == "1":
        octet1 += 1
    if binaryNumber[9] == "1":
        octet2 += 128
    if binaryNumber[10] == "1":
        octet2 += 64
    if binaryNumber[11] == "1":
        octet2 += 32
    if binaryNumber[12] == "1":
        octet2 += 16
    if binaryNumber[13] == "1":
        octet2 += 8
    if binaryNumber[14] == "1":
        octet2 += 4
    if binaryNumber[15] == "1":
        octet2 += 2
    if binaryNumber[16] == "1":
        octet2 += 1
    if binaryNumber[18] == "1":
        octet3 += 128
    if binaryNumber[19] == "1":
        octet3 += 64
    if binaryNumber[20] == "1":
        octet3 += 32
    if binaryNumber[21] == "1":
        octet3 += 16
    if binaryNumber[22] == "1":
        octet3 += 8
    if binaryNumber[23] == "1":
        octet3 += 4
    if binaryNumber[24] == "1":
        octet3 += 2
    if binaryNumber[25] == "1":
        octet3 += 1
    if binaryNumber[27] == "1":
        octet4 += 128
    if binaryNumber[28] == "1":
        octet4 += 64
    if binaryNumber[29] == "1":
        octet4 += 32
    if binaryNumber[30] == "1":
        octet4 += 16
    if binaryNumber[31] == "1":
        octet4 += 8
    if binaryNumber[32] == "1":
        octet4 += 4
    if binaryNumber[33] == "1":
        octet4 += 2
    if binaryNumber[34] == "1":
        octet4 += 1
    userField.delete(0, tk.END)
    userField.insert(0, str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4))


def ddn_to_binary():
    ddnNumber = userField.get()
    ddnList = []
    for octet in ddnNumber.split('.'):
        ddnList.append(octet)
    octetOne = int(ddnList[0])
    octetTwo = int(ddnList[1])
    octetThree = int(ddnList[2])
    octetFour = int(ddnList[3])
    binaryOne = []
    binaryTwo = []
    binaryThree = []
    binaryFour = []
    if octetOne >= 128:
        binaryOne.append("1")
        octetOne -= 128
    else:
        binaryOne.append("0")
    if octetOne >= 64:
        binaryOne.append("1")
        octetOne -= 64
    else:
        binaryOne.append("0")
    if octetOne >= 32:
        binaryOne.append("1")
        octetOne -= 32
    else:
        binaryOne.append("0")
    if octetOne >= 16:
        binaryOne.append("1")
        octetOne -= 16
    else:
        binaryOne.append("0")
    if octetOne >= 8:
        binaryOne.append("1")
        octetOne -= 8
    else:
        binaryOne.append("0")
    if octetOne >= 4:
        binaryOne.append("1")
        octetOne -= 4
    else:
        binaryOne.append("0")
    if octetOne >= 2:
        binaryOne.append("1")
        octetOne -= 2
    else:
        binaryOne.append("0")
    if octetOne >= 1:
        binaryOne.append("1")
        octetOne -= 1
    else:
        binaryOne.append("0")
    if octetTwo >= 128:
        binaryTwo.append("1")
        octetTwo -= 128
    else:
        binaryTwo.append("0")
    if octetTwo >= 64:
        binaryTwo.append("1")
        octetTwo -= 64
    else:
        binaryTwo.append("0")
    if octetTwo >= 32:
        binaryTwo.append("1")
        octetTwo -= 32
    else:
        binaryTwo.append("0")
    if octetTwo >= 16:
        binaryTwo.append("1")
        octetTwo -= 16
    else:
        binaryTwo.append("0")
    if octetTwo >= 8:
        binaryTwo.append("1")
        octetTwo -= 8
    else:
        binaryTwo.append("0")
    if octetTwo >= 4:
        binaryTwo.append("1")
        octetTwo -= 4
    else:
        binaryTwo.append("0")
    if octetTwo >= 2:
        binaryTwo.append("1")
        octetTwo -= 2
    else:
        binaryTwo.append("0")
    if octetTwo >= 1:
        binaryTwo.append("1")
        octetTwo -= 1
    else:
        binaryTwo.append("0")
    if octetThree >= 128:
        binaryThree.append("1")
        octetThree -= 128
    else:
        binaryThree.append("0")
    if octetThree >= 64:
        binaryThree.append("1")
        octetThree -= 64
    else:
        binaryThree.append("0")
    if octetThree >= 32:
        binaryThree.append("1")
        octetThree -= 32
    else:
        binaryThree.append("0")
    if octetThree >= 16:
        binaryThree.append("1")
        octetThree -= 16
    else:
        binaryThree.append("0")
    if octetThree >= 8:
        binaryThree.append("1")
        octetThree -= 8
    else:
        binaryThree.append("0")
    if octetThree >= 4:
        binaryThree.append("1")
        octetThree -= 4
    else:
        binaryThree.append("0")
    if octetThree >= 2:
        binaryThree.append("1")
        octetThree -= 2
    else:
        binaryThree.append("0")
    if octetThree >= 1:
        binaryThree.append("1")
        octetThree -= 1
    else:
        binaryThree.append("0")
    if octetFour >= 128:
        binaryFour.append("1")
        octetFour -= 128
    else:
        binaryFour.append("0")
    if octetFour >= 64:
        binaryFour.append("1")
        octetFour -= 64
    else:
        binaryFour.append("0")
    if octetFour >= 32:
        binaryFour.append("1")
        octetFour -= 32
    else:
        binaryFour.append("0")
    if octetFour >= 16:
        binaryFour.append("1")
        octetFour -= 16
    else:
        binaryFour.append("0")
    if octetFour >= 8:
        binaryFour.append("1")
        octetFour -= 8
    else:
        binaryFour.append("0")
    if octetFour >= 4:
        binaryFour.append("1")
        octetFour -= 4
    else:
        binaryFour.append("0")
    if octetFour >= 2:
        binaryFour.append("1")
        octetFour -= 2
    else:
        binaryFour.append("0")
    if octetFour >= 1:
        binaryFour.append("1")
        octetFour -= 1
    else:
        binaryFour.append("0")
    formattedBinary1 = ''.join(binaryOne)
    formattedBinary2 = ''.join(binaryTwo)
    formattedBinary3 = ''.join(binaryThree)
    formattedBinary4 = ''.join(binaryFour)
    userField.delete(0, tk.END)
    userField.insert(0,str(formattedBinary1)+"."+str(formattedBinary2)+"."+str(formattedBinary3)+"."+str(formattedBinary4))


window = tk.Tk()
window.geometry("400x400")

binaryText = tk.Label(text="Enter information below")
userField = tk.Entry(width=40)
binaryConvert = tk.Button(text="Binary to DDN", command=binary_to_ddn)
ddnToBinary = tk.Button(text="DDN to Binary", command=ddn_to_binary)


binaryText.pack(padx=4, pady=4)
userField.pack(padx=4, pady=4)
binaryConvert.pack(padx=4, pady=4)
ddnToBinary.pack(padx=4, pady=4)
window.mainloop()
