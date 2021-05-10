# DocAppoints
**WebApp for general or specific medical appointments.**   
Allows users to make appointments for new or registered patients, as well as modify existings appointments or delete. Users can register new doctors or patients, and make reports (future iterations). This is a final project for an school assignment, currently being developed.

## Requirements for this assignment  
* Flask / Django as web framework.
* MySQL as database.
* Python.

## How to run
1. Clone this repository  
``` git clone https://github.com/AlanHerediaG/docappoints.git ```
2. Install dependencies  
``` pip install -r requirements.txt```
3. Create a file called '.env' on the same directory as manage.py, and write your django' SECRET_KEY  
``` SECRET_KEY = <your_secret_key> ```
4. Run the server  
``` python manage.py runserver```  
Access the server on http://localhost:8000

## Roadmap
- [x] Basic layout for every view.
- [x] Retrieve all basic entities (doctors/patients/appointments).
- [x] Make new appointments.
- [x] Register new doctors/patients.
- [ ] Update/Delete appointments.
- [ ] Basic reports.
- [ ] Refresh appointments list of the day.