'''main functions'''
from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import feedback_work
from . import facts_work
from . import users_work


def index(request):
    '''index'''
    return render(request, "index.html")


def terms_list(request):
    '''list of terms'''
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def feedback_list(request):
    '''list of feedback'''
    feedback = feedback_work.get_feedback_for_table()
    return render(request, "feedback_list.html", context={"feedback": feedback})


def facts_list(request):
    '''list of facts'''
    facts = facts_work.get_facts_for_table()
    return render(request, "facts_list.html", context={"facts": facts})


def add_feedback(request):
    '''feedback adding'''
    return render(request, "feedback_add.html")


def add_user(request):
    '''user adding'''
    return render(request, "user_add.html")


def send_user(request):
    '''user sending to db'''
    if request.method == "POST":
        cache.clear()
        login = request.POST.get("login")
        password = request.POST.get("password")
        email = request.POST.get("email")
        context = {"user": login}
        if len(login) == 0:
            context["success"] = False
            context["comment"] = "Логин не должен быть не пустым"
        elif len(password) < 8:
            context["success"] = False
            context["comment"] = "Пароль должен содержать не менее 8 символов"
        elif len(email) == 0:
            context["success"] = False
            context["comment"] = "Почта не должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Вы зарегестрированы"
            users_work.write_user(login, password, email)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "user_request.html", context)
    else:
        add_user(request)


def send_feedback(request):
    '''feedback sending to db'''
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        new_feedback = request.POST.get("new_cat", "")
        context = {"user": user_name}
        if len(new_feedback) == 0:
            context["success"] = False
            context["comment"] = "Отзыв должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш отзыв принят"
            feedback_work.write_feedback(new_feedback, user_name, user_email)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "feedback_request.html", context)
    else:
        add_feedback(request)
