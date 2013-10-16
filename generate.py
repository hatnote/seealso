import argparse
import codecs
import yaml
import ashes

DEFAULT_OUTPUT_NAME = 'static/index.htm'
DEFAULT_YAML = 'content.yaml'
DEFAULT_TEMPALTE_NAME = 'index.dust'

def parse_page_contents(docs):
    ret = {'sections': [],
           'visualizations': []}
    for doc in docs:
        if not doc:
            continue
        if doc.get('page_title'):
            ret['page_title'] = doc['page_title']
            ret['page_subtitle'] = doc['page_subtitle']
            continue
        if doc.get('section_title'):
            ret['sections'].append(doc)
            continue
        if doc.get('title'):
            ret['visualizations'].append(doc)
    return ret

def main(content_name, output_name):
    with codecs.open(content_name, 'r') as file:
        contents = file.read()
    from_yaml = yaml.load_all(contents)
    page_dict = parse_page_contents(from_yaml)
    ashes_env = ashes.AshesEnv(['./templates'], keep_whitespace=True)
    rendered = ashes_env.render('index.dust', page_dict)
    with codecs.open(output_name, 'w', 'utf-8') as file:
        file.write(rendered)
    print 'successfully generated %s' % output_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--content', help='input YAML file with content',
                         default=DEFAULT_YAML)
    parser.add_argument('--output', help='output HTML file',
                         default=DEFAULT_OUTPUT_NAME)
    args = parser.parse_args()
    main(args.content, args.output)