from pymongo import MongoClient
import certifi
try:
    MONGO_URI = "mongodb+srv://punitectssrgsp_db_user:mongodb123@cluster0.h7lbrs1.mongodb.net/"
    client = MongoClient(MONGO_URI,tls=True,tlsCAFile=certifi.where())
    client.admit.command("ping")
    db = client["ssus1234"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]
    print("MongoDB connection successfully")
except Exception as e:
    print("MongoDB Error:",e)
#MONGODB CODE
