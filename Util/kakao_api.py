import requests, json
from pprint import pprint 

class KakaoAPI:
    def __init__(self, kakao_rest_api_key:str):
        self.API_AUTH_KEY = kakao_rest_api_key
        self.auth_headers = {"Authorization": f"KakaoAK {self.API_AUTH_KEY}"}
        self.HOST = "https://dapi.kakao.com"
        self.SEARCH_ADDRESS_URL = "/v2/local/search/address"
        self.SEARCH_KEYWORD_URL = "/v2/local/search/keyword"
        pass

    def get_coordiantion_by_address(self, address:str, headers:dict={}, params:dict={}):
        """
        https://developers.kakao.com/docs/latest/ko/local/dev-guide#address-coord

        ex: "제주도 서귀포시 상예로 319"
        ('126.39471590891', '33.2731855026733')
        """
        headers.update(self.auth_headers.copy())
        params.update({"query": address})
        
        req = requests.get(self.HOST+self.SEARCH_ADDRESS_URL,
                           headers=headers, params=params)
        json_data = json.loads(req.text)
        documents = json_data['documents'][0]
        return documents['x'], documents['y']
    
    
    def get_search_result_by_address(self, address:str, headers:dict={}, params:dict={}):
        """
        https://developers.kakao.com/docs/latest/ko/local/dev-guide#address-coord

        ex: "제주도 서귀포시 상예로 319"
        ('126.39471590891', '33.2731855026733')
        """
        headers.update(self.auth_headers.copy())
        page = 0
        params.update({"query": address, "page": page})
        try:
            while True:
                page += 1
                params.update({"page": page})
                json_data = json.loads(
                    requests.get(self.HOST+self.SEARCH_ADDRESS_URL,
                           headers=headers, params=params).text
                            )
                documents = json_data["documents"]
                for doc in documents:
                    # 내가 찾는 문서면 리턴
                    if doc["address_name"] == address:
                        return doc
                # 못찾았으면 종료
                if json_data["meta"]["is_end"] == True:
                    break
            # 못찾았으면 마지막에 검색된 데이터를 documents에 넣고
            # 비어있으면 None 있으면 검색된 거라도 줌
            documents = json_data["documents"]
            if documents:
                return documents[0]
            return None
        
        except KeyError:
            return {"json_data": json_data, "address":address, "page": page}

    def get_search_result_by_keyword(self, keyword:str, headers:dict={}, params:dict={}):
        """
        https://developers.kakao.com/docs/latest/ko/local/dev-guide#search-by-keyword

        ex: "CGV강남", params={"category_group_code":"CT1"}
        """
        headers.update(self.auth_headers.copy())
        page = 0
        params.update({"query": keyword, "page": page})
        try:
            while True:
                page += 1
                params.update({"page": page})
                json_data = json.loads(
                    requests.get(self.HOST+self.SEARCH_KEYWORD_URL,
                            headers=headers, params=params).text
                            )
                documents = json_data["documents"]
                for doc in documents:
                    if doc['place_name'].replace(" ", "") == keyword.replace(" ", ""):
                        return doc
                if json_data["meta"]["is_end"] == True:
                    break
            documents = json_data["documents"]
            if documents:
                return documents[0]
            return None
        
        except KeyError:
            return {"json_data": json_data, "keyword":keyword, "page": page}