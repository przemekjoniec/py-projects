def getUserInfo(name, surname, job):
    name = name.upper().strip()
    surname = surname.upper().strip()
    job = job.lower().strip()
    text = "Name: " + name + ", Surname: " + surname + ", job: " + job
    print(text)

getUserInfo("Kate   ", "   Johnson    ", "PrograMMER")