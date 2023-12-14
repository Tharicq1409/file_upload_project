from django.shortcuts import render,redirect
from . forms import candidate_form
from django.http import JsonResponse

def application(request):
    if request.method == 'POST':
        form = candidate_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('applynow')
        else:
            print(form.errors)
    else:
        form = candidate_form()
    return render(request, "applynow.html", {'form': form})



def autocomplete(request):
    suggestions = ["C","JavaScript","Python","Java","C#","C++","PHP","Swift","TypeScript","Ruby","Go","Rust","Kotlin","Scala","HTML","CSS","Bash",
                   "Data Structures","Algorithms","Database Management Systems (DBMS)","Operating Systems","Networking","Web Technologies","Version Control",
                   "Software Development Life Cycle (SDLC)","Debugging and Testing","Cybersecurity Basics","Cloud Computing","Basic Linux Commands","Soft Skill",] 
    
    query = request.GET.get('term', '').split(',')[-1].strip().lower()  
    if len(query) >= 1:
        filtered_suggestions = [word for word in suggestions if word.lower().startswith(query)]
    else:
        filtered_suggestions = []
    print(f"Query: {query}, Suggestions: {filtered_suggestions}")
    return JsonResponse(filtered_suggestions, safe=False)


def city_auto(request):
    suggestions = ["Delhi","Mumbai","Kolkata","Chennai","Bangalore","Hyderabad","Ahmedabad","Pune",
                "Jaipur","Lucknow","Kanpur","Nagpur","Patna","Indore","Thiruvananthapuram","Kochi","Bhopal","Surat","Visakhapatnam",
                "Coimbatore","Tirunelveli"]
    query = request.GET.get('term', '')
    if len(query) >= 3:
        filtered_suggestions = [word for word in suggestions if word.lower().startswith(query)]#if query.lower() in word.lower()]
    else:
        filtered_suggestions = []
    print(f"Query: {query}, Suggestions: {filtered_suggestions}")
    return JsonResponse(filtered_suggestions, safe=False)


def state_auto(request):
    suggestions = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                "Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
                "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",            
                ]
    query = request.GET.get('term', '')
    if len(query) >= 3:
        filtered_suggestions = [word for word in suggestions if word.lower().startswith(query)]#if query.lower() in word.lower()]
    else:
        filtered_suggestions = []
    print(f"Query: {query}, Suggestions: {filtered_suggestions}")
    return JsonResponse(filtered_suggestions, safe=False)


