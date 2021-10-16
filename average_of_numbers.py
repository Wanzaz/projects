print("Zadávejte celá čísla za každým Enter: nebo jen Enter pro ukončení")

total = 0
count = 0 

while True:
  line = input("číslo: ")
  if line:
    try:
        number = int(line)
    except ValueError as err:
        print(err)
        continue
    total += number
    count += 1
  else:
     break 

if count:
  print("počet =", count, "celkem =", total, "průměr =", total/count)
