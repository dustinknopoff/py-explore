from glob import glob
with open("./sickpicks.md", "w+") as out:
    for fname in glob("/Users/Dustin/Documents/Gits/Web/Syntax/shows/*"):
        with open(fname, 'r') as f:
            contents = f.read()
            can_add = False
            picks = []
            for line in contents.split("\n"):
                if "## Sick Picks" in line:
                    can_add = True
                elif "## ××× SIIIIICK ××× PIIIICKS ×××" in line:
                    can_add = True
                elif "##" in line and can_add is True:
                    can_add = False
                elif can_add is True and line is not '':
                    out.write(line)
                    out.write("\n")