import airtable_api
import tistory_api
import requests
import os

def main():
    # airtable에서 레코드 가져오기
    records = airtable_api.get_records()

    # 가져온 레코드를 이용하여 Tistory에 블로그 글 등록
    for record in records:
        fields = record.get('fields')
        if fields:
            title = fields.get('Title')
            body = fields.get('Content')
            tag = fields.get('Tags')
            image_url = fields.get('Main Image URL')
            # Main Image 필드에서 첫 번째 이미지의 url 가져오기
            if title and body and tag:
                # Tistory에 블로그 글 등록
                tistory_api.post_write(title, body, tag, image_url)


if __name__ == '__main__':
    main()
