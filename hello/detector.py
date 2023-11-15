import json

with open("./aleo2json.json", "r") as f:
    aleo2json = json.load(f)

print(f"{aleo2json}")

result = False

insts = aleo2json["functions"]["main"]["instructions"]
for inst in insts:
    tokens = inst["str"].strip(";").split()
    #match tokens:
     #   case ["div", r0, r1, "into", r3]:
      #      a = b
       # case _:
        #    pass
for inst in insts:
    tokens = inst["str"].strip(";").split()
    if tokens[0] == "div":
        result = True
print(f"result: {result}")