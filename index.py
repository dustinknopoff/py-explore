from yattag import Doc
import json, subprocess

base = 'https://www.fanfiction.net'
list = ['artemis', 'daphne', 'diana', 'favorites', 'fleur', 'morgana', 'rias']
base2 = '/Users/Dustin/Documents/Python3/tutorial/'
out = '/Users/Dustin/Documents/Python3/out/'
files = []
with open(base2 + 'artemisu.json') as f1:
    artemis = json.load(f1)
with open(base2 + 'daphneu.json') as f2:
    daphne = json.load(f2)
with open(base2 + 'dianau.json') as f3:
    diana = json.load(f3)
with open(base2 + 'favorites.json') as f4:
    favorites = json.load(f4)
with open(base2 + 'fleuru.json') as f5:
    fleur = json.load(f5)
with open(base2 + 'morganau.json') as f6:
    morgana = json.load(f6)
with open(base2 + 'riasu.json') as f7:
    rias = json.load(f7)


def main():
    subprocess.call('bash updates.sh', shell=True)
    with open('index.html', 'w+', encoding='utf8') as f:
        f.write(content(list))


def content(info):
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
            doc.asis('<link rel="stylesheet" href="index.css">')
            doc.asis("<link rel='shortcut icon' type='image/x-icon' href='/Users/Dustin/Documents/Python3/out/favicon_2010_site.ico' />")
            doc.asis('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>')
            doc.asis('<script src="index.js"></script>')
            with tag('title'):
                text('My Fanfiction')
        with tag('body'):
            with tag('div', klass="container-fluid"):
                with tag('div', klass="row justify-content-md-center align-content-center opt"):
                    with tag('h1', klass="title"):
                        text('My Fanfiction')
                    with tag('ul', klass='options'):
                        for opt in info:
                            with tag('li', klass="option-item"):
                                with tag('button', klass="link-button", id=opt):
                                    text(opt.title())
            with tag('div', klass="row justify-content-md-center"):
                with tag('h1', klass="each-title"):
                    text('New Updates')
                with tag('div', klass="my-row", id="artemis", style="overflow:scroll;"):
                    doc.asis(sections(artemis, 'artemis'))
                with tag('div', klass="my-row", id="daphne", style="overflow:scroll;"):
                    doc.asis(sections(daphne, 'daphne'))
                with tag('div', klass="my-row", id="diana", style="overflow:scroll;"):
                    doc.asis(sections(diana, 'diana'))
                with tag('div', klass="my-row", id="favorites", style="overflow:scroll;"):
                    doc.asis(sections(favorites, 'favorites'))
                with tag('div', klass="my-row", id="fleur", style="overflow:scroll;"):
                    doc.asis(sections(fleur, 'fleur'))
                with tag('div', klass="my-row", id="morgana", style="overflow:scroll;"):
                    doc.asis(sections(morgana, 'morgana'))
                with tag('div', klass="my-row", id="rias", style="overflow:scroll;"):
                    doc.asis(sections(rias, 'rias'))

    return doc.getvalue()


def sections(list1, name):
    doc, tag, text = Doc().tagtext()
    for i in range(0, 10):
        try:
            with tag('div', klass="each"):
                with tag('div', klass="card-block"):
                    with tag('h1', klass="new"):
                        text(list1[i].get('title'))
                    with tag('h5'):
                        try:
                            text(str(list1[i].get('info')[2])
                                 .replace('-', '')
                                 .replace('Complete', '')
                                 .replace('[', '')
                                 .replace(']', ''))
                        except IndexError:
                            text('No Information Found')
                    with tag('p', klass="summ"):
                        text(list1[i].get('summary')[0])
                    with tag('a', href=base + list1[i].get('link'), target="_blank"):
                        with tag('button', klass="btn btn-primary space"):
                            text('Read More!')
                    with tag('a', href=base + list1[i].get('reviews'), target="_blank"):
                        with tag('button', klass="btn btn-secondary space"):
                            text('Reviews')
                    with tag('p'):
                        text(list1[i].get('info')[0])
        except IndexError:
            with tag('a', klass="More Updates",
                     href="https://www.fanfiction.net/"):
                text('Find More!')
    with tag('a', href='/Users/Dustin/Documents/Python3/out/' + name + '.html', target="_blank", klass="align-self-center"):
        with tag('button', klass="btn btn-success", style="height: 40px;", ):
            text('Get more ' + name.title() + ' by Favorites!')
    return doc.getvalue()


if __name__ == "__main__":
    main()
