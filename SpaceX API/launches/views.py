from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import requests
from datetime import datetime
from django.urls import reverse
from .models import *

base_link = "https://api.spacexdata.com/v3/"

def updateLaunches():
    response = requests.get(base_link + "launches")

    json_object = response.json()

    launch_details = []

    for item in json_object:
        
        new_launch = {}
            
        new_launch.update({"flight_number":item["flight_number"]})

        timestamp = item["launch_date_unix"]
        dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%Y-%m-%d")
        new_launch.update({"launch_date":dt_object})

        new_launch.update({"rocket_name":item["rocket"]["rocket_name"]})

        new_launch.update({"mission_patch_link":item["links"]["mission_patch_small"]})

        new_launch.update({"reddit_launch":item["links"]["reddit_launch"]})
        
        new_launch.update({"video_link":item["links"]["video_link"]})
        
        new_launch.update({"wikipedia":item["links"]["wikipedia"]})
        
        new_launch.update({"article_link":item["links"]["article_link"]})
        
        new_launch.update({"details":item["details"]})
        
        new_launch.update({"launch_success":item["launch_success"]})
    
        launch_details.append(str(new_launch))

        if Launches.objects.filter(flight_number=new_launch.get("flight_number")).exists():
            l = Launches.objects.filter(flight_number=new_launch.get("flight_number")).update(**new_launch)
        else:
            l = Launches(**new_launch)
            l.save()

def updateMissions():
    response = requests.get(base_link + "missions")

    json_object = response.json()

    mission_details = []

    for item in json_object:
        
        new_mission = {}
            
        new_mission.update({"mission_name":item["mission_name"]})

        new_mission.update({"mission_id":item["mission_id"]})

        new_mission.update({"wikipedia":item["wikipedia"]})
        
        new_mission.update({"twitter":item["twitter"]})

        new_mission.update({"website":item["website"]})

        new_mission.update({"description":item["description"]})
    
        mission_details.append(str(new_mission))

        if Mission.objects.filter(mission_id=new_mission.get("mission_id")).exists():
            m = Mission.objects.filter(mission_id=new_mission.get("mission_id")).update(**new_mission)
        else:
            m = Mission(**new_mission)
            m.save()

def updateCores():
    response = requests.get(base_link + "cores")

    json_object = response.json()

    core_details = []

    for item in json_object:
        
        new_core = {}
            
        new_core.update({"core_serial":item["core_serial"]})

        timestamp = item["original_launch_unix"]

        if timestamp != None:
            dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%Y-%m-%d")
        new_core.update({"launch_date":dt_object})

        new_core.update({"mission_name":item["missions"][0]["name"]})

        new_core.update({"mission_flight":item["missions"][0]["flight"]})

        new_core.update({"details":item["details"]})
    
        core_details.append(str(new_core))

        if Core.objects.filter(core_serial=new_core.get("core_serial")).exists():
            m = Core.objects.filter(core_serial=new_core.get("core_serial")).update(**new_core)
        else:
            m = Core(**new_core)
            m.save()

def updateRockets():
    response = requests.get(base_link + "rockets")

    json_object = response.json()

    rocket_details = []

    for item in json_object:
        
        new_rocket = {}
            
        new_rocket.update({"rocket_number":item["id"]})
            
        new_rocket.update({"active":item["active"]})
            
        new_rocket.update({"cost_per_launch":item["cost_per_launch"]})
            
        new_rocket.update({"country":item["country"]})
            
        new_rocket.update({"wikipedia":item["wikipedia"]})
            
        new_rocket.update({"rocket_id":item["rocket_id"]})
            
        new_rocket.update({"description":item["description"]})
            
        new_rocket.update({"rocket_name":item["rocket_name"]})

        first_flight = datetime.strptime(item["first_flight"],"%Y-%m-%d")
        new_rocket.update({"first_flight":first_flight})
        
        rocket_details.append(str(new_rocket))

        if Rocket.objects.filter(rocket_id=new_rocket.get("rocket_id")).exists():
            m = Rocket.objects.filter(rocket_id=new_rocket.get("rocket_id")).update(**new_rocket)
        else:
            m = Rocket(**new_rocket)
            m.save()

