from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Bankinfo
from .form import BankForm

# Create your views here.
def index(request):
    return render(request,'index.html',{
        'Bankinfos':Bankinfo.objects.all()
    })
def view_bankinfo(request, id):
    Bankinfos = Bankinfo.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method =='POST':
        form = BankForm(request.POST)
        if form.is_valid():
            new_Application_Number = form.cleaned_data['bank_id']
            new_first_name = form.cleaned_data['first_name']
            new_middle_name = form.cleaned_data['middle_name']
            new_last_name = form.cleaned_data['last_name']
            new_address_1 = form.cleaned_data['address_1']
            new_address_2 = form.cleaned_data['address_2']
            new_city = form.cleaned_data['city']
            new_state = form.cleaned_data['state']
            new_zip_code = form.cleaned_data['zip_code']
            new_phone = form.cleaned_data['phone']
            new_gender = form.cleaned_data['gender']
            new_email = form.cleaned_data['email']
            new_date_of_birth = form.cleaned_data['date_of_birth']
            new_social_number = form.cleaned_data['social_number']
            new_passport_no = form.cleaned_data['passport_no']
            new_account_type = form.cleaned_data['account_type']
            new_nominee_name = form.cleaned_data['nominee_name']
            
            new_Bankinfo = Bankinfo(
                bank_id =new_Application_Number,
                first_name =new_first_name,
                middle_name = new_middle_name,
                last_name = new_last_name,
                address_1 = new_address_1,
                address_2 = new_address_2,
                city = new_city,
                state = new_state,
                zip_code = new_zip_code,
                phone = new_phone,
                gender = new_gender,
                email = new_email,
                date_of_birth = new_date_of_birth,
                social_number = new_social_number,
                passport_no = new_passport_no,
                account_type = new_account_type,
                nominee_name =new_nominee_name
            )
            new_Bankinfo.save()
            return render(request,'add.html',{
                'form':BankForm(),
                'success':True
            })
    else:
        form=BankForm()
    return render(request,'add.html',{
        'form':BankForm()
    })

def edit(request, id):
    if request.method == 'POST':
        Bankinfos = Bankinfo.objects.get(pk=id)
        form = BankForm(request.POST, instance=Bankinfos)
        if form.is_valid():
            form.save()
            return render(request,'edit.html',{
                'form':form,
                'suceess':True
            })
    else:
        Bankinfos = Bankinfo.objects.get(pk=id)
        form = BankForm(instance=Bankinfos)
    return render(request,'edit.html', {
        'form':form
    })

def delete(request, id):
    if request.method == 'POST':
        Bankinfos = Bankinfo.objects.get(pk=id)
        Bankinfos.delete()
    return HttpResponseRedirect(reverse('index'))
           
    
