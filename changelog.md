# OoB (Order-of-Business) ChangeLog

## v0.1.0

### Models

- [x] Core Models
  - [x] User
- [x] Oob App Models
  - [x] Task
  - [x] Project
  - [x] Section
  - [x] Tag

### Views

- [x] Core Views
  - [x] Landing
  - [x] Login
  - [x] Register
- [ ] Oob App Views
  - [x] Home
  - [x] Inbox
  - [x] Project
  - [x] Calendar
  - [x] Create New Task
  - [x] Create New Project
  - [ ] Create New Section

### Forms

- [ ] Core Forms
  - [x] Register
- [ ] Oob App Forms
  - [x] Create New Task
  - [x] Create New Project
  - [ ] Create New Section

### Templates

- [ ] Core Templates
  - [x] base.html
  - [ ] login.html
  - [ ] register.html
- [ ] Oob App Templates
  - [x] user_navbar.html
  - [ ] user_home.html
  - [ ] user_inbox.html
  - [ ] user_project.html
  - [ ] user_calendar.html

### Tests

- [ ] Models
  - [ ] Task
  - [ ] Project
  - [ ] Section
  - [ ] Tag
  - [ ] User
- [ ] Views
  - [ ] Landing Page
  - [ ] Login
  - [ ] Register
  - [ ] User Home
  - [ ] User Inbox
  - [ ] User Projects
  - [ ] User Calendar
  - [ ] User Add Task
  - [ ] User Add Project
  - [ ] User Add Section
  - [ ] User Logout

### Add-Ons & Mix-Ins

- [ ] Mix-Ins
- [ ] Decorators
  - [x] anonymous_user: only allow access if the user is not logged in
- [ ] Context Processors
  - [x] user_context: sends extra context to logged in users for Navbar functionality

### Project Organization

- [ ] Separate core and OoB app code
- [ ] Comment all necessary code
