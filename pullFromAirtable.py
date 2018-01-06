import requests, json, pickle

header = 'Bearer key56ZMngq2Tl2IbO' #of type Authorization
def main():
    # response = r.json()
    r = requests.get("https://api.airtable.com/v0/appVAXRMq3z9O8PXy/Work%20Experience",
                     headers={'Authorization': 'Bearer key56ZMngq2Tl2IbO'}, )
# hold = r('records')
        # print(hold[x].get('fields'))
        # title = hold[x].get('fields').get('Title')+'-'+ hold[x].get('fields').get('start') + '.json'
    i = 0
    with open('works.json', 'w') as fd:
        fd.write(r.text)


if __name__ == "__main__":
    main()