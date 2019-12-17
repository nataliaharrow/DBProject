# Mentor Meet

Library/Language Requirements:
1. Python 3.x.x
2. Django
3. Crispy Forms
4. Pillow
5. MySQL & SQLite (default) (database can be changed in /mentorproject/mentorapp/mentorapp/settings.py)

Steps to run locally:
1. Navigate to repo location in terminal
2. Call `python manage.py runserver`
3. Navigate to port provided in output + **'/home'**

Mentor Meet is the first project created by our team NTFs. We are comprised of Natalia Harrow, Terri Thampan, and Florence Fong. 

**The project implements all CRUD operations:** 
- Users can register to the portal as students or mentors. They can provide personal and professfional information about themselves such as their name, email address, attended schools, majors, companies, positions and industries. All the information is then **saved** and stored in a User table along with each user's id. 

- Each user has their own profile that includes all their information and a photo

- Users can **edit** and **remove** their personal and professional information

- Students that wish to be provided mentor's help on a specific career related issue can submit a request to which they can attach a file such as a resume, transcript or cover letter. 

- Students and mentors can **search** for each other based on the information provided and see other users' profiles.

- Users can connect with each other. The database stores the connections in a separate table that stores the user that sent the invite, invited user, request and request's status (pending, accepted or declined)

- Connections can be removed

- Registered users can log in to the portal and access all user specific pages such as their personal profiles, connections and pending invitations

