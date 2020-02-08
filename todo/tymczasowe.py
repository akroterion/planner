class CategoryCreate(SuccessMessageMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'todo/category_create.html'
    success_message = 'Kategoria"%(name)s"utworzona poprawnie'
    extra_context = {
        'title': "Dodaj nową Kategorię",
    }
# def funkcja(user):
#     return random.choice([True, False])
@permission_required([
    'todo.add_Category',
], raise_exception=True)
def suggestion(request):
    #jeżeli są dane poost toi spróbuj je zwalidować
    if request.method == "POST":
        #skoro dostępne są dane post, to nalezy je wrzucić do formularza:
        form = SuggestionForm(request.POST)
        #sprawdzenie poprawności formularza:
        if form.is_valid():
            #dane poprawne(form.cleaned_data)
            #procesujemy
            # 1. tworzymy Queation i zapisujemy w bazie
            q = Category.objects.create(
                category_text=form.cleaned_data['name'],
               
            )






#   * logowanie, wylogowanie

# * widok kategorii + zadania w kategorii

# * widok projektów + zadania w projekcie

# * widok zadań chronologicznie

# * widok zadań po dacie (zadania dla danej konkretnej daty)

# * CRUD kategorie

# * CRUD projekty

# * CRUD zadania

# Widok zadań wg kategorii
# widok zadań wg projeków
# widok zadań wg listy
# widok zadań w kalendarzu

# formularz dodawania zadań obcych od osób trzecich (logowanie za pomocą jednych danych, w komentarzu opis od kogo)



stary forms:
import datetime
from django.forms import ModelForm
from django import forms
from .models import Category, Project, Task

class CategoryForm(forms.Form):
    name = forms.CharField(label="category", max_length=120)


class ProjectForm(forms.Form):
    title = forms.CharField(label="project", max_length=120)







class TaskForm(forms.Form):
    desc = forms.CharField(label="task", max_length=120)
    due_date = forms.DateTimeField(label="due date",)
{% extends "base.html" %}
{% block content %}
<center>
    <h1>Dodaj kategorię</h1>
    <form method="POST">
        {% csrf_token %}
        {%for field in category_create}
    <tr>
        <th>{{field.label}}</th>
        <td>{{ field }}</td>
    </tr>
    {% endfor %}
        <button type="submit" class="btn btn-lg btn-warning">Submit</button>
    </form>
</center>
{% endblock %}





