# with classes
class Report:
    def __init__(self, formatter):
        self.formatter = formatter

    def generate_report(self):
        self.retrieve_data()
        self.formatter.format_report()
        self.send_report()

    def retrieve_data(self):
        print('Data retrieved!')

    def send_report(self):
        print('Report sent!')


class TextFormatter:
    def format_report(self):
        print('HTML formatting!')


class HtmlFormatter:
    def format_report(self):
        print('Text formatting!')


# Report(TextFormatter()).generate_report()
# Report(HTMLFormatter()).generate_report()

# Also see higher-order function soultuin in the
# template_method.py

if __name__ == '__main__':
    print(Report(TextFormatter()).generate_report())
    print(Report(HtmlFormatter()).generate_report())
