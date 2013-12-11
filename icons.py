import yaml
import math

def getIcons():
    path = 'bower_components/font-awesome/src/icons.yml'
    icons_yml = open(path)
    icons = yaml.load(icons_yml.read())
    icons_yml.close()
    return icons['icons']

def getCategories(icons):
    categories = {}
    for icon in icons:
        for category in icon['categories']:
            if category not in categories:
                categories[category] = []
            categories[category].append(icon['id'])
    return categories

CATEGORY_TPL = """
<h2>%(title)s</h2>
<div class="ui-grid-c ui-responsive">
%(content)s
</div>
"""

COL_TPL = """
<div class="ui-block-%(col)s">
<ul data-role="listview" data-theme="%(col)s">
%(content)s
</ul>
</div>
"""

ICON_TPL = """
<li data-icon="%(id)s"><a href="#">%(id)s</a></li>
"""

if __name__ == '__main__':
    icons = getIcons()
    categories = getCategories(icons)
    html = ""
    for category in categories:
        category_info = {"title": category, "content": ""}
        icons = categories[category]
        category_length = len(icons)
        col_length = int(math.ceil(category_length/4.0))
        for col in ('a', 'b', 'c', 'd'):
            col_content = ""
            if col == 'a':
                start = 0
                end = col_length
            elif col == 'b':
                start = col_length
                end = col_length * 2
            elif col == 'c':
                start = col_length * 2
                end = col_length * 3
            elif col == 'd':
                start = col_length * 3
                end = -1
            for icon in icons[start:end]:
                col_content += ICON_TPL % {"id": icon}
            category_info["content"] += COL_TPL % {"col": col, "content": col_content}

        html += CATEGORY_TPL % category_info

    tpl = open('dist/index_tpl', 'r').read()
    index = open('dist/index.html', 'w')
    html = tpl.replace('ICONS_TO_REPLACE', html)
    index.write(html)
