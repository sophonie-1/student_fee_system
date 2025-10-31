from django.db import models
from django.core.validators import MinValueValidator

class FeeStructure(models.Model):
    program = models.CharField(max_length=100)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    total_fee = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ['program', 'year']  # No duplicate program/year combos

    def __str__(self):
        return f"{self.program} - Year {self.year}"

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)  # e.g., S001
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    year_of_study = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    def get_total_fee(self):
        fee = FeeStructure.objects.filter(program=self.program, year=self.year_of_study).first()
        return fee.total_fee if fee else 0

    def get_total_paid(self):
        from django.db.models import Sum
        total = self.payment_set.aggregate(total=Sum('amount'))['total']
        return total or 0

    def get_balance(self):
        return max(0, self.get_total_fee() - self.get_total_paid())

    def get_status(self):
        return "Cleared" if self.get_balance() == 0 else "Not Cleared"

class Payment(models.Model):
    payment_id = models.CharField(max_length=10, unique=True, primary_key=True)  # e.g., P001
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    date = models.DateField(auto_now_add=True)  # Auto-set to today

    def save(self, *args, **kwargs):
        # Validate: Total paid <= total fee
        total_paid = self.student.get_total_paid() + self.amount  # Includes this payment
        if total_paid > self.student.get_total_fee():
            raise ValueError("Total payments exceed required fee.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment {self.payment_id} for {self.student.name}"