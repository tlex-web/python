N = int(input())


# create a subclass and override the handler methods
class MyHTMLParser:
    def feed(self, html: str):
        for line in html.splitlines():
            self.feed(line)

    def handle_starttag(self, tag):
        print("Start : ", tag)

    def handle_endtag(self, tag):
        print("End :", tag)

    def handle_startendtag(self, tag):
        print("Empty :", tag)

    def handle_attributes(self, attrs):
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for _ in range(1, N):
    parser.feed(input())
