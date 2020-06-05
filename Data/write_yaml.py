import yaml

data = {'search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_003': {'expect': [4, 5, 6], 'value': 456}
}}

# 将data写入到当前目录下ww.yaml文件中
with open("./ww.yaml", "a", encoding='utf-8')as f:
    # 写yaml数据
    yaml.safe_dump(data, f, encoding='utf-8', allow_unicode=True)
