import json, sys
from yattag import Doc

base = 'https://www.fanfiction.net'
name = sys.argv[1]
name = str(name).lower()

def main():
    with open('/Users/Dustin/Documents/Python3/tutorial/'+name+'.json') as f:
        myson = json.load(f)
        print(myson[0].get('title'))
        with open(name +'.html', 'w+', encoding='utf8') as newf:
            newf.write(displayEm(myson))


def displayEm(data):
    doc, tag, text = Doc().tagtext()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis(
                '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">')
            doc.asis(
                '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>')
            doc.asis(
                '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.bundle.min.js" integrity="sha384-VspmFJ2uqRrKr3en+IG0cIq1Cl/v/PHneDw6SQZYgrcr8ZZmZoQ3zhuGfMnSR/F2" crossorigin="anonymous"></script>')
            doc.asis('<link rel="stylesheet" href="styles.css">')
            doc.asis("<link rel='shortcut icon' type='image/x-icon' href='favicon_2010_site.ico' />")
            with tag('title'):
                text(name.title() + ' Fanfiction')
        with tag('body'):
            with tag('h1', klass="myTitle"):
                text(name.title() + ' Fanfiction')
            with tag('div', klass="container-fluid"):
                with tag('div', klass="row"):
                    for i in range(0, len(data)):
                        if i % 4 == 0:
                            with tag('div', klass='w-100'):
                                doc.attr(id="w-100")
                        else:
                            with tag('div', klass="card col-sm", style="width: 45rem;"):
                                with tag('div', klass="card-block"):
                                    with tag('h1'):
                                        text(data[i].get('title'))
                                    with tag('p', klass="complete"):
                                        try:
                                            if 'Complete' in str(data[i].get('info')[2]):
                                                text('Complete')
                                        except IndexError:
                                            text('N/A')
                                    with tag('h5', klass="card-title"):
                                        try:
                                            text(str(data[i].get('info')[2])
                                                 .replace('-', '')
                                                 .replace('Complete', '')
                                                 .replace('[', '')
                                                 .replace(']', ''))
                                        except IndexError:
                                            text('No Information Found')
                                    with tag('p', klass="card-text"):
                                        text(data[i].get('summary')[0])
                                    with tag('a', href=base + data[i].get('link'), target="_blank"):
                                        with tag('button', klass="btn btn-primary space"):
                                            text('Read More!')
                                    with tag('a', href=base + data[i].get('reviews'), target="_blank"):
                                        with tag('button', klass="btn btn-secondary space"):
                                            text('Reviews')
                                    with tag('p'):
                                        text(data[i].get('info')[0])

    return doc.getvalue()


if __name__ == "__main__":
    main()
