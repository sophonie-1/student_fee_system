from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.shortcuts import redirect
from .models import Student, Payment
from .forms import StudentForm, PaymentForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'management/student_list.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()  # Empty form for GET requests
        return context

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        # Invalid form: Manually set object_list and build context
        self.object_list = self.get_queryset()
        context = super().get_context_data(object_list=self.object_list, **kwargs)
        context['form'] = form  # Include invalid form with errors
        return self.render_to_response(context)

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'management/student_edit.html'
    pk_url_kwarg = 'student_id'  # Use 'student_id' in URL instead of default 'pk'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'management/student_delete.html'
    pk_url_kwarg = 'student_id'  # Use 'student_id' in URL
    success_url = reverse_lazy('student_list')

from .models import Student, FeeStructure  # Add FeeStructure here
from .forms import StudentForm, FeeStructureForm  # Add FeeStructureForm here

# ... existing views ...

class FeeStructureListView(LoginRequiredMixin, ListView):
    model = FeeStructure
    template_name = 'management/fee_structure_list.html'
    context_object_name = 'fees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FeeStructureForm()  # Empty form for GET
        return context

    def post(self, request, *args, **kwargs):
        form = FeeStructureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_structure_list')
        # Invalid: Manually set queryset and build context
        self.object_list = self.get_queryset()
        context = super().get_context_data(object_list=self.object_list, **kwargs)
        context['form'] = form  # Include invalid form with errors
        return self.render_to_response(context)

class FeeStructureUpdateView(LoginRequiredMixin, UpdateView):
    model = FeeStructure
    form_class = FeeStructureForm
    template_name = 'management/fee_update.html'
    success_url = reverse_lazy('fee_structure_list')


class PaymentRecordView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'management/payment_record.html'
    context_object_name = 'payments'
    ordering = ['-date']  # Newest first

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PaymentForm()  # Empty form for GET
        return context

    def post(self, request, *args, **kwargs):
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)  # Don't save yet
            # Generate payment_id: P + sequential (e.g., P001)
            last_id = Payment.objects.order_by('-payment_id').first()
            if last_id:
                num = int(last_id.payment_id[1:]) + 1
                payment.payment_id = f"P{num:03d}"
            else:
                payment.payment_id = "P001"
            payment.save()  # Now save with validation
            return redirect('payment_record')
        # Invalid: Manually set queryset and build context
        self.object_list = self.get_queryset()
        context = super().get_context_data(object_list=self.object_list, **kwargs)
        context['form'] = form  # Include invalid form with errors
        return self.render_to_response(context)