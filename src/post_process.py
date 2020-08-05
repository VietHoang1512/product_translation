import re

def post_process(text):
    text = text.lower()    
    
    text = re.sub('\[', '【 ', text)
    text = re.sub('\]', ' 】', text)
    # text = re.sub('\[', '【', text)
    # text = re.sub('【', '【 ', text)
    # text = re.sub('\]', '】', text)
    # text = re.sub('】', ' 】', text)
    pattern = re.compile("【(.+\-)")
    matches = re.findall("【.+\-.+】",text)
    # for pattern in matches:
    #     new_pattern = old.replace("【", "【 ").replace("】", " 】")
    #     text = text.replace(pattern, new_pattern)
    #     print(text)
    text = re.sub('＊', '*', text)
    text = re.sub('\*', ' * ', text)
    text = text.replace('-', ' - ')
    text = text.replace('~', ' ~ ')
    text = text.replace('/', ' / ')
    text = text.replace('’', ' ’ ')
    text = text.replace('&', ' & ')
    text = text.replace('#', ' # ')
    text = text.replace('_', ' _ ')
    text = text.replace("men's", "men")
    text = text.replace(" pc", "pcs")
    # text = text.replace(" ml", "ml")    # lower
    
    # text = text.replace("women", "female")    # lower
    # text = re.sub(r'\d+ (g)', 'g', text)
    text = re.sub('\s+', ' ', text)
    # text = re.sub('\(', '( ', text)    # lower
    # text = re.sub('\)', ' )', text)
    return text