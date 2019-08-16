from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import requests
from datetime import datetime
from django.urls import reverse

base_link = "https://api.spacexdata.com/v3/"

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
    
    print(next_launch)
    context = {
        'latest': latest_launch,
        'next': next_launch,
    }
    return render(request,"home.html",context)

def allLaunches(request):
    return HttpResponseRedirect(reverse('main:launches',kwargs={'no':1,'category':"all"}))


def launchesPast(request):
    return HttpResponseRedirect(reverse('main:launches',kwargs={'no':1,'category':"past"}))
    

def launchesUpcoming(request):
    
    return HttpResponseRedirect(reverse('main:launches',kwargs={'no':1,'category':"upcoming"}))

def launches(request,category,no):

    if category=="all":
        response = requests.get(base_link + "launches")

        json_object = response.json()

        launch_details = []

        for item in json_object:
            
            new_launch = {}
                
            new_launch.update({"flight_number":item["flight_number"]})

            new_launch.update({"rocket_name":item["rocket"]["rocket_name"]})
        
            launch_details.append(new_launch)
    
    else:
        response = requests.get(base_link + "launches/" + category)

        json_object = response.json()

        launch_details = []

        for item in json_object:
            
            new_launch = {}
                
            new_launch.update({"flight_number":item["flight_number"]})

            new_launch.update({"rocket_name":item["rocket"]["rocket_name"]})

            launch_details.append(new_launch)
    
    response = requests.get(base_link + "launches/" + str(no))

    json_object = response.json()

    item = json_object 

    current_launch = {}
            
    current_launch.update({"flight_number":item["flight_number"]})

    timestamp = item["launch_date_unix"]
    dt_object = datetime.strftime(datetime.fromtimestamp(timestamp),"%d-%B-%Y")
    current_launch.update({"launch_date":dt_object})

    current_launch.update({"rocket_name":item["rocket"]["rocket_name"]})

    current_launch.update({"mission_patch_link":item["links"]["mission_patch_small"]})

    current_launch.update({"reddit_launch":item["links"]["reddit_launch"]})
        
    current_launch.update({"video_link":item["links"]["video_link"]})
        
    current_launch.update({"wikipedia":item["links"]["wikipedia"]})
        
    current_launch.update({"article_link":item["links"]["article_link"]})
        
    current_launch.update({"details":item["details"]})
        
    current_launch.update({"launch_success":item["launch_success"]})
    
    print(launch_details)
    context = {
        'launch_details': launch_details,
        'current':current_launch,
        'no':no,
        'category':category,
    }
    return render(request,"launches.html",context)
