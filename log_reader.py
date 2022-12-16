#import struct
#PY3K = sys.version_info >= (3, 0)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", "'", "0", "1", "2", "3", "4", "5", "@"]
a_lower = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y"]
final = []
primal = []

with open("primary-bin.000001", "rb") as file:
   data = file.read()
   decode_data = data.decode(encoding = "latin-1")
   primal.append(data)


for i in decode_data:
   if i in alphabet:
      final.append(i + " ")
   elif i in a_lower:
      final.append(i + " ")
   else:
      continue

print(''.join(str(c) for c in final))

with open("out.txt", "w") as f:
   f.write(" ".join(map(str,final)))
   f.write("\n")

   #print(' '.join(str(c) for c in decode_data))


#     lines = []
#     for line in data:
#          if not PY3K:
#               lines.append(line)
#          else:
#               lines.append(line.decode('utf-8', 'backslashreplace'))