import requests

client_id = 'App ID'
client_secret = 'Secret Key'
access_token = 'access token'
redirect_uri = '블로그 주소'
blogName = '블로그 이름 (https://XXX.tistory.com 에서 XXX의 값)'
# tag = 'Developer, Coding'  # 등록할 태그값, 쉼표로 구분
output = 'json'  # 고정값
grant_type = 'authorization_code'  # 고정값
visibility = 0  # 0은 비공개, 3은 공개 발행
category = 1045233


def get_token(code):
    url = 'https://www.tistory.com/oauth/access_token?'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code,
        'grant_type': grant_type
    }
    r = requests.get(url, data)
    return r.text


def get_category():
    url = 'https://www.tistory.com/apis/category/list?'
    data = {
        'access_token': access_token,
        'output': output,
        'blogName': blogName,
    }
    r = requests.get(url, data)
    return r.text


def post_write(title, content, tag, image_url=None):
    # Tistory API로 블로그 글 등록
    url = 'https://www.tistory.com/apis/post/write?'
    data = {
        'access_token': access_token,
        'output': output,
        'blogName': blogName,
        'title': title,
        'content': content,
        'visibility': visibility,
        'category': category,
        'tag': tag,
    }

    r = requests.post(url, data=data)
    return r.text
