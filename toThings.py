import requests, re
import webbrowser #, appex

# For Testing
content = """# My App Wishlist
#wants
---
+ Pythonista 3 $9.99 [Check it out](https://itunes.apple.com/us/app/pythonista-3/id1085978097?mt=8&uo=4)
+ Fantastical 2 for iPad $15.99 [Check it out](https://itunes.apple.com/us/app/fantastical-2-for-iphone/id718043190?mt=8&uo=4)
- Things 3 for iPad $19.99 [Check it out](https://itunes.apple.com/us/app/things-3-for-ipad/id904244226?mt=8&uo=4) 
+ iA Writer $4.99 [Check it out](https://itunes.apple.com/us/app/ia-writer/id775737172?mt=8&uo=4)
+ Screens VNC $14.99 [Check it out](https://itunes.apple.com/us/app/screens-vnc/id655890150?mt=8&uo=4)
+ Things 3 for Mac $49.99 [Check it out](https://itunes.apple.com/us/app/things-3/id904280696?mt=12).
- Affinity Photo for Mac $49.99 [Check it out]( https://itunes.apple.com/us/app/affinity-photo/id824183456?mt=12)
- Affinity Designer for Mac $49.99 [Check it out](https://itunes.apple.com/us/app/affinity-designer/id824171161?mt=12)
- Kaleidoscope 2 $19.99 [Check it out](https://itunes.apple.com/us/app/kaleidoscope-2/id1273771160?mt=8&uo=4)
- Dash $24.99 [Check it out](https://kapeli.onfastspring.com/dash) (50% off for students)
- Alfred (Powerpack) ￡35 [Check it out](https://www.alfredapp.com/powerpack/) ($50)
+ FileBrowser - Computers+Cloud $5.99 [Check it out](https://itunes.apple.com/us/app/filebrowser-computers-cloud/id364738545?mt=8&uo=4)
- lire (Full-text RSS) $6.99 [Check it out](https://itunes.apple.com/us/app/lire-full-text-rss/id550441545?mt=8&uo=4)
- iCab Mobile (Web Browser) $1.99 [Check it out](https://itunes.apple.com/us/app/icab-mobile-web-browser/id308111628?mt=8&uo=4)"""
def main():
   # content = appex.get_text();
    if not content:
        print('No input text found. Use this script from the share sheet in an app like Bear.')
        return
    re.sub(r'[^\x00-\x7F]+', ' ', content)
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

if __name__ == '__main__':
    main()
