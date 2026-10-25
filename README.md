# Smart Appointment System for OPD and Medical sector #

## Inspiration✨: 

I got this idea because my father is a doctor and sometimes his OP appointments are overlapping with his surgeries, his free time, etc. Then later I also realized that most of the doctors and patients face this problem of not proper communication or coordination between the doctor and the patient. So, I have decided to make a system where there will be a proper coordinated communication between a doctor and the patient. I want to create an app where it a platform for the whole hospital or a department where the app would know the doctors' every day schedule but for now I made a small website using streamlit. When I have enough resources I will try to make and app for this.   

## Tech Stack⚒️:

**Python:** Like most of my projects this is built by using python as the main programming language as it is powerful tool, easy to spot errors, can be easily run through windows and it is cost effective

**Streamlit:** Of course for patients and doctors to interact with each other there should be a common platform where they can communicate or send information to each other.So, I used streamlit to do this task for now as it can be easliy run through python and make a good basic model for the website  

## Website Architecture🏛️:

In the website there are two portals one patient portal and other the doctor portal(in real application of this the people will have designated portal to them and they cannot view the other portal. This option of switching is only here for reference)

### **The Patient Portal:**
This is where the patient fills in all the details of their main problem, at what time can visit the doctor for OPD, etc 

![OPD_preview](Patient_Portal.png)

<ins> **Main Components:** </ins>

**The Main details section:** </br>
This is the part where the patient enters their personal details like name, age, and gender. As well as the time they were able to visit and the doctor they are willing to visit (Note:The system already knows when the doctor is avilable for OP and only gives those timings ).

**The Medical Background Section:** 

This is the section where the patient fills in the details regarding the problems they are facing and their past medical history like past surgeries, diseases they have,etc. These details directly go to the doctor where he/she can view the details through their portal and get the concise idea of what patient is facing before they even see the patient physically.


**The Conformation:** After the patient is done filling in their details and medical information, they can click "Confirm Appointment" and their appointment will immediately be booked and their details sent to the doctor portal.

**Generate Random medical history:** Just a utility feature that generates random medical history for the convenience of anyone reviewing this prototype; this would not be present in a production build.


### **The Doctor Portal:** </br>
This the part where the doctor can view when his/her appointment with the patient is scheduled and view the details about the patient before even meeting the patient. 





