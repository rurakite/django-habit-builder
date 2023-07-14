<i class="bi bi-train-front-fill"></i>HABITRAIN

Habitrain is a habit tracking and management tool designed to help individuals cultivate positive habits, eliminate harmful ones, and enhance their overall well-being. With its user-friendly interface and comprehensive features, Habitrain empowers users to set goals, track progress, and stay motivated on their journey towards personal growth and self-improvement. The live link can be found here: https://habitrain-923cabcbe865.herokuapp.com/

User-Experience-Design

Site-Goals

The primary goal of the Habitrain site is to provide users with a robust platform for tracking and managing their habits effectively. Users should be able to create, edit, and track their habits, record daily progress, and view comprehensive statistics to monitor their habit performance.

The site aims to offer a user-friendly and intuitive experience, ensuring that users can navigate the application easily and access the features and information they need without any confusion or complexity. The interface is visually appealing, responsive, and optimized for various devices.

Certainly! Here's an example of a UX design for the Habitrain application:

**Home Page**
- The home page features a clean and modern design with a hero image background that reflects the idea of an application - the locomotive, symbolizing progress, momentum, and the journey of building and maintaining habits.
- A prominent call-to-action button invites new users to register and join the Habitrain.
- The navigation menu is minimalistic and easy to navigate, providing links to login and signin.


**Registration Page**
- The registration page features a user-friendly form with clear labels for each input field.
- Inline validation provides real-time feedback on the validity of the entered information.
- Upon successful registration, users are redirected to the login page.
- If the user already has an account, the link will redirect them to the login page to access their existing account.

**Login Page**
- The login page presents a clean and intuitive design with a login form prominently displayed.
- The input fields for username and password are designed with a clean and intuitive layout, making it easy for users to enter their login credentials.
- An option to register is available for new users who haven't created an account yet.

**Dashboard Page**
- The dashboard offers a visually appealing and organized layout with a fixed top navigation bar and offcanvas side bar.
- This design ensures a consistent and seamless user experience, especially on larger screens where the side bar remains visible at all times.
- An animated card displaying motivational text is prominently featured on the dashboard. This dynamic element adds a touch of inspiration to the user experience.
- A weather widget has been integrated into the dashboard, providing users with up-to-date weather information at a glance. 
- The dashboard includes a dynamic table that allows users to instantly add habits with the help of asynchronous HTMX technology. The header provides users with important information, including the current day, date, and week number as well as a bright plus button, which serves as an intuitive and eye-catching element for adding new habits.
- By clicking on the plus button, a modal pop-up window appears, presenting the user with a habit creation form. Within this form, users can input essential details such as the habit's title, description, and select a type from preinstalled categories, specify the start and end dates for the habit, allowing them to set a duration or timeframe for their habit tracking.
- The table view provides users with a clear and comprehensive overview of dates and weekdays. When a new habit is created, the backend automatically generates daily records based on the specified timeframe. The intuitive checkbox system allows users to easily monitor their daily habits, making it simple to identify which habits have been completed and which are still pending. In case when a daily record does not match the corresponding date the app logo will appear.
- Progress bars indicate the completion status of each habit during a week for quick visual assessment.
- Users can easily navigate to specific habit details or take actions such as editing or deleting habits. And a same pop up modal will help to push any updates.
- Success messages or notifications confirm the successful creation of the habit as well as update and delete.

**View Habits Page**
- When a user visits the page without having created any habits, a friendly and encouraging message is displayed along with a prompt to take action and start adding habits.
- The page presents a visually pleasing and well-organized grid-view of the user's habits.
- Habit card provides a snapshot of each habits details, including title and description. 
- At the footer of each habit card, users will find two buttons that provide additional functionality and information related to the habit.
- The "Edit" button, represented by a gear icon. When clicked, it opens a modal where they can update the habit's details such as title, description, category, and time frame. 
- The "Daily Records " button, represented by a text. This button allows users to access a modal that displays all the daily records created for the specific habit, showing the dates and completion status for each day.

**Statistics View (statistics.html):**
- The statistics view provides a visually appealing representation of habit-related data and insights.
- Users can select a specific date or time period to view corresponding statistics.
- Clear labels and tooltips aid in understanding the displayed data.
- Navigation or filtering options allow users to explore different views or compare data.

**User Profile View (user-profile.html):**
- The user profile page showcases the user's profile information and settings in a well-structured layout.
- Personal details, such as name, email, and profile picture, are prominently displayed.
- Users can easily update their profile information, change their profile picture, or modify account settings.
- Navigation links or tabs provide access to additional profile sections, such as password change or privacy settings.

**User Profile Update View (user-profile-update.html):**
- The user profile update view features a form pre-filled with the user's existing profile information.
- Users can make changes to their personal information, profile picture, or other relevant details.
- Real-time validation ensures accurate and valid data entry.
- Success messages or notifications confirm the successful update of the user's profile.

**Daily List View (daily-list.html):**
- The daily list view presents a comprehensive list of daily tasks or habits.
- Each daily task is displayed with relevant information, including the habit title, completion status, and date.
- Visual indicators or icons highlight completed tasks for easy recognition.
- Users can mark tasks as completed or undone with a single click or tap.



**Error Pages (400.html, 403.html, 404.html, 500.html):**
- Error pages feature a consistent design and layout to maintain a seamless user experience.
- Clear and user-friendly error messages explain the encountered issue.
- Links or navigation options are provided to guide users back to functional pages or to relevant support resources.

Remember to customize the UX design to match your application's branding, color scheme, and visual style. The examples provided here are for illustration purposes and can be further enhanced based on your specific design preferences and target audience.

- Key statistics, such as the number of completed habits, ongoing habits, and overall progress, are displayed prominently.
- Habit cards are presented in a grid or list format, showcasing the habit title, category, and completion status.