def details(request):
    response = requests.get(base_link + "launches")

    json_object = response.json()

    launch_details = []

    for item in json_object:
        
        new_launch = {}
            
        new_launch.update({"flight_number":item["flight_number"]})

        timestamp = item["launch_date_unix"]
        dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%d-%B-%Y")
        new_launch.update({"launch_date":dt_object})

        new_launch.update({"rocket_name":item["rocket"]["rocket_name"]})

        new_launch.update({"mission_patch_link":item["links"]["mission_patch_small"]})

        new_launch.update({"reddit_launch":item["links"]["reddit_launch"]})
        
        new_launch.update({"video_link":item["links"]["video_link"]})
        
        new_launch.update({"wikipedia":item["links"]["wikipedia"]})
        
        new_launch.update({"article_link":item["links"]["article_link"]})
        
        new_launch.update({"details":item["details"]})
        
        new_launch.update({"launch_success":item["launch_success"]})
    
        launch_details.append(str(new_launch))

    response = requests.get(base_link + "missions")

    json_object = response.json()

    mission_details = []

    for item in json_object:
        
        new_mission = {}
            
        new_mission.update({"mission_name":item["mission_name"]})

        new_mission.update({"mission_id":item["mission_id"]})

        new_mission.update({"wikipedia":item["wikipedia"]})
        
        new_mission.update({"twitter":item["twitter"]})

        new_mission.update({"website":item["website"]})

        new_mission.update({"description":item["description"]})
    
        mission_details.append(str(new_mission))

    
    response = requests.get(base_link + "cores")

    json_object = response.json()

    core_details = []

    for item in json_object:
        
        new_core = {}
            
        new_core.update({"core_serial":item["core_serial"]})

        timestamp = item["original_launch_unix"]

        if timestamp != None:
            dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%d-%B-%Y")
        new_core.update({"launch_date":dt_object})

        new_core.update({"mission_name":item["missions"][0]["name"]})

        new_core.update({"mission_flight":item["missions"][0]["flight"]})

        new_core.update({"details":item["details"]})
    
        core_details.append(str(new_core))

    response = requests.get(base_link + "rockets")

    json_object = response.json()

    rocket_details = []

    for item in json_object:
        
        new_rocket = {}
            
        new_rocket.update({"id":item["id"]})
            
        new_rocket.update({"active":item["active"]})
            
        new_rocket.update({"cost_per_launch":item["cost_per_launch"]})
            
        new_rocket.update({"country":item["country"]})
            
        new_rocket.update({"wikipedia":item["wikipedia"]})
            
        new_rocket.update({"rocket_id":item["rocket_id"]})
            
        new_rocket.update({"description":item["description"]})
            
        new_rocket.update({"rocket_name":item["rocket_name"]})

        new_rocket.update({"first_flight":item["first_flight"]})
        
        rocket_details.append(str(new_rocket))

    return HttpResponse("<h1>Launches Details</h1>"+"<br><br>".join(launch_details)+"<h1>Mission Details</h1>"+"<br><br>".join(mission_details)+"<h1>Core Details</h1>"+"<br><br>".join(core_details)+"<h1>Rocket Details</h1>"+"<br><br>".join(rocket_details))

def home(request):
    response = requests.get(base_link + "launches/latest")

    json_object = response.json()

    item = json_object 

    latest_launch = {}
            
    latest_launch.update({"flight_number":item["flight_number"]})

    timestamp = item["launch_date_unix"]
    dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%d-%B-%Y")
    latest_launch.update({"launch_date":dt_object})

    latest_launch.update({"rocket_name":item["rocket"]["rocket_name"]})

    latest_launch.update({"mission_patch_link":item["links"]["mission_patch_small"]})

    latest_launch.update({"reddit_launch":item["links"]["reddit_launch"]})
        
    latest_launch.update({"video_link":item["links"]["video_link"]})
        
    latest_launch.update({"wikipedia":item["links"]["wikipedia"]})
        
    latest_launch.update({"article_link":item["links"]["article_link"]})
        
    latest_launch.update({"details":item["details"]})
        
    latest_launch.update({"launch_success":item["launch_success"]})
    
    response = requests.get(base_link + "launches/next")

    json_object = response.json()

    item = json_object

    next_launch = {}
            
    next_launch.update({"flight_number":item["flight_number"]})

    timestamp = item["launch_date_unix"]
    dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%d-%B-%Y")
    next_launch.update({"launch_date":dt_object})

    next_launch.update({"rocket_name":item["rocket"]["rocket_name"]})

    next_launch.update({"mission_patch_link":item["links"]["mission_patch_small"]})

    next_launch.update({"reddit_launch":item["links"]["reddit_launch"]})
        
    next_launch.update({"video_link":item["links"]["video_link"]})
        
    next_launch.update({"wikipedia":item["links"]["wikipedia"]})
        
    next_launch.update({"article_link":item["links"]["article_link"]})
        
    next_launch.update({"details":item["details"]})
        
    next_launch.update({"launch_success":item["launch_success"]})
    
    context = {
        'latest': latest_launch,
        'next': next_launch,
    }
    return render(request,"home.html",context)

