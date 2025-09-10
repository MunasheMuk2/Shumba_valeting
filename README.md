# Shumba Valeting

Shumba valeting is a **Full Stack Django website** designed for **car valeting services**.  
The site allows customers to explore valet packages, make bookings, and contact the business.  
The site has a complete CRUD implementation, responsive design, and database modelling, with an emphasis on a **professional, luxury user experience**.

The site can be accessed by this [link](https://munashemuk2.github.io/StackSmartGuide/)


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

## 🧭 Navigation Bar

- Placed at the top of every page, with links to **Home**, **Services**, **Contact**, and **Booking**.  
- Fully responsive across desktop and mobile.  
- On mobile, the navigation bar collapses into a **burger menu** for easier navigation.  

![Navigation Bar](screenshots/navbar.jpg)

---

## 🏠 Home Page

**Features:**

- Brand introduction with clear messaging.  
-  Call-to-action buttons directing users to the **Booking** page.  

![Home Page](screenshots/homepage.jpg)

---

## 🛠️ Services Page

**Features:**

- Displays valet packages: **Basic, Premium, Executive, Luxury**.  
- Each package includes descriptions, pricing, and images.  

![Services Page](screenshots/servicespage.jpg)

---

## ✉️ Contact Page

**Features:**

- Contact form with fields for user details.  
- Built-in **validation** and error handling.  
- Submit button to send user inquiries.  

![Contact Page](screenshots/contactpage.jpg)

---

## 📅 Booking Page

**Features:**

- Booking form connected to the database.  
- Prevents **duplicate time slots** from being booked.  
- Provides **success/error feedback** upon submission.  

![Booking Page](screenshots/bookingpage.jpg)

---

- **CRUD Operations**:  

  - **Create**: Bookings and messages.  
  - **Read**: Services, bookings, and contact messages.  
  - **Update**: Admin updates booking records and services.  
  - **Delete**: Admin removes bookings or services.  
- **User Feedback**: Django messages framework provides alerts (e.g., “Booking confirmed”, “Time slot already taken”).  
- **Responsive Design**: Works seamlessly across desktops, tablets, and mobiles.  


### Future features to Implement
- Online payments 
- SMS/email booking notifications.  
- Testimonials page.  


## Database Schema

The system uses Django ORM with models mapped to **SQLite (development)** / **PostgreSQL (production)**.

### Models

**Contact**
- `name` (CharField)  
- `email` (EmailField)  
- `message` (TextField)  

**Booking**
- `user` (ForeignKey to Django User, optional for guests)  
- `date` (DateField)  
- `time_slot` (CharField / TimeField)  
- `package` (ForeignKey to Service)  
- **Unique constraint** on date + time_slot  

**Service**
- `title` (CharField)  
- `description` (TextField)  
- `price` (DecimalField)  
- `image` (ImageField)  

### Schema Characteristics
- Fully normalised, relational database.  
- One-to-many: `User → Bookings`, `Service → Bookings`.  
- Centralised config in `settings.py`.  
- Schema matches business needs (car valeting domain).  

---

## Testing

### Manual Testing
- Forms tested with valid/invalid inputs. Validation errors display correctly.  
- Duplicate booking attempts rejected gracefully with error message.  

### CRUD Testing
- Added, updated, and deleted services and bookings via Django Admin.  
- Verified CRUD operations reflected immediately in UI.  

### Responsive Testing
- Tested on desktop, tablet, and mobile (Chrome DevTools).  
- Grid layout adapts correctly.  

### Browser Testing
- Works in Chrome, Firefox, Safari, Edge.  

### Accessibility
- Checked colour contrast with Lighthouse.  
- Semantic HTML (headings, lists, alt text).  

---

## 🛠️ Development Process

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

## Deployment

### Local Deployment
git clone https://github.com/yourusername/shumba-valeting.git
cd shumba-valeting
python -m venv venv
venv\Scripts\activate      
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---


## 🚀 Remote Deployment (Heroku)

- Deployed with **Heroku**, using **PostgreSQL** as the database.  
- `Procfile` and `requirements.txt` included for deployment.  
- Environment variables managed in **Heroku Config Vars**.  
- `DEBUG = False` in production for security.  

---

## 🔒 Security

- Used **SECRET_KEY** 
- `.gitignore` excludes sensitive files.  
- `DEBUG` disabled in production.  

---

## 🙌 Credits

- **Media**: Images sourced from [Unsplash](https://unsplash.com) & chatGPT. 
- **Code References**: code institute and youtube tutorials












### Target audience:

- Logistics transportation planners and freight forwarders 


### Purpose and Value of Stack Smart Guide to users: 

The site makes freight planning easier for logistics professionals as the guide suggests the ideal vehicle size based on the cargo they will be transporting.  In return, their planning will be more efficient, ensures safe transportation as goods will not be overloaded over the vehicle weight capacity and they will choose the right vehicle that fits all goods which reduces costs of sending replacement vehicles to their clients due to miscalculation errors. 

### Planning 

Defined the core purpose: smart vehicle recommendation.Outlined key pages: Home, Vehicle Guide, Contact. Identified target users: logistics professionals

### Core Site Formula applied in JavaScript

 ### How to Determine if Pallets Fit in a Vehicle

 1.	Check the Total Pallet Length Against the Vehicle Length

- Multiply the length of a single pallet by the total number of pallets.
- If the combined pallet length is equal to or less than the van's length, proceed to check the width.
- If the total length exceeds the van’s length, rearrangement might be necessary.

2.	Adjust the Pallet Orientation to Fit the Space

- Pallets can be rotated to reduce the total length taken up inside the vehicle.
- Example: If a pallet is 120 cm (length) × 100 cm (width), it can be rotated so that the 100 cm width becomes the length instead, potentially making the load fit better.

3.	Check the Width of the Pallets Against the Vehicle Width

- After adjusting or confirming the length, check if pallets fit within the vehicle’s width.
- Apply the same logic: If width exceeds the van’s limit, consider rotating the pallets to balance the fit.

4.	Consider Stackability (If Applicable)

- If the pallets are stackable, multiply the height of one pallet by the number stacked until reaching the vehicle’s height limit.
- StackSmartGuide does not account for stackable pallets, so this step is omitted in its calculations.

### Total volume

Total pallet dimensions = Length × Width × Height
-	Length: The length of the pallet.
-	Width: The width of the pallet.
-	Height: The height of the pallet.

For example: 
120cm (length) × 100cm (width) × 150 cm (height) = 1,800,000 cubic centimetres (cm³)

### Final Decision

- If the combined pallet dimensions fit within the vehicle’s length, width, and height, then the vehicle is suitable.
- If not, a larger vehicle may be needed.
- Total volume was also used in JS to recommend the appropriate vehicle size, ensuring efficient and safe transportation.
---

### User stories:

_First time visitors_

1. As a logistics professional I want a simple and intuitive, easy-to-use platform that simplifies complex logistics calculations.

2. As a logistics professional I want key dimensions unit inputs that ensure the correct sized vehicle is recommended 

3. As a logistics professional I want to see Stack Smart Guide’s social links in case I need further information from their logistics community on how to use the guide tool etc

_Returning visitors_

1. As a logistics professional, I want accurate cargo calculations and vehicle recommendations to ensure optimal transport solutions.

2. As a logistics professional, I want to see updated features 

3.	As a logistics professional, professional I want to be able to contact Stack Smart Guide in case there are any issues with the calculator

_Frequent users_

1. As a logistics professional I want consistent and dependable results for freight planning

## Features

+ ### Navigation bar and Logo

    - Placed at the top of the page is the company logo "StackSmartGuide" on the left and also in the nav bar bottom left.
    - The navigation bar also has all the site pages (on mobile the nav bar changes to a dropdown burger icon )

    ![Nav bar](screenshots/logo.jpg)

---

+ ### Home page

    - Features: 

    ![Home Page](screenshots/landingpage.jpg)

        * Guide introduction with steps on how to use the pallet calculator 
        * Buttons to scroll to page sections
        * Form with inputs/ select options to collect data for vehicle recommendation 
        * Max and min amount notifications on the input options
        * Calculate button to show results based on user inputs and reset button to bring form back to its initial state and allow user to fill in new information 

---

+ ### Vehicle guide page

    - Features: 

    ![Vehicle guide Page](screenshots/vehicleguidepage.jpg)

        * Vehicle Cards showcasing images, van types, and classification
        * Technical Specs including volume capacity, payload limits, and vehicle dimensions.

---

+ ### Contact us page

    - Features: 

    ![Contact us Page](screenshots/contactuspage.jpg)

        * Contact Form requesting user details.
        * The form also includes a submit button to send user-provided contact information.

---

+ ### Contact us success page

    - Features: 

    ![Contact us success Page](screenshots/successpage.jpg)

        *  Confirmation Message thanking users for getting in touch and reinforcing that their inquiry was received.
        *  Return to Home” Button enabling  navigation back to the landing page.

---

+ #### Footer

    - Footer contains the stack smart guide logo and also social media links through icons so users stay connected.
​
    ![Footer](screenshots/footer.jpg)
​
---
## Technologies Used

- [If else statements](https://www.shecodes.io) - Used to Access Properties Inside an Object for If Else Statements
- [VSCode](https://code.visualstudio.com/)  Used as the main code editor
- [GitHub](https://github.com/) code host for the site
- [W3schools](https://www.w3schools.com/howto/howto_js_accordion.asp) - Used to assist with how to make a collapsable accordion.
- Code institute tutorials for understanding how to access elements in the DOM through JavaScript
---

### Solved bugs

1. Had an issue with the select options for the pallet types showing as strings despite the select type being a number. Rectified this by adding .value to the variable in JavaScript and listing the pallet size dimensions 

2. The site buttons were not working on the page when trying to add an event listener for clicks in a form. Resolved this by taking out the form tags and putting the form data in a div container instead.

3. The two buttons on the home page were not staying in one position when screen size changed so placed them in a div and used flex box 

### Testing

1. Deployed the site early so I could catch deployment specific bugs early 

2. Verified that all UI elements ( buttons, form inputs, accordion) operate as expected.

3. Confirmed vehicle recommendation logic runs correctly with varied pallet types, dimensions, and weight inputs.

4. Performed manual walkthroughs replicating real user scenarios—changing pallet types, submitting form, reading output.

5. Manually Tested website functionality by using the site as an end user. This involved entering various input combinations into the form fields, triggering the calculateTotal() function via the ‘Calculate’ button and ensuring that the vehicle recommendation output appeared correctly from the vanOutput element. 


### Unsolved bugs

1. On the vehicle guide page the main header is appearing lower than it should without any CSS at the start of the page and could not push it updwards by attempting to add margin. As the space at the top is only small I left the header as it is. 

---
## Design

### Color Scheme

![Color pallet](screenshots/color-pallete.jpg)

- The colour scheme for the site is blue, orange and white 

- Blue to instil user trust and convey reliability and professionalism so the site visitors feel assured about the accuracy of the information from the site. 

-	Orange to draw users’ attention to the logo and to highlight the vehicle recommendation output box 

- The white backgrounds make text and the site content clearer.

### Typography


- Chose open/public sans Google Font as they increase readability and clarity. Due to this it will be easy for users to scan through data and numerical values 

### Wireframes 

#### Mobile/Tablets/Desktop devices

- [Wireframe link](https://www.canva.com/design/DAGsg5tEPug/F1DLTwL4BDx1LUsQqJEtiQ/edit)

### Wireframe Reasoning 

1. The wireframe prioritizes clarity and usability, ensuring users can quickly understand the purpose of the Smart Pallet Calculator.

2. Input fields on the pallet calculator form/contant us page are logically grouped to guide the user through step-by-step data entry

3. The calculate and reset button on home page and submit button on contact us page are positioned to reinforce final action after data is entered

4. Images added on the vehicle guide page work as an aid to indicate vehicle sizes in each section 


---

## Testing

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

    ![XS devices](screenshots/xs-devices.jpg)

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

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |
| Pallet Data Form | | | | | |
| Number of pallets input | Enter number | number is displayed | Yes | Yes | - |
| Pallet height input | Enter number | number is displayed | Yes | Yes | - |
| Weight per pallet input | Enter number | number is displayed | Yes | Yes | - |
| Select pallet type | Select one of the 2 predifined pallet types  | pallet type is displayed | Yes | Yes | - |
| Buttons | | | | | |
| Calculate button | Click on the calculate button | An output of a vehicle recommendation is displayed | Yes | Yes | - |
| Reset button| Click on the reset button| The pallet data form refreshes all numbers entered by user are reset | Yes | Yes | - |
| Contact us Form | | | | | |
| First name input | Enter first name | first name is displayed | Yes | Yes | - |
| Last name input | Enter last name | last name is displayed | Yes | Yes | - |
| Email address input | Enter email address | email address is displayed | Yes | Yes | - |
| Message input | Enter message | message is displayed | Yes | Yes | - |
| Buttons | | | | | |
| Submit button | Click on the submit button | User redirected to contact us sucess page | Yes | Yes | User gets notification message received |
| Contact us sucess Page | | | | | |
| Return to home button | Click on the return to home button | User redirected to home page | Yes | Yes | - |
---

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

 No errors or warnings were found when passing through the JS code in JSHint. Only  warnings indicating that the version of JSHint does not support key word 'const' as  this is supported Javascript version ES6. 

   ![JSHint](screenshots/jshint.jpg)

---


## Deployment

### Deployment to GitHub Pages

- The site was deployed to GitHub pages. Using the following steps: 
  - In the [GitHub repository](https://github.com/MunasheMuk2/StackSmartGuide), clicked on the Settings tab.
  - Selected the main branch under default branch and clicked on code 
  - Under deployments was a ribbon display to indicate the successful deployment.

The live link can be found [here](https://munashemuk2.github.io/StackSmartGuide/).

### Local Deployment

In order to make a local copy of this project clone it in your IDE Terminal using the following command:

- `git clone https://github.com/MunasheMuk2/StackSmartGuide`


---

## Future improvements

Future development will focus on optimizing the functionality of the pallet calculator so it can calculate stackable pallets and provide vehicle recommendation based on manual length and width input. 

---

 #### Tools

    - [Favicon](https://favicon.io/favicon-converter/) generating an emoji fav icon 
    - [Canva](https://www.canva.com/) Wireframes created in canva
    - Used chatgpt and dev tools to test some of the Javascript code 
  
---

### Credits

All work done by myself - my two accounts MunasheMuk and MunasheMuk2 showing in error in git hub as contributors



## Acknowledgments

- [Code Institute](https://codeinstitute.net/) All slack community members willing to help at any time of the day. 

---