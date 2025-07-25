from django.shortcuts import render, get_object_or_404
from .models import Role, Question, Option

def role_selection(request):
    roles = Role.objects.all()
    return render(request, 'Role/role_selection.html', {'roles': roles})

def start_quiz(request):
    role_id = request.GET.get('role')
    if not role_id:
        roles = Role.objects.all()
        return render(request, 'Role/role_selection.html', {
            'error': 'Please select a role first.',
            'roles': roles,
        })

    role = get_object_or_404(Role, id=role_id)
    questions = Question.objects.filter(role=role).prefetch_related('options')

    return render(request, 'Role/quiz.html', {
        'role': role,
        'questions': questions,
    })

def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        total_questions = 0

        for key in request.POST:
            if key.startswith('q'):
                total_questions += 1
                selected_option_ids = request.POST.getlist(key)
                question_id = key[1:]
                
                correct_option_ids = list(
                    Option.objects.filter(question_id=question_id, is_correct=True).values_list('id', flat=True)
                )

                selected_option_ids_int = list(map(int, selected_option_ids))

                if set(selected_option_ids_int) == set(correct_option_ids):
                    score += 1

        return render(request, 'Role/quiz_result.html', {
            'score': score,
            'total': total_questions,
        })

    roles = Role.objects.all()
    return render(request, 'Role/role_selection.html', {'roles': roles})

# Keep your other views unchanged or update paths accordingly:
def frontend(request):
    return render(request, 'Role/frontend.html')

def backend_view(request):
    return render(request, 'Role/backend.html')

def aptitude_view(request):
    return render(request, 'Role/aptitude.html')

def data_scientist_view(request):
    return render(request, 'Role/data_scientist.html')

def cloud_engineer(request):
    return render(request, 'Role/cloud_engineer.html')
