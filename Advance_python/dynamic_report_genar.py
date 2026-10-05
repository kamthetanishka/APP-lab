#Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to customize and format reports.
# The system should allow users to define report templates and apply various formatting options dynamically.
def report_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Generating Report...")
        return func(*args, **kwargs)
    return wrapper

@report_decorator
class ReportGenerator:
    def __init__(self,title, data):
        self.title = title
        self.data = data
    def __str__(self):
        return f"Report Title: {self.title}\nData: {self.data}"
    def format_report(self, format_type):
        if format_type == "plain":
            return str(self)
        elif format_type == "json":
            import json
            return json.dumps({"title": self.title, "data": self.data})
        elif format_type == "csv":
            import csv
            from io import StringIO
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(["Title", "Data"])
            writer.writerow([self.title, self.data])
            return output.getvalue()
        else:
            return "Unsupported format type."

r1 = ReportGenerator("Sales Report", {"Q1": 1000, "Q2": 1500, "Q3": 2000, "Q4": 2500})
print(r1.format_report("plain"))

r2 = ReportGenerator("Inventory Report", {"Item1": 50, "Item2": 30, "Item3": 20})
print(r2.format_report("json"))                