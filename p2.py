x = "123"

pr = []

for i in range(999)

      pr.append(str(i).zfill(6))

for pw in pr:

      if pw == x:

            print("Brute Force Attack Successful")

            print(pw)

            break

else:

     print("Brute Force Attack Failed")