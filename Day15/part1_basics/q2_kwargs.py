def student_details(**details):
    print (details)
    for key,value in details.items():
        print(f"{key}:{value}")
        
student_details(name="aman",branch="aiml",cgpa=8.5,placed=True)
print("---")
student_details(name="riya",company="servicenow",package=14.97)

def create_api_endpoint(**config):
    print(f"Creating API at {config.get('url')} with model {config.get('model')}")
    
create_api_endpoint(url="/predict",model="distilbert",version="v1")