import requests, json, airtable
def main():
    stable = airtable.Airtable('appkNJsnNJrb3FmsM', 'Stories', 'key56ZMngq2Tl2IbO')
    stories = stable.get_all()
    itable = airtable.Airtable('appkNJsnNJrb3FmsM', 'Imported%20Table', 'key56ZMngq2Tl2IbO')
    imported = itable.get_all()
    for i in range(0, len(stories)):
        sName = stories[i].get('fields').get('Name')
        iName = imported[i].get('fields').get('Title')
        if str(sName) in str(imported):
            print('Done!')
        else:
            print('need to add')
            # record = {'Name': iName,
            #           'Description': imported[i].get('fields').get('Summary'),
            #           'Pairing': imported[i].get('fields').get('Pairings'),
            #           'Completed': imported[i].get('fields').get('Completed'),
            #           'Link': imported[i].get('fields').get('Link'),
            #           'World': imported[i].get('fields').get('World'),
            #           'Author': imported[i].get('fields').get('Author')}
            # stable.insert(record)

if __name__ == "__main__":
    main()