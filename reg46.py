import re

txt = '-if smalldemo.txt -iv text -o out -speed 2'.strip()
file = re.findall(r'(?<=-if).\w+', txt)[0].strip()
view = re.findall(r'(?<=-iv).\w+', txt)[0].strip()
out = re.findall(r'(?<=-o).\w+', txt)[0].strip()
speed = int(re.findall(r'(?<=-speed).\w+', txt)[0].strip())
print(file, view, out, speed)

# Equivalent in Java
# Pattern p = Pattern.compile(file);
# Matcher m = p.matcher(txt);
# print(m.find());
