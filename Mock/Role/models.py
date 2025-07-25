from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Enter the name of the role (e.g., Data Scientist)")

    def __str__(self):
        return self.name

class Question(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(help_text="Enter the quiz question text")

    def __str__(self):
        return self.text[:50]  # Limiting in admin/list display for readability

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200, help_text="Enter the option text")
    is_correct = models.BooleanField(default=False, help_text="Mark true if this is a correct answer")

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"
