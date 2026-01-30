from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'


#Task 3 new function
@app.get('/students')
async def get_students():
    return data
#end of new function


# #Task 4 new function
# @app.get('/students/{id}')
# async def get_student(id):
#     for student in data:
#         if student['id'] == id: #only return the student if the ID matches
#             return student

# #Task 5 (Updated Task 4 function)
# @app.get('/students')
# async def get_students(pref=None):
#     if pref:
#         filtered_students = []
#         for student in data:
#             if student['pref'] == pref:  #select only the students with a given meal preference
#                 filtered_students.append(student) #add match student to the result
#             return filtered_students
#     return data
# #end of new function


# Exercise 1
# Create a route/stats which returns a count of the various meal preferences and programmes in the data set. Example:
# {
#     Chicken: 76,
#     Computer Science (Major): 11,
#     Computer Science (Special): 37,
#     Fish: 6,
#     Information Technology (Major): 26,
#     Information Technology (Special): 18,
#     Vegetable: 10
# }
#Solution:
@app.get('/stats')
async def get_stats():
    stats = {}
    for student in data:
        pref = student['pref']
        programme = student['programme']
        
        if pref in stats:
            stats[pref] += 1
        else:
            stats[pref] = 1
        
        if programme in stats:
            stats[programme] += 1
        else:
            stats[programme] = 1
            
    return stats
#End of solution

#My Statistics that was displayed at the url "http://127.0.0.1:8000/stats":
# {
#     Chicken: 76,
#     Computer Science (Special): 37,
#     Information Technology (Special): 18,
#     Computer Science (Major): 11,
#     Fish: 9,
#     Information Technology (Major): 26,
#     Vegetable: 10,
#     I.T. Major, Management & Communications Minor (Can only make it to Friday's labs): 1,
#     Lingustics: 1,
#     Major:Mathematics : 1
# }



#Exercise 2
#Create additional routes; /add/a/b, /subtract/a/b, multiple/a/b and divide/a/b that takes in 2 route parameters a and b and returns the result of the calculation.
#Solution:
@app.get('/add/{a}/{b}')
async def add_numbers(a: int, b: int):
    result = a + b
    return {"operation": "addition", "a": a, "b": b, "result": result}
#Example: http://localhost:8000/add/2/4

@app.get('/subract/{a}/{b}')
async def subtract_numbers(a: int, b: int):
    result = a- b
    return {"operation": "subraction", "a": a, "b": b, "result": result}


@app.get('/multiply/{a}/{b}')
async def multiply_numbers(a: int, b: int):
    result = a * b
    return {"operation": "multiplication", "a": a, "b": b, "result": result}


@app.get('/divide/{a}/{b}')
async def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    result = a / b
    return {"operation": "division", "a": a, "b": b, "result": result}