import pandas as pd
import re


def extract_year(url):
    match1 = re.search(pattern1, url)
    match2 = re.search(pattern2, url)
    match3 = re.search(pattern3, url)

    # if (not match1) and (not match2) and (not match3):
    #     print(url, 'hhh')

    if match1:
        year = match1.group('year')

    if match2:
        gd = match2.groupdict()
        if gd['year1'] is not None:
            year = gd['year1']
        elif gd['year2'] is not None:
            year = gd['year2']
        else:
            year = gd['year']

    if match3:
        year = '2022'

    return year


df = pd.read_csv('./resources/source_data/data1.csv')
pattern1 = re.compile(r'\\(?P<year>\d{4})年超声图片\\')
pattern2 = re.compile(r'\\(?P<year>\d{4}|(?P<year1>\d{4})（老系统）|(?P<year2>\d{4})（新系统）)\\')
pattern3 = re.compile(r'2022年6月8日包虫考核.*?\\(?P<id>\d{1,3})\.jpg')
years = []

for url in df.loc[:, 'urls']:
    year = extract_year(url)
    years.append(year)

series = pd.Series(years)
df.insert(len(df.columns), 'year', series)
df.to_csv('./resources/trim_data/add_year.csv', encoding='utf-8-sig', index=False)
