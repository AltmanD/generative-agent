from Memory import Memory
from GPTClient import GPTClient

class Player:
    def __init__(self) -> None:
        self.memory = Memory()
        self.gpt = GPTClient()

    def query(self, question:str):
        prom = self.memory.genprom(question)
        answer = self.gpt.send_and_recv(prom)
        self.memory.record(question, answer)
        return answer

if __name__ == '__main__':
    agent = Player()
    while True:
        que = input()
        answer = agent.query('{}'.format(que))
        print(answer)