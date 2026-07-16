from pymongo import MongoClient
try:
    MONGO_URI = "mongodb+srv://punitectssrgsp_db_user:MongoDB#05@cluster0.h7lbrs1.mongodb.net/"
    client = MongoClient(MONGO_URI)
    db = client.admit.command("ping")
    db = client["ssus"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]
    print("MongoDB connection successfully")
except ExceptionGroup as e:
    print("MongoDB Error:",e)
#MONGODB CODE
