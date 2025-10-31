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

# class Student(models.Model):
#     student_id = models.CharField(max_length=10, unique=True, primary_key=True)  # e.g., S001
#     name = models.CharField(max_length=100)
#     program = models.CharField(max_length=100)
#     campus = models.CharField(max_length=50)
#     year_of_study = models.PositiveIntegerField(validators=[MinValueValidator(1)])

#     def __str__(self):
#         return self.name

#     def get_total_fee(self):
#         fee = FeeStructure.objects.filter(program=self.program, year=self.year_of_study).first()
#         return fee.total_fee if fee else 0

#     def get_total_paid(self):
#         from django.db.models import Sum
#         total = self.payment_set.aggregate(total=Sum('amount'))['total']
#         return total or 0

#     def get_balance(self):
#         return max(0, self.get_total_fee() - self.get_total_paid())

#     def get_status(self):
#         return "Cleared" if self.get_balance() == 0 else "Not Cleared"

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)  # e.g., S001
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    year_of_study = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    # ... existing fields unchanged ...

    def __str__(self):
        return self.name

    def get_total_fee(self):
        fee = FeeStructure.objects.filter(program=self.program, year=self.year_of_study).first()
        if not fee:
            print(f"DEBUG: No fee for {self.name} (program: {self.program}, year: {self.year_of_study})")  # Temp debug
            return 0
        print(f"DEBUG: Fee for {self.name}: {fee.total_fee}")  # Temp
        return fee.total_fee

    def get_total_paid(self):
        from django.db.models import Sum
        total = self.payment_set.aggregate(total=Sum('amount'))['total']
        paid = total or 0
        print(f"DEBUG: Paid for {self.name}: {paid}")  # Temp
        return paid

    def get_balance(self):
        fee = self.get_total_fee()
        paid = self.get_total_paid()
        balance = max(0, fee - paid)
        print(f"DEBUG: Balance for {self.name}: {balance}")  # Temp
        return balance

    def get_status(self):
        fee = self.get_total_fee()
        if fee == 0:
            return "Fee Not Defined"  # Clear edge case
        balance = self.get_balance()
        status = "Cleared" if balance == 0 else "Not Cleared"
        print(f"DEBUG: Status for {self.name}: {status}")  # Temp
        return status
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