#Alternative way of wiriting open statement
#data = open("primary-bin.000001.decoded.txt", "r")
#Lines = data.readlines()
filename = "primary-bin.000001.decoded.txt"
with open(filename, "r") as file:
   Lines = file.readlines()

data = []
less_data = []
more_data = []
count = 0

for line in Lines:
    count += 1
    if "###" in line:
        data.append("Line{}: {}\n".format(count, line.strip()))
        #print("Line{}: {}".format(count, line.strip()))
        
    elif "#221201" in line:
        less_data.append("Line{}: {}\n".format(count, line.strip()))
        #print("Line{}: {}".format(count, line.strip()))
    
    elif "/*!" in line:
        more_data.append("Line{}: {}\n".format(count, line.strip()))
        #print("Line{}: {}".format(count, line.strip()))

#Print statement used for debugging and seeing if desired information is appended
#print("Line{}: {}".format(count, line.strip()))

#Outputting data to a text file:

with open("useful_data.txt", "w") as f:
    f.write("Data taken from {} \n".format(filename))
    f.write("Line numbers make reference to position in file: \n\n")
    f.write("Queries made by users: \n")
    f.write(" ".join(map(str,data)))
    f.write("\n")
    f.write("Date and Time of opened sessions: \n")
    f.write(" ".join(map(str,less_data)))
    f.write("\n")
    f.write("Session opened: \n")
    f.write(" ".join(map(str,more_data)))
    f.write("\n")