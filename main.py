import jinja2
import json
import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()

def create_file(vars=None, html='index'):
    folder = ''
    if '\\' in html:
        page = html[html.rfind('\\')+len('\\'):]
        folder = html[:html.rfind('\\')]
        folder = f'/{folder}'

        #check if folder exists else create it
        sub_folder = f'./build{folder}'
        check_folder = os.path.isdir(sub_folder)

        if not check_folder:
            os.makedirs(sub_folder)
    else:
        page = html

    build = f'./build{folder}/{page}.html'

    # build html from template
    content = jinja2.Environment(
            loader=jinja2.FileSystemLoader(f'./templates{folder}')
            ).get_template(f'{page}.html').render(vars=vars)
    # save built html to file
    with open(build, 'w') as f: f.write(content)


#check if build folder exists else create it
sub_folder = f'./build'
check_folder = os.path.isdir(sub_folder)

if not check_folder:
    os.makedirs(sub_folder)

templates = []
# r=root, d=directories, f = files
for r, d, f in os.walk(os.path.join('.','templates')):
    for file in f:
        if file.endswith('.html'):
            templates.append(os.path.join(r, file))

for template in templates:
    # get json file
    start = 'templates\\'
    end = '.html'
    page = template[template.find(start)+len(start):template.rfind(end)]
    with open(f'json/{page}.json') as f:
        data = json.load(f)
    create_file(data, page)