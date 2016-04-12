import re
import sys
from pinyin import convert
from summarize import summarize

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
        print(line)
    trad, simp, pinyin, eng = match.groups()
    pinyin = pinyin.replace('u:', 'v')
    eng = eng.split('/')
    return trad, simp, pinyin, eng

def make_entry(trad, simp, pinyin, eng):
    eng_names = list(map(summarize, eng))
    names = [simp, trad, pinyin] + eng_names
    nice_pinyin = ' '.join(convert(syl) for syl in pinyin.split())
    defn = eng #"\n".join(eng)
    entry = pyglossary.entry.Entry(names, defn)
    return entry

glossary = pyglossary.glossary.Glossary()
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.startswith('#'):
            entry = make_entry(*parse_line(line))
            glossary.addEntryObj(entry)

glossary.write(sys.argv[2], format='Stardict')

