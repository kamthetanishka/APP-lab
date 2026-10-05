# Decorator
def add_stars(func):
    def wrapper(*args, **kwargs):
        return "***** REPORT *****\n" + func(*args, **kwargs) + "\n******************"
    return wrapper


class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method
    @classmethod
    def student_report(cls, name, marks):
        return cls("Student Report", f"Name: {name}\nMarks: {marks}")

    # Magic method
    def __str__(self):
        return self.show()

    # Decorated method
    @add_stars
    def show(self):
        return f"{self.title}\n{self.content}"


# Create report using class method
r = Report.student_report("Shreyaa", 92)

# Print report (__str__ is called automatically)
print(r)