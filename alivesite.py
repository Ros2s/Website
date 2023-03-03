import requests
from urllib.parse import urlparse


proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }

# 从文件中读取网站列表
with open('websites.txt', 'r') as f:
    websites = f.readlines()
def check_website(websites):
    # 解析URL
    parsed_url = urlparse(websites)

    # 如果协议为空，则默认使用http协议
    if not parsed_url.scheme:
        websites = 'https://' + websites

# 检查每个网站是否存活并将结果写入文件
with open('website_status.txt', 'w') as f:
    for website in websites:
        website = "https://" + website
        try:
            response = requests.get(website.strip(),proxies=proxies,timeout=5)
            if response.status_code == 200:
                f.write(website.strip() + ' is alive\n')
            else:
                f.write(website.strip() + ' returned a status code of ' + str(response.status_code) + '\n')
        except requests.exceptions.RequestException as e:
            f.write(website.strip() + ' is not alive: ' + str(e) + '\n')
        except (HTTPError, URLError) as e:
            f.write(website.strip() + ' is not alive: ' + str(e) + '\n')

# 打印结果
with open('website_status.txt', 'r') as f:
    print(f.read())
