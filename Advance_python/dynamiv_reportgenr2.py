#Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to customize and format reports.
# The system should allow users to define report templates and apply various formatting options dynamically.

from datetime import datetime

# -------------------- Decorators --------------------
def add_border(func):
    """Decorator to add a border around the report"""
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        border = "=" * 50
        return f"{border}\n{content}\n{border}"
    return wrapper


def add_timestamp(func):
    """Decorator to add generation timestamp"""
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return f"Generated on: {datetime.now()}\n{content}"
    return wrapper


# -------------------- Report Class --------------------
class Report:
    def __init__(self, title, content, style="plain"):
        self.title = title
        self.content = content
        self.style = style

    # -------- Magic Methods --------
    def __str__(self):
        """Custom string representation"""
        return self.generate()

    def __len__(self):
        """Return number of lines in content"""
        return len(self.content.splitlines())

    def __add__(self, other):
        """Combine two reports"""
        new_title = f"{self.title} + {other.title}"
        new_content = self.content + "\n" + other.content
        return Report(new_title, new_content, self.style)

    # -------- Class Methods --------
    @classmethod
    def sales_template(cls, sales_data):
        content = "\n".join([f"Product: {p} | Sales: {s}"
                             for p, s in sales_data.items()])
        return cls("Sales Report", content, style="formal")

    @classmethod
    def student_template(cls, student_name, marks):
        avg = sum(marks) / len(marks)
        content = (
            f"Student: {student_name}\n"
            f"Marks: {marks}\n"
            f"Average: {avg:.2f}"
        )
        return cls("Student Report", content, style="academic")

    # -------- Report Generation --------
    @add_border
    @add_timestamp
    def generate(self):
        if self.style == "formal":
            formatted = self.content.upper()
        elif self.style == "academic":
            formatted = self.content.title()
        else:
            formatted = self.content

        return f"REPORT: {self.title}\n\n{formatted}"


# -------------------- Example Usage --------------------

# Create reports using class methods
sales_report = Report.sales_template({
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25
})

student_report = Report.student_template(
    "Shreyaa", [85, 90, 78, 88]
)

# Print reports (__str__)
print(sales_report)
print()
print(student_report)

# Combine reports using __add__
combined_report = sales_report + student_report

print("\nCOMBINED REPORT\n")
print(combined_report)

# Use __len__
print(f"\nStudent report contains {len(student_report)} lines.")