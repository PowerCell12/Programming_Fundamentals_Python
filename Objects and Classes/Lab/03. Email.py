class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list1 = []

while True:
    info = input()

    if info == "Stop":
        break

    info = info.split(" ")

    list1.append(info)


lines = list(map(int, input().split(", ")))

for i in range(len(list1)):
    if i in lines:
        is_sent = True
    else:
        is_sent = False

    final = Email(list1[i][0], list1[i][1], list1[i][2], is_sent)   
    print(final.get_info())
