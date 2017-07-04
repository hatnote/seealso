# -*- coding: utf-8 -*-

import codecs
import argparse
import time
from datetime import datetime
from email.Utils import formatdate

import yaml
import ashes
from boltons.timeutils import UTC, isoparse

DEFAULT_PAGE_NAME = './static/index.htm'
DEFAULT_RSS_NAME = './static/feed.rss'
DEFAULT_YAML = 'content.yaml'
DEFAULT_PAGE_TMPL = 'index.dust'
DEFAULT_RSS_TMPL = 'rss.dust'


def to_rss_timestamp(dt_obj, to_utc=False):
    if to_utc and dt_obj.tzinfo:
        dt_obj = dt_obj.astimezone(UTC)
    return formatdate(time.mktime(dt_obj.timetuple()))


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
            if not doc.get('date_added'):
                import pdb; pdb.set_trace()
            doc['pub_date'] = to_rss_timestamp(doc['date_added'])
            ret['visualizations'].append(doc)
    return ret


def main(content_name, page_name, rss_name):
    with codecs.open(content_name, 'r') as file:
        contents = file.read()
    from_yaml = yaml.load_all(contents)
    page_dict = parse_page_contents(from_yaml)
    page_dict['cur_utc'] = to_rss_timestamp(datetime.now())
    ashes_env = ashes.AshesEnv(['./templates'], keep_whitespace=True)
    rendered_page = ashes_env.render(DEFAULT_PAGE_TMPL, page_dict)
    with codecs.open(page_name, 'w', 'utf-8') as outfile:
        outfile.write(rendered_page)
    rendered_rss = ashes_env.render(DEFAULT_RSS_TMPL, page_dict)
    with codecs.open(rss_name, 'w', 'utf-8') as outfile:
        outfile.write(rendered_rss)
    print 'successfully generated %s, %s' % (page_name, rss_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--content', help='input YAML file with content',
                         default=DEFAULT_YAML)
    parser.add_argument('--page', help='output HTML file name',
                         default=DEFAULT_PAGE_NAME)
    parser.add_argument('--rss', help='output RSS file name',
                         default=DEFAULT_RSS_NAME)
    args = parser.parse_args()
    main(args.content, args.page, args.rss)
