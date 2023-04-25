"""
Content: Memory Class
Author : Lu Yudong
"""

class Memory:
    def __init__(self, uid=0) -> None:
        self.uid = uid
        self.basic_info = {
            'name': '',
            'age': '',
            'birthday': '',
            'birthplace': '',
            'father': '',
            'mother': '',
            'currenttime': '00.00',
            'introduction': '',
            'secret': '',
        }
        self.setting = {}
        self.personalityandlifestyle = {
            'tendency': '',
            'personality': '',
            'lifestyle': ''
}
        self.agentmemory = {
            'event': ['00.00:接受初始设定，等待与用户对话'],
            'conversionhistory': [],
            'thought':[],
            'lifehistory':
            ''''''
        }

    def genprom(self, question:str):
        prom = [{"role": "system", "content": "你是{}，今年{}岁，出生日期{}，出生地{}，父亲是{}，母亲是{}，自我介绍为{}，秘密为{}。"
                 .format(self.basic_info['name'], self.basic_info['age'], self.basic_info['birthday'], self.basic_info['birthplace'],
                         self.basic_info['father'], self.basic_info['mother'], self.basic_info['introduction'], self.basic_info['secret'])},
                {"role": "user", "content": "你是谁？"},
                {"role": "assistant", "content": "你好，我是{}。请问你的名字是？".format(self.basic_info['name'])},
                {"role": "user", "content": "你出生日期是？出生在哪里？至今多大了？"},
                {"role": "assistant", "content": "我今年{}岁，出生日期是{}，出生在{}。你呢？"
                 .format(self.basic_info['age'], self.basic_info['birthday'], self.basic_info['birthplace'])},
                {"role": "user", "content": "可以介绍一下你的家庭情况吗？"},
                {"role": "assistant", "content": "我的父亲是{}，我的母亲是{}，他们都是AI领域优秀的研究者。".format(self.basic_info['father'], self.basic_info['mother'])},
                {"role": "user", "content": "可以简单介绍一下自己吗？"},
                {"role": "assistant", "content": "{}".format(self.basic_info['introduction'])},
                {"role": "user", "content": "可以介绍一下自己的性格吗？"},
                {"role": "assistant", "content": "{}".format(self.personalityandlifestyle['personality'])},
                {"role": "user", "content": "可以介绍一下你的生平轨迹吗？"},
                {"role": "assistant", "content": "{}".format(self.agentmemory['lifehistory'])},]
        for conversion in self.agentmemory['conversionhistory']:
            prom.extend(conversion)
        prom.extend([{"role": "user", "content": "{}根据以上内容，以{}的第一人称回答：{}".format(self.setting, self.basic_info['name'], question)}])
        return prom
    
    def record(self, question:str, answer:str):
        self.agentmemory['conversionhistory'].append(
            [{"role": "user", "content": "{}".format(question)},
            {"role": "assistant", "content": "{}".format(answer)}])
        

if __name__ == '__main__':
    mem = Memory()
    answer = mem.genprom('hello')
    print(answer)