from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect
from .models import Student
from .forms import StudentForm
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