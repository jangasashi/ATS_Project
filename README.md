# 🚀 AI-Powered Applicant Tracking System (ATS) – Project Report

## 1. Project Name
**AI ATS Tool – Resume and Job Description Matcher**

## 2. Project Description
This AI-based Applicant Tracking System (ATS) project helps automate the resume screening process by matching resumes against job descriptions and providing a match score. It replicates a simplified version of real-world ATS platforms like Greenhouse or Taleo, but customized for educational, prototype, or small business use cases.

Users can:
- Sign up and log in
- Upload resumes and job descriptions
- View real-time match scores

Match results are stored in a local SQLite database, allowing users to view historical match data.

## 3. My Role
I served as the **sole developer and architect** of this project. My responsibilities included:
- Designing the application structure and user flow using **Streamlit**
- Implementing **user authentication** (Login/Signup)
- Creating **resume and job description input functionality**
- Building **resume-to-job description matching logic** using NLP and similarity scoring
- Integrating a **local SQLite database** to store users and match history
- Ensuring smooth integration between **UI and backend**

## 4. Tools & Technologies Used

- **Programming Language**: Python  
- **Frontend**: Streamlit  
- **Backend**: Python, SQLite3  
- **Libraries**:
  - `difflib` (SequenceMatcher) – for match scoring logic
  - `PyPDF2` – for reading resume PDFs
  - `sqlite3` – for database management
  - `os`, `datetime` – for file handling and timestamps  
- **Folder Structure**: Modular Python files:
  - `app.py`
  - `auth.py`
  - `database.py`
  - `matcher.py`
  - `parser.py`
  - `email_handler.py`
  - `utils.py`

## 5. Key Features Implemented
- 🔒 User authentication (login/signup)
### 🔐 Login Page
![Login Screenshot](https://github.com/user-attachments/assets/0e464100-4f41-45c4-b931-65fa949cf469)

- 📄 Resume upload functionality (.pdf format)
![Upload Resume](https://github.com/user-attachments/assets/3098767d-7545-4231-a18e-c1b6c2fb5192)

- 📝 Job description input via text
![Job Description](https://github.com/user-attachments/assets/9a45f05d-555d-4a69-b13a-d57c5b2deea9)

- 📊 Real-time resume-to-JD matching with percentage scores
![Matching Result](https://github.com/user-attachments/assets/6cff1a72-edf6-43c1-a246-cafe5f1ff917)

- 🧾 Match history logging with timestamps
![Match History](https://github.com/user-attachments/assets/3847087d-eb85-43f3-96fd-c46300cfae6a)
- 📁 Organized folder structure

## 6. Challenges Faced & Solutions

- **PDF reading delays**: Solved by allowing direct text input for job descriptions  
- **Match result logging**: Fixed missing parameters and adjusted database schema  
- **Database errors (no such table)**: Solved by calling table creation functions on app startup  
- **Modular file confusion**: Simplified and cleaned up the structure for better maintenance

## 7. Conclusion
This ATS project demonstrates how a solo developer can build a functional AI-driven web application using Python and Streamlit. It is ideal as a prototype for extending with:
- Advanced NLP models like spaCy or BERT
- Cloud-based storage
- Role-based dashboards

It reflects **end-to-end project development**, **problem-solving**, and **hands-on AI integration**.

