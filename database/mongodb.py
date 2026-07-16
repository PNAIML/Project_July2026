from pymongo import MongoClient
import certifi
try:
    MONGO_URI = "mongodb+srv://punit541985_db_user:mongodb123@cluster0.twjwbke.mongodb.net/?appName=Cluster0"
    client = MongoClient(MONGO_URI,tls=True,tlsCAFile=certifi.where())
    client.admit.command("ping")
    db = client["ssus_project"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]
    print("MongoDB connection successfully")
except Exception as e:
    print("MongoDB Error:",e)
#MONGODB CODE