def allLaunches(request):
    no = Launches.objects.first().id
    return HttpResponseRedirect(reverse('main:launches',kwargs={'no':no,'category':"all"}))


def launchesPast(request):
    no = Launches.objects.filter(launch_success__isnull=False).first().id
    return HttpResponseRedirect(reverse('main:launches',kwargs={'no':no,'category':"past"}))
    

def launchesUpcoming(request):
    no = Launches.objects.filter(launch_success__isnull=True).first().id
    return HttpResponseRedirect(reverse('main:launches',kwargs={'no':no,'category':"upcoming"}))

def launches(request,category,no):
    if request.method == "POST":
        if 'refresh' in request.POST:
            updateLaunches()
            return HttpResponseRedirect(reverse('main:launches',kwargs={'no':no,'category':category}))
        elif 'filter' in request.POST:
            category = request.POST['category']
            if category=="upcoming":
                return HttpResponseRedirect(reverse('main:launchesUpcoming'))
            elif category=="past":
                return HttpResponseRedirect(reverse('main:launchesPast'))
            else:
                return HttpResponseRedirect(reverse('main:allLaunches'))

    if category=="all":
        
        launch_details = Launches.objects.all()

    elif category=="upcoming":
        
        launch_details = Launches.objects.filter(launch_success__isnull=True)

    elif category=="past":
        
        launch_details = Launches.objects.filter(launch_success__isnull=False)

    current_launch = launch_details.filter(id=no)[0]
    
    context = {
        'launch_details': launch_details,
        'current':current_launch,
        'no':no,
        'category':category,
    }
    return render(request,"launches.html",context)

def allMissions(request):
    no = Mission.objects.first().id
    return HttpResponseRedirect(reverse('main:missions',kwargs={'no':no}))

def missions(request,no):
    if request.method == "POST":
        updateMissions()
        return HttpResponseRedirect(reverse('main:missions',kwargs={'no':no}))

    mission_details = Mission.objects.all()

    current_mission = Mission.objects.filter(id=no)[0]

    context = {
        'mission_details': mission_details,
        'current':current_mission,
        'no':no,
    }
    return render(request,"missions.html",context)

def allCores(request):
    no = Mission.objects.first().id
    return HttpResponseRedirect(reverse('main:cores',kwargs={'no':no}))

def cores(request,no):
    if request.method == "POST":
        updateCores()
        return HttpResponseRedirect(reverse('main:cores',kwargs={'no':no}))

    core_details = Core.objects.all()

    current_core = Core.objects.filter(id=no)[0]

    context = {
        'core_details': core_details,
        'current':current_core,
        'no':no,
    }
    return render(request,"cores.html",context)

def allRockets(request):
    updateRockets()
    no = Mission.objects.first().id
    return HttpResponseRedirect(reverse('main:rockets',kwargs={'no':no}))

def rockets(request,no):
    if request.method == "POST":
        updateRockets()
        return HttpResponseRedirect(reverse('main:rockets',kwargs={'no':no}))

    rocket_details = Rocket.objects.all()

    current_rocket = Rocket.objects.filter(id=no)[0]

    context = {
        'rocket_details': rocket_details,
        'current':current_rocket,
        'no':no,
    }
    return render(request,"rockets.html",context)