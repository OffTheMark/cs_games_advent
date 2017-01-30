import wikipedia
from challenge1.netcat import Netcat


if __name__ == "__main__":
    n = Netcat("workshop.dciets.com", 8111)
    while True:
        message = str(n.read())
        if not message:
            break
        print(message)
        parts = message.split(" ")
        name = " ".join(parts[6:-1])
        print(name)
        page = wikipedia.page(name)
        print(page.summary)
