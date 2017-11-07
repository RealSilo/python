# With classes
class Report:
    def generate_report(self):
        self.retrieve_data()
        self.format_report()
        self.send_report()

    def retrieve_data(self):
        print('Data retrieved!')

    def format_report(self):
        raise NotImplementedError('Subclasses should implement this!')

    def send_report(self):
        print('Report sent!')


class TextReport(Report):
    def format_report(self):
        print('Text formatting!')


class HTMLReport(Report):
    def format_report(self):
        print('HTML formatting!')


print(TextReport().generate_report())
print(HTMLReport().generate_report())

print('----------------------------')


# With higher order functions:
def text_format():
    print('Text formatting!')


def html_format():
    print('HTML formatting!')


def generate_report(format_report):
    def retrieve_data():
        print('Data retrieved!')

    def send_report():
        print('Report sent!')

    retrieve_data()
    format_report()
    send_report()


print(generate_report(text_format))
print(generate_report(html_format))
