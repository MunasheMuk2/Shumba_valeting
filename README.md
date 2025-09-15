# Shumba Valeting

Shumba valeting is a **Full Stack Django website** designed for **car valeting services**.  
The site allows customers to explore valet packages, make bookings, and contact the business.  
The site has a complete CRUD implementation, responsive design, and database modelling. 

- [Site link](https://shumba-app-20d8670cc25d.herokuapp.com/)


## User Experience (UX)

### User Stories

**As a site user, I want to be able to:**
- Easily view valet packages, so that I can choose the right service for my car.  
- Make an online booking, so that I don’t need to phone the company.  
- Receive confirmation and feedback messages when I submit a booking or contact form.  
- Navigate smoothly across all pages on desktop and mobile, so that I can use the site anywhere.  

**As a site owner, I want to be able to:**
- Add, edit, and delete services and bookings, so that the business can stay up to date.  
- Receive booking requests and customer inquiries directly through the site.  
- Ensure the system validates user input when booking services, so there are no duplicate bookings 
- Provide customers with clear, professional branding in line with Shumba Valeting.  

---

### Purpose and Value of Shumba Valeting to users: 


Shumba Valeting is a **full-stack site** where customers can view packages, make bookings, and contact the business.  

Designed the site so the purpose of the site is **clear to first-time visitors**: it is a **car valeting booking and information platform**, targeting **high-end car owners** who want convenience, professionalism, and a luxury service.  

### Wireframes 

#### Mobile/Tablets/Desktop devices

- [Wireframe link](https://www.canva.com/design/DAGvX6KVp-M/JDVmeQI2DLzMSHCkSxI5jA/view?utm_content=DAGvX6KVp-M&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hc1f717e4d3)

### Wireframe Reasoning 

1. The wireframe prioritizes clarity and usability, ensuring users can quickly understand the purpose of Shumba Valeting.

2. Input fields on the booking form are logically grouped to guide the user through step-by-step data entry

3. The  buttons on home page are positioned to work as call to actions 

4. Images added to show users examples of thw work Shumba valeting does


### Colour Scheme
- **Black** – luxury, premium feel  
- **Silver/Grey** – professional, modern tone  
- **White** – clean readability  

### Typography
- **Playfair Display** (headings, luxury branding)  
- **Sans-serif fallback** (body text for readability)  


### Imagery
- High-quality imagery of valeting services is used across the Services page.  
- Each valet package has a dedicated image for visual clarity.  


# Project Features

---

##  Navigation Bar

- Placed at the top of every page, with links to **Home**, **Services**, **Contact**, and **Booking**.  
- Fully responsive across desktop and mobile.  
- On mobile, the navigation bar collapses into a **burger menu** for easier navigation.  

![Navigation Bar](screenshots/navbar.jpg)

---

##  Home Page

**Features:**

- Brand introduction with clear messaging.  
-  Call-to-action buttons directing users to the **Booking** page.  

![Home Page](screenshots/homepage.jpg)

---

##  Services Page

**Features:**

- Displays valet packages: **Basic, Premium, Executive, Luxury**.  
- Each package includes descriptions, pricing, and images.  

![Services Page](screenshots/servicespage.jpg)

---

##  Contact Page

**Features:**

- Contact form with fields for user details.  
- Built-in **validation** and error handling.  
- Submit button to send user inquiries.  

![Contact Page](screenshots/contactpage.jpg)

---

##  Booking form

**Features:**

- Booking form connected to the database.  
- Prevents **duplicate time slots** from being booked.  
- Provides **success/error feedback** upon submission.  

![Booking form](screenshots/bookingform.jpg)

---

## My Bookings Page

**Features:**

- Displays a list of all the user’s **upcoming bookings**.  
- Shows key details: **date, time slot, package, and action buttons**.  
- Allows users to **cancel bookings** with a confirmation prompt.  
- If no bookings exist, shows a friendly message: *"You have no bookings yet."*  

![My Bookings Page](screenshots/mybookingspage.jpg)

---


##  Sign Up Page

**Features:**

- User registration with **email, username, and password**.  
- Redirects users after successful registration.  

![Sign Up Page](screenshots/signuppage.jpg)

---
##  Login Page

**Features:**

- Allows users to **sign in** securely.  
- Provides a link to **sign up** if the user does not have an account.  
- CSRF protection for secure login requests.  

![Login Page](screenshots/loginpage.jpg)

---

## Logout Page

**Features:**

- Confirms before logging a user out.  
- CSRF protection for security.  
- Simple one-click **sign out** functionality.  

![Logout Page](screenshots/logoutpage.jpg)

---

- **CRUD Operations**:  

  - **Create**: Bookings and messages.  
  - **Read**: Services, bookings, and contact messages.  
  - **Update**: Admin updates booking records and contact messages.  
  - **Delete**: Admin removes bookings or contact messages.  
- **User Feedback**: Messages framework provides alerts (e.g., “Booking confirmed”, “Time slot already taken”).  
- **Responsive Design**: Works seamlessly across desktops, tablets, and mobiles.  


### Future features to Implement
- Online payments 
- SMS/email booking notifications.  
- Testimonials page.  


## Database Schema

The system uses Django ORM with models mapped to **PostgreSQL (production)**.

### Models

**Contact**
- `name` (CharField)  
- `email` (EmailField)  
- `message` (TextField)  

**Booking**  
- `user` (ForeignKey to Django User, optional for guests)  
- `name` (CharField)  
- `email` (EmailField)  
- `car_make_model` (CharField)  
- `car_reg` (CharField)  
- `package` (ForeignKey to Package)  
- `date` (DateField)  
- `time_slot` (CharField)  
- `created_at` (DateTimeField)  
- `cancelled` (BooleanField)  
- **Unique constraint** on (`date`, `time_slot`) – prevents double booking  

### Schema Characteristics
- One-to-many: `User to Bookings`, `Package to Bookings`.  

---

## Testing

### Manual Testing
- Forms tested with valid/invalid inputs. Validation errors display correctly.  
- Duplicate booking attempts rejected with error message.  

### CRUD Testing
- Added, updated, and deleted contact messages and bookings via Django Admin.  
- Verified CRUD operations reflected immediately in UI regarding bookings.  

### Responsive Testing
- Tested on desktop, tablet, and mobile (Chrome DevTools).  
- Grid layout adapts correctly.   

---

## Development Process

- **Version control**: Git & GitHub.  
- **Commit messages**: Small, descriptive, documenting progress.  
- **Process followed**:  
  1. Planning (wireframes, schema design, UX goals).  
  2. Setup (Django project, models, apps, templates).  
  3. Implementation (CRUD, forms, feedback).  
  4. Styling (CSS branding, responsive grid).  
  5. Testing (manual and validation).  
  6. Deployment (local + Heroku).  

---

### Solved bugs

1. Although I had created a superuser locally, I had to recreate the superuser on heroku so the admin panel could show up 

2. The booking form was showing an error like "Select a valid choice" for the package or time slot, even when the options looked right. Amended the packages to make sure they were in the data base, made sure the timeslots were being correctly passed into the form and updated mismatch between my local code and Heroku by updating  models and running migrations properly. (This issue came up because Heroku wasn't deployed on time—I had to wait for my GitHub Student Pack to get free credits for hosting.)

3. Had an issue with fave icons not working with normal links in base.html and so has to use template tags

---

### Unsolved bugs

1. Attempted to have a pop up alert message when there is a duplicate booking but site kept generating a message on the booking for due to the Django auto generated message from errors. Had to resort to using javascript within the home.html where the form is selected to scroll to the form on error. However the issue with the pop up message still stands as won't work. 
---

## Deployment

### Local Deployment
git clone https://github.com/MunasheMuk2/Shumba_valeting.git
cd shumba-valeting
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---

##  Remote Deployment (Heroku)

- Deployed with **Heroku**, using **PostgreSQL** as the database.  
- `Procfile` and `requirements.txt` included for deployment.  
- Environment variables managed in **Heroku Config Vars**.  
- `DEBUG = False` in production for security.  

## Remote Deployment after project completion (Heroku) 
Deployment delays (waiting for GitHub Student Pack credits)

* Step 1: Make Migrations Locally
* Step 2: Push Code to Heroku
* Step 3: Run Migrations on Heroku
* Step 4: Create a Superuser on Heroku
* Step 5: Sync Data (Packages & Time Slots)

* Due to late deployment onto Heroku - deployments split between git hub and Heroku 
---

## Security

- Used **SECRET_KEY** 
- `.gitignore` excludes sensitive files.  
- `DEBUG` disabled in production.  

---

##  Credits

- **Media**: Images sourced from [Unsplash](https://unsplash.com) & chatGPT. 
- **Code References**: code institute and youtube tutorials

## Technologies Used

- [VSCode](https://code.visualstudio.com/)  Used as the main code editor
- [GitHub](https://github.com/) code host for the site
- [W3schools](https://www.w3schools.com/howto/howto_js_accordion.asp) 
- Code institute tutorials for setting up models, apps, templates and heroku
-**Favicons**: Sourced from [favicon](https://favicon.io/)
---


# TESTING

## Compatibility

In order to confirm the correct functionality, responsiveness, and appearance:

+ The website was tested on popular browsers : Chrome and Microsoft edge

    - Chrome:

    ![Chrome](screenshots/chrome.jpg)

     - Microsoft Edge:

    ![Microsoft Edge](screenshots/MicrosoftEdge.jpg)

---

## Responsiveness


+ Also checked the website's responsiveness in devtools - Chrome.

    - Extra small devices:

    ![XS devices](screenshots/small-devices.jpg)

    ---

    - Small devices:

    ![Small devices](screenshots/smalldevices.jpg)

    ---

    - Medium devices:

    ![Medium devices](screenshots/medium-devices.jpg)

    ---
    
     - large/Xl devices:

    ![Extra large devices](screenshots/largexl.jpg)
---
## Manual testing

### Site Users
| User Story | Test Action | Expected Result | Status |
|---|---|---|---|
| View valet packages | Visit `/services` | See Basic, Premium, Executive, Luxury cards with price, image, description | Yes |
| Make online booking | Visit homepage - booking form - submit valid data | Booking saved, success message shown, redirected to Home | Yes |
| Smooth navigation | Use navbar on mobile/desktop | Links to Home/Services/Contact work | Yes |
| Input validation | Submit blank/invalid email; duplicate slot | Form errors shown; duplicate slot rejected with clear message | Yes|



### Site Owner/Admin
| User Story | Test Action | Expected Result | Status |
|---|---|---|---|
| Add/edit/delete services | Django Admin: Packages | Create, update, delete package | Yes|
| Manage contact messages | Django Admin: Bookings | Create, View, edit, delete | Yes |


---

##  Functional Testing (Manual)

### 2.1 Booking Form
| Case | Steps | Expected | Result |
|---|---|---|---|
| Valid booking | Fill required fields (date, time slot, package, name/email ) - Submit | Success message | Yes |
| Missing required field | Leave `date` blank - Submit | Field error under `date` | Yes |
| Invalid email | Enter email without @ - Submit | Email validation error | Yes |
| Duplicate slot | Create booking for same `date + slot` | Error message: slot already booked | Yes |



### Contact Form
| Case | Steps | Expected | Result |
|---|---|---|---|
| Valid submission | Fill name/email/message → Submit | Success message; Message received | Yes |
| Missing name | Submit empty `name` | Field error shown | Yes |
| Invalid email | Submit email without @ | Email validation error | Yes |




## 3 CRUD Coverage

CRUD operations verified through **UI** and **Django Admin**.

| Entity | Create | Read | Update | Delete | UI Reflection |
|---|---|---|---|---|---|
| Service | Admin adds service | Services page lists correctly | Admin edits service | Admin deletes service | Changes visible immediately on `/services` |
| Booking | User submits form | Admin can view; user sees message | Admin edits record/slot | Admin deletes record | Changes reflected: duplicates blocked, messages updated |
| Contact | User submits form | Admin can read | (N/A for user) | Admin deletes | (Back-office only) |



## Validator testing
+ ### HTML

  #### Landing Page
   
    ![Landing Page HTML Validator](screenshots/htmlvalidator.jpg).

     - No errors or warnings were found when passing through the official W3C validator.

      #### Vehicle guide Page
   
    ![Vehicle guide Page HTML Validator](screenshots/vehicleguidevalidator.jpg).

     - No errors or warnings were found when passing through the official W3C validator.

     #### Contact us Page
   
    ![Contact us Page HTML Validator](screenshots/contactusvalidator.jpg).

     - No errors or warnings were found when passing through the official W3C validator.

 #### Contact sucess Page
   
   ![Contact sucess Page HTML Validator](screenshots/successvalidator.jpg).

     - No errors or warnings were found when passing through the official W3C validator.



    
+ ### CSS
  No errors or warnings were found when passing through the official W3C (Jigsaw) validator 
    ![CSS](screenshots/cssvalidator.jpg)

 ---

+ ### JSHint

 No errors or warnings were found when passing through the JS code in JSHint. 

   ![JSHint](screenshots/jshint.jpg)

---


## Acknowledgments

- [Code Institute](https://codeinstitute.net/) 










