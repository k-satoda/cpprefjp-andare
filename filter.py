#!/usr/bin/env python
# coding: utf-8

# Usage: filter.py BASE_URL PATH
#
#   ソースを標準入力から読み取り、変換結果を標準出力に出します。
#
#   BASE_URL, PATH はリンクの変換に使用されますが、ファイルの出入力には
#   一切使用されません。

import sys
import markdown

# github_to_html/models.py からコピペしてきたもの。
# TODO: 実コードと統合
def _md_to_html(md_data, base_url, path):
    paths = path.split('/')
    qualified_fenced_code = 'github_to_html.qualified_fenced_code'
    html_attribute = 'github_to_html.html_attribute(base_url={base_url}, base_path={base_path}, full_path={full_path})'.format(
        base_url=base_url,
        base_path='/'.join(paths[:-1]),
        full_path='/'.join(paths),
    )
    footer = 'github_to_html.footer(url={url})'.format(
        url='https://github.com/cpprefjp/site/edit/master/{paths}'.format(
            paths='/'.join(paths),
        )
    )

    md = markdown.Markdown([
        'tables',
        qualified_fenced_code,
        'codehilite(noclasses=True)',
        html_attribute,
        footer])
    return md.convert(unicode(md_data, encoding='utf-8'))

if __name__ == '__main__':
    sys.stdout.write(
      _md_to_html(sys.stdin.read(), sys.argv[1], sys.argv[2]).encode('utf-8'))
