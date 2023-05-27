import razorpay
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as autho
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Save_code
from .models import Premium
from .models import Doubt
from .models import htmlquestion
from .models import Feedback
from .models import Notes
from .models import Payment
from django.db.models import Q
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

# @login_required(login_url='login')


def home(request):
    return render(request, "index.html")


def signin(request):

    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pswd1')
        password2 = request.POST.get('pswd2')

        if password1 != password2:
            return redirect("signin")
        else:
            if User.objects.filter(username=username).first():
                return render(request, "signin.html", {'msg': 'Already have this password'})
            else:
                my_user = User.objects.create_user(username, email, password2)
                my_user.first_name = firstname
                my_user.last_name = lastname
                my_user.save()

                return redirect('login')

    return render(request, "signin.html")


def login(request):

    if request.method == "POST":
        username = request.POST.get('user')
        pass1 = request.POST.get('pswd')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            autho(request, user)
            return redirect('home')

        else:
            return render(request, "login.html", {'msg': 'Wrong ! Username & Password'})

    return render(request, "login.html")


def forgot_password(request):
    try:
        if request.method == 'POST':
            global username
            username = request.POST.get('user')

            if not User.objects.filter(username=username).first():
                messages.success(request, "Not Found")
                return render(request, "fp.html", {'msg': 'User not found!'})

            user_email = User.objects.filter(
                username=username).values_list('email')

            if user_email:
                user_email_str = ''.join(user_email[0])

            # print("Email : "+user_email_str)

            global token
            token = random.randint(99999, 999999)
            to = str(token)
            # print(type(token))
            # print(token)

            send_mail(
                username,
                'Your OTP : '+to,
                'ytsuruu@gmail.com',
                [user_email_str],
                fail_silently=False,
            )
            return redirect('otp')

    except Exception as e:
        print(e)

    return render(request, "fp.html")


def otp(request):

    try:
        if request.method == 'POST':
            otp = request.POST.get("otp")
            otp_int = int(otp)

            # print(type(otp_int))

            if otp_int == token:
                return redirect('change_password')
            else:
                return render(request, 'otp.html', {'msg_otp': 'Wrong OTP !'})

    except Exception as e:
        print(e)

    return render(request, 'otp.html')


def change_password(request):

    try:
        if request.method == 'POST':
            pass1 = request.POST.get("pass1")
            pass2 = request.POST.get("pass2")

            if pass1 == pass2:
                user = User.objects.get(username=username)
                user.set_password(pass1)
                user.save()
                return redirect('login')
            else:
                msg = "The password doesn't match"
                return render(request, "cp.html", {'msg': msg})

    except Exception as e:
        print(e)

    return render(request, 'cp.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
    

def htmlcontent(request, status):

    try:
        user = request.user
        username = user.username
        
        if status == "intro":
            
            if request.method == 'POST':
                n = request.POST.get("code_lang_ans1")
                
                have = Q(Q(note_user=username))
                status = Notes.objects.filter(have)

                if len(status) > 0:    
                    Notes.objects.filter(have).update(note_1=n)
                    info = Notes.objects.filter(have).values_list("note_1")
                    data = {'note':info[0][0]}
                    return render(request, "htmlcontent.html",data)
                else:
                    save_note = Notes(note_user=username, note_1=n,note_2="",note_3="")
                    save_note.save()
                    info = Notes.objects.filter(have).values_list("note_1")
                    data = {'note':info[0][0]}
                    return render(request, "htmlcontent.html",data)
                
        if status == "overview":
                return render(request, "htmlcontentOverview.html")
        
        if status == "basictags":
            return render(request, "htmlcontentBasicTags.html")
        

    except Exception as e:
        print(e)

    return render(request, "htmlcontent.html")



def doubt(request, status):
    try:

        if status == "home":
            info = Doubt.objects.all()
            loop_count = len(info)
            data = {'doubt': info, 'loop_count': loop_count}
            return render(request, "doubt.html", data)

        if status == "post":
            if request.method == 'POST':
                user = request.user
                username = user.username
                code_lang = request.POST.get("code_lang_ans1")
                code_question = request.POST.get("code_question")
                code_code = request.POST.get("code_code")

                have = Q(Q(doubt_code=code_code) & Q(doubt_q=code_question))
                status = Doubt.objects.filter(have)

                if len(status) > 0:

                    info = Doubt.objects.all()
                    loop_count = len(info)
                    data = {'doubt': info, 'loop_count': loop_count}
                    return render(request, "doubt.html", data)
                else:
                    save_post = Doubt(doubt_user=username, doubt_lang=code_lang,
                                      doubt_q=code_question, doubt_code=code_code)
                    save_post.save()
                    info = Doubt.objects.all()
                    loop_count = len(info)
                    data = {'doubt': info, 'loop_count': loop_count}
                    return render(request, "doubt.html", data)
        else:
            info = Doubt.objects.all()
            loop_count = len(info)
            data = {'doubt': info, 'loop_count': loop_count}
            return render(request, "doubt.html", data)

    except Exception as e:
        print(e)

    info = Doubt.objects.all()
    loop_count = len(info)
    data = {'doubt': info, 'loop_count': loop_count}
    return render(request, "doubt.html", data)


def htmlex(request, num="0"):

    try:

        if (num == "1"):
            ex = 1
            question = 'Add a "tooltip" to the paragraph below with the text "About W3Schools".'
            start_q = "< p  "
            end_q = """ = "About Website"> It's a little baby site ! </p>"""
            ans = "title"

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

        if (num == "2"):
            ex = 2
            question = 'Set the size of the image to 250 pixels wide.'
            start_q = '<img src="w3schools.jpg" width="'
            end_q = '">'
            ans = "250"

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

        if (num == "3"):
            ex = 3
            question = 'Make the element below into a link that goes to "https://www.google.com".'
            start_q = '<a'
            end_q = '"https://www.google.com">This is a link</a>'
            ans = "href="

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

        if (num == "4"):
            ex = 1
            question = 'Use the correct HTML tag to add a heading with the text "London".'

            start_q = ''

            ans = "<h1>London</h1>"

            end_q = ' <p>London is the capital city of England. It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>'

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

        if (num == "5"):
            ex = 2
            question = """Mark up the text with appropriate tags:
                "Universal Studios Presents" is the most important heading."""
            start_q = ''
            end_q = ' Universal Studios Presents </h1>'
            ans = "<h1>"

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

        if (num == "6"):
            ex = 3
            question = 'Mark up the text with appropriate tags:The last sentence is just a paragraph.'
            start_q = '<p> On the Island of Isla Nublar, a new park has been built: Jurassic Park is a theme park of cloned dinosaurs!!'
            end_q = ''
            ans = "</p>"

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

        if (num == "7"):
            ex = 4
            question = 'Mark up the text with appropriate tags:"About" is the third most important heading.'
            start_q = ''
            end_q = ' About </h3>'
            ans = "<h3>"

            data = {

                'ex': ex,
                'question': question,
                'start_q': start_q,
                'end_q': end_q,
                'ans': ans
            }
            return render(request, "htmlex.html", data)

    except Exception as e:
        print(e)

    return render(request, "htmlex.html")


def htmlquestions(request):

    info = htmlquestion.objects.all()
    loop_count = len(info)
    data = {'info': info, 'loop_count': loop_count}

    return render(request, "htmlquestions.html", data)


def email(request):

    print("i am in")
    send_mail(
        'vikash',
        'Your OTP : ',
        'ytsuruu@gmail.com',
        ['jayp272829@gmail.com'],
        fail_silently=False,
    )

    return render(request, "payment.html")


@login_required(login_url='login')
def feedback(request, status):

    try:
        if status == "home":
            info = Feedback.objects.all()
            loop_count = len(info)
            data = {'feed': info, 'loop_count': loop_count}
            return render(request, "feedback.html", data)

        if status == "post":

            if request.method == 'POST':
                user = request.user
                feedback_user = user.username
                feedback_user_email = request.POST.get("email")
                feedback_content = request.POST.get("feedback_text")
                feedback_rate = request.POST.get("rate")
                have = Q(Q(feedback_user=feedback_user) & Q(
                    feedback_user_email=feedback_user_email))
                status = Feedback.objects.filter(have)

                if len(status) > 0:

                    info = Feedback.objects.all()
                    loop_count = len(info)
                    data = {'feed': info, 'loop_count': loop_count,
                            'msg': 'Your feedback has already been received, and we cannot accept multiple submissions from the same user.'}
                    return render(request, "feedback.html", data)
                else:
                    save_post = Feedback(feedback_user_email=feedback_user_email, feedback_rate=feedback_rate,
                                         feedback_content=feedback_content, feedback_user=feedback_user)
                    save_post.save()
                    info = Feedback.objects.all()
                    loop_count = len(info)
                    data = {'feed': info, 'loop_count': loop_count}
                    return render(request, "feedback.html", data)

        info = Feedback.objects.all()
        loop_count = len(info)
        data = {'feed': info, 'loop_count': loop_count}
        return render(request, "feedback.html", data)

    except Exception as e:
        print(e)

    info = Feedback.objects.all()
    loop_count = len(info)
    data = {'feed': info, 'loop_count': loop_count}
    return render(request, "feedback.html", data)


@csrf_exempt
def payment(request, corse):

    try:

        if corse == "java_payment":

            if request.method == 'POST':
                user = request.user
                username = user.username

                amount = Premium.objects.filter(id=1).values_list("premium_amount")
                course = Premium.objects.filter(id=1).values_list("premium_name")
                name = request.POST.get("firstname")
                num = request.POST.get("lastname")
                email = request.POST.get("email")
                who = request.POST.get("username")
                premium_id = Premium.objects.values_list("id")
                
                print(username)

                have = Q(Q(name=name) & Q(email=email))
                status = Payment.objects.filter(have)
                if len(status) > 0:
                    ordernum = Payment.objects.filter(have).values_list("order_id")
                    return render(request, "payment.html", {'course': course[0][0], "name": name, "num": num, "email": email, "ordernum": ordernum[0][0], "amount": amount[0][0]})
                else:
                    ordernum = random.randint(999999999, 9999999999)
                    save_post = Payment(payment_user=who, name=name,enrolled_course=course, enrolled_id=premium_id,mobile_no=num,email=email,order_id=ordernum,amount=amount)
                    save_post.save()
                    return render(request, "payment.html", {'course': course[0][0], "name": name, "num": num, "email": email, "ordernum": ordernum, "amount": amount[0][0]})

                
            
            client = razorpay.Client(
                auth=("rzp_test_GW0H7pJwQSuws9", "HrRIYGssp8pdJ09rAkbfeDOb"))

            payment = client.order.create(
                {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        return redirect("email")

    except Exception as e:
        print(e)

    return render(request, "payment.html")


@login_required(login_url='login')
def premium(request, name):
    try:

        if (name == "java"):
            premium = Premium.objects.filter(id=1).values_list("premium_name")
            premium_amount = Premium.objects.filter(
                id=1).values_list("premium_amount")

            name = premium[0][0]
            amount = premium_amount[0][0]

            return render(request, "premium.html", {'name': name, 'amount': amount, 'done': "java_payment"})

        elif (name == "cpp"):

            premium = Premium.objects.filter(id=2).values_list("premium_name")
            premium_amount = Premium.objects.filter(
                id=2).values_list("premium_amount")

            name = premium[0][0]
            amount = premium_amount[0][0]
            return render(request, "premium.html", {'name': name, 'amount': amount})

        elif (name == "python"):

            premium = Premium.objects.filter(id=3).values_list("premium_name")
            premium_amount = Premium.objects.filter(
                id=3).values_list("premium_amount")

            name = premium[0][0]
            amount = premium_amount[0][0]
            return render(request, "premium.html", {'name': name, 'amount': amount})

        elif (name == "php"):

            premium = Premium.objects.filter(id=4).values_list("premium_name")
            premium_amount = Premium.objects.filter(
                id=4).values_list("premium_amount")

            name = premium[0][0]
            amount = premium_amount[0][0]
            return render(request, "premium.html", {'name': name, 'amount': amount})

        elif (name == "payment"):
            return redirect('payment')

        else:
            return render(request, "index.html")

    except Exception as e:
        print(e)

    return render(request, "index.html")


@login_required(login_url='login')
def filesave(request):

    try:

        if request.method == 'POST':
            user = request.user
            username = user.username
            filename = request.POST.get('filename')

            have = Q(Q(file_name=filename) & Q(file_user=username))
            shave = Save_code.objects.filter(have)

            # print(len(shave))

            if len(shave) > 0:
                return render(request, "save.html", {'msg': '🙅‍♂️ the same file name have'})

            else:
                filecontent = request.POST.get('filecontent')
                filedate = datetime.date.today()
                savecode = Save_code(
                    file_user=username, file_name=filename, file_content=filecontent, file_date=filedate)
                savecode.save()
                return redirect('savecode')

    except Exception as e:
        print(e)

    return render(request, "save.html")


@login_required(login_url='login')
def searchfile(request):

    try:
        if request.method == 'POST':

            user = request.user
            username = user.username

            filename = request.POST.get('sbar')

            fname = Save_code.objects.filter(
                file_user=username).values_list('file_name')

            data = []
            fdate = []
            date = []
            file = []

            for i in range(len(fname)):
                data.append(fname[i][0])

            # search

            s_data = []
            s_fdate = []
            s_date = []

            filelen = len(fname)

            if filename in data:
                file.append(filename)
                fdate.append(Save_code.objects.filter(
                    file_name=filename).values_list('file_date'))
                date.append(str(fdate[0][0][0]))
                filesdata = {'files': file, 'fdate': date, 'len': filelen}
                return render(request, "savecode.html", filesdata)

            else:
                mulifiles = Q(Q(file_name__icontains=filename)
                              & Q(file_user=username))
                da = Save_code.objects.filter(mulifiles)
                s_filelen = len(da)

                if (s_filelen >= 1):

                    for j in range(len(da)):
                        s_data.append(da[j])
                        s_fdate.append(Save_code.objects.filter(
                            file_name=da[j]).values_list('file_date'))
                        s_date.append(str(s_fdate[j][0][0]))

                    S_filesdata = {'files': s_data,
                                   'fdate': s_date, 'len': s_filelen}

                    return render(request, "savecode.html", S_filesdata)

                else:
                    return redirect('savecode')

        return redirect('savecode')

    except Exception as e:
        print(e)

    return render(request, "savecode.html", filesdata)


@login_required(login_url='login')
def savecode(request):

    try:

        user = request.user
        username = user.username

        fname = Save_code.objects.filter(
            file_user=username).values_list('file_name')

        data = []
        fdate = []
        date = []

        # geting filename & date
        for i in range(len(fname)):
            data.append(fname[i][0])
            fdate.append(Save_code.objects.filter(
                file_name=data[i]).values_list('file_date'))
            date.append(str(fdate[i][0][0]))

        filelen = len(fname)
        filesdata = {'files': data, 'fdate': date, 'len': filelen}

        return render(request, "savecode.html", filesdata)

    except Exception as e:
        print(e)


def renamefile(request):

    try:
        if request.method == 'POST':
            user = request.user
            username = user.username

            oldfilename = request.POST.get('oldname')
            newfilename = request.POST.get('renamedfilename')
            disison = request.POST.get('result')

            if disison == "1":
                filename = Q(Q(file_name=oldfilename) & Q(file_user=username))
                Save_code.objects.filter(filename).update(
                    file_name=newfilename)

            if disison == "0":
                filename = Q(Q(file_name=oldfilename) & Q(file_user=username))
                Save_code.objects.filter(filename).delete()

            return redirect('savecode')

    except Exception as e:
        print(e)

    return redirect('savecode')


def openfile(request):

    try:
        if request.method == 'POST':

            user = request.user
            username = user.username
            oldfilename = request.POST.get('oldname')
            result = request.POST.get('status')
            updatedcontent = request.POST.get('data')

            if result == "1":
                filename = Q(Q(file_name=oldfilename) & Q(file_user=username))
                Save_code.objects.filter(filename).update(
                    file_content=updatedcontent)
                return redirect('searchfile')

            else:
                filename = Q(Q(file_name=oldfilename) & Q(file_user=username))
                filedata = Save_code.objects.filter(
                    filename).values_list('file_content')
                return render(request, "openfile.html", {'filename': oldfilename, 'content': filedata[0][0]})

        return render(request, "openfile.html")

    except Exception as e:
        print(e)

    return render(request, "openfile.html")
