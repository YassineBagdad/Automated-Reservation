from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .forms import NewUserForm, SettingsForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm

from main.forms import SignUpForm

from main.selenium_folder import mainOfSelenium

#sys.path.insert(1, '/path/to/application/app/folder')
#from main.selenium_folder import function1

#sys.path.append('/path/to/application/app/folder')


from .models import ToDoList,Item
#from .forms import CreateNewList
# Create your views here.


def request_page(response):
    #if(request.GET.get('mybtn')):
    #function1.allFunctions()
    mainOfSelenium.main()
    return render(response,'main/home.html')

def home(response):
    #current_user = request.user
    return render(response,"main/home.html", {})

def settings(request):
    #current_user = request.user
    #return render(response,"main/settings.html", {})
    # if response.method == "POST":
    #     form = SettingsForm(response.POST)

    #     if form.is_valid():
    #         n = form.cleaned_data["name"]
    #         t = ToDoList(name=n)
    #         t.save()

    #     return HttpResponseRedirect("/%i" %t.id)

    # else:
    #     form = CreateNewList()
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = SettingsForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/home/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    form = SettingsForm()

    return render(request, 'main/settings.html', {'form': form})
    # return render(response, "main/settings.html", {"form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.") 
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def index(response, id):
    ls = ToDoList.objects.get(id=id)
 
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
    
                item.save()
    
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
 
 
    return render(response, "main/list.html", {"ls":ls})

# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     return render(response,"main/list.html", {"ls":ls})



# def create(response):
#     if response.method == "POST":
#         form = CreateNewList(response.POST)

#         if form.is_valid():
#             n = form.cleaned_data["name"]
#             t = ToDoList(name=n)
#             t.save()

#         return HttpResponseRedirect("/%i" %t.id)

#     else:
#         form = CreateNewList()

#     return render(response, "main/create.html", {"form":form})

def index1(response):
   return render(response,"index.html",{})

# def simple_function(request):
#    #print("\nThisasimple function\n")
#    function1.launchPlatform()
#    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def index(response,request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    ls = ToDoList.objects.get(id=id)
    return render(response,"main/base.html", {"username":username})

# def home(response):
#     return render(response,"main/home.html", {"name":"test"})


# detecter les postes les plus resérvé
# reservation par equipe
# Sending emails
# styling python elements

#C:\Users\ybagdad\Automated_Reservation\main\selenium_folder\function1.py