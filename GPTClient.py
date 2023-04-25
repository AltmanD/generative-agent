"""
Content: Client wrapper of GPT
Author : Lu Yudong
"""

import os
import openai
from typing import Any, List, Dict, Tuple


class GPTClient:
    def __init__(self, model: str="gpt-3.5-turbo", api_key: str='') -> None:
        self.model = model
        openai.api_key = api_key

    def send_and_recv(self, msg: List[Dict[str, Any]], temp: float=0.6) -> Tuple[List[str], Exception]:
        self.set_proxy()
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=msg,
            temperature=temp,
        )
        self.unset_proxy()
        print(response)
        result = [response.choices[0].message["content"]]
        return result

    def set_proxy(self, port=7890) -> None:
        os.environ["https_proxy"] = "http://127.0.0.1:{}".format(port)
        os.environ["http_proxy"] = "http://127.0.0.1:{}".format(port)

    def unset_proxy(self) -> None:
        os.environ["https_proxy"] = ""
        os.environ["http_proxy"] = ""


if __name__ == '__main__':
    client = GPTClient(model="gpt-3.5-turbo", api_key='')
    result, err = client.send_and_recv(msg=[{"role": "system", "content": "你是一个热心的智能助手。"},
                                            {"role": "user", "content": "你好，你是谁?"}], temp=0.6)
    print(result)