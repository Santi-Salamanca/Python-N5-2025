badges = int(input("Please enter the number of Badges you would like to buy: "))
if badges >= 150:
    print("your order will cost " + str((badges/100 * 90)/4) + "£")
else:
    print("Your badges will cost " + str(badges/4) + "£")