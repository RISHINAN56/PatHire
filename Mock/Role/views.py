from django.shortcuts import render
def start_quiz(request):
    return render(request, 'quiz.html')

def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        answers = {
            'q1': '32',
            'q2': '24',
            'q3': '12s',
            'q4': '9',
            'q5': 'Thursday',
        }
        for key in answers:
            user_answer = request.POST.get(key)
            if user_answer == answers[key]:
                score += 1

        return render(request, 'Role/quiz_result.html', {
            'score': score,
            'total': len(answers)
        })

    return render(request, 'quiz.html')



def role_selection(request):
    return render(request, 'Role/role_selection.html')

def frontend(request):
    return render(request, 'Role/frontend.html')
def backend_view(request):
    return render(request, 'Role/backend.html')

def aptitude_view(request):
    return render(request, 'Role/aptitude.html')

def data_scientist_view(request):
    return render(request, 'Role/data_scientist.html')

def cloud_engineer(request):
    return render(request, 'cloud_engineer.html')





# Create your views here.
