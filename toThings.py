import requests, re
import webbrowser

content = """# Groceries
#todo
---
## Costco
- Broccoli
- Asparagus
- Green Beans
- Thighs
- Breasts
- Skirt Steak
+ Salmon
- *Olive Oil*

## Star Market
+ Tomatoes
+ Garlic
+ Onions
+ Mushrooms
- Zucchini
- Canned Tomatoes
- Frozen Veggies
- Cauliflower
- Fresh Mozzarella 
+ Shredded Mozzarella 
+ Prosciutto 
+ Hot sauce
+ Prosciutto or pepperoni 
+ Lemons
+ Shrimp/Seafood Mix
## Target
+ Body Wash
+ Paper Towels
+ Floss picks
+ Tin foil
+ Garbage bags 
+ Hand soap refill
+ Wipes"""

headings = re.findall(r'# .*?\n', content)
tasks = re.findall(r'[+] .*?\n', content)
finalH = []
finalT = []
print(tasks[0].replace("+ ", "").replace("\n", ""))
for head in headings:
    finalH.append(head.replace("# ", "").replace("\n", ""))
for task in tasks:
    finalT.append(task.replace("+ ", "").replace("\n", "").replace(" ", "%20"))
str = finalH[0]
output = "things:///add?title=" + str.replace(" ", "") + "&checklist-items="
counter = 0;
for t in finalT:
    if counter == len(finalT) - 1:
        output += t
    else:
        output += t + '%0A'
        counter += 1
webbrowser.open(output)