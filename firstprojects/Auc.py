beds={}

products=["shoenen","Jas","Passer","Lover"]

for product in products:
    print("bedding for "+product)
    bedding = True
    while bedding:
        bed = int(input("Enter a bed: "))
        name = input("Enter your name: ")

        beds[name]=bed
        other=input("Another bed: ?")
        if other.lower() != "y":
            bedding=False
    biggest_key=0
    biggest_value = 0
    for key,value in beds.items():
        if biggest_value < value:
           biggest_key=key
           biggest_value=value
    print(f"{biggest_key}: {biggest_value}")