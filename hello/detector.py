import json

with open("./aleo2json.json", "r") as f:
    json_obj = json.load(f)

print(f"{json_obj}")

result = False

insts = json_obj["functions"]["main"]["instructions"]
for inst in insts:
    tokens = inst["str"].strip(";").split()
    match tokens:
        case ["div", r0, r1, "into", r3]:
            pass
        case _:
            pass
for inst in insts:
    tokens = inst["str"].strip(";").split()
    #if tokens[0] == "div":
     #   result = True
print(f"result: {result}")