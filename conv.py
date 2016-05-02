import re
import os
import sys
from pinyin import convert
from summarize import summarize
import jinja2

import logging
log = logging.getLogger('root')
log.addHandler(logging.StreamHandler())

import pyglossary.glossary
import pyglossary.entry

line_reg = re.compile(r'^([^ ]+) ([^ ]+) \[([^\]]+)\] /(.+)/$')
def parse_line(line):
    line = line.strip()
    match = line_reg.match(line)
    if match is None:
        print("bad line:")
        print(line)
    trad, simp, pinyin, eng = match.groups()
    pinyin = pinyin.replace('u:', 'v')
    eng = eng.split('/')
    return trad, simp, pinyin, eng

def make_entry(trad, simp, pinyin, eng):
    eng_names = list(map(summarize, eng))
    names = [simp, trad, pinyin] + eng_names
    article = render_article(trad, simp, pinyin, eng)

    entry = pyglossary.entry.Entry(names, article, defiFormat='h')
    return entry

script_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(script_dir),
    extensions=['jinja2htmlcompress.HTMLCompress'])
COLORS = {'': 'black', '1': 'red', '2': 'orange', '3': 'green', '4': 'blue', '5': 'black'}
def render_article(trad, simp, pinyin, eng):
    pinyin_tones = [convert(syl) for syl in pinyin.split()]
    nice_pinyin = []
    tones = []
    for syllable in pinyin.split():
        nice_syllable, tone = convert(syllable)
        nice_pinyin.append(nice_syllable)
        tones.append(tone)
    args = dict(COLORS=COLORS, trad=trad, simp=simp,
        pinyin=nice_pinyin, tones=tones, defns=eng)

    template = jinja_env.get_template("article.html")
    return template.render(zip=zip, **args)

glossary = pyglossary.glossary.Glossary()
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.startswith('#'):
            entry = make_entry(*parse_line(line))
            glossary.addEntryObj(entry)

glossary.write(sys.argv[2], format='Stardict')

