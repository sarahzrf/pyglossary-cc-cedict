# coding=utf-8
# based on https://github.com/zkoch/CEDICT_Parser

TONES = { "a1":"ā", "a2":"á", "a3":"ǎ", "a4":"à",
          "e1":"ē", "e2":"é", "e3":"ě", "e4":"è",
          "i1":"ī", "i2":"í", "i3":"ǐ", "i4":"ì",
          "o1":"ō", "o2":"ó", "o3":"ǒ", "o4":"ò",
          "u1":"ū", "u2":"ú", "u3":"ǔ", "u4":"ù",
          "v1":"ǖ", "v2":"ǘ", "v3":"ǚ", "v4":"ǜ" }
          # using v for the umlauded u

def convert(word):
    tone = word[-1]
    pinyin = word[0:-1].lower()
    result = pinyin

    if tone == "5":
        return pinyin
    elif tone not in "1234":
        return word

    for vowel in "a e ou io iu ui uo i o v u".split():
        if pinyin.find(vowel) > -1:
            vowel1 = vowel[-1]
            result = pinyin.replace(vowel1, TONES[vowel1+tone])
            break

    return result

