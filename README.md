## Unified AI Service

Unified AI Service is a simple backend application that provides AI-powered services through a RESTful API.
It allows clients to send requests and receive responses in JSON format.

This project demonstrates proper backend development practices, including Git workflow, RESTful API design, clean code structure, and Docker-based deployment.

## Project Objectives

Build a working RESTful API using FastAPI

Apply proper Git and GitHub workflow (branches, commits, merges)

Ensure clean, readable, and maintainable code

Prepare the application for containerized deployment using Docker

## Development Workflow (Step by Step)
1. Project Initialization

Created the project locally using PyCharm

Initialized a Git repository

Created a GitHub repository

Added an initial README file

2. Git & GitHub Workflow

Used main branch as the stable branch

Created feature branches for new functionalities

Committed changes with clear and descriptive commit messages

Merged feature branches into main using proper merge strategy

3. Backend Development (FastAPI)

Built a simple backend service using FastAPI

Implemented RESTful API principles

Ensured the service runs successfully

4. API Features

Implemented HTTP methods:

GET

POST

Used proper HTTP status codes:

200 OK

400 Bad Request

422 Unprocessable Entity

500 Internal Server Error

Used JSON format for requests and responses

Added input validation

Implemented error handling to prevent crashes

5. Clean Code & Project Structure

Separated concerns between routes, services, and models

Used clear and meaningful names

Kept functions small and focused

6. Docker (Next Step)

Docker will be used to containerize the application

This ensures consistent and repeatable deployment across environments


## Features

RESTful API with GET and POST methods

Input validation and error handling

Clean and organized code structure

GitHub-based development workflow

Docker-ready backend service

## Structure 
```
unified-ai-service/
│
├─ main.py                  # Application entry point
├─ README.md                # Project documentation
└─ app/
   ├─ routes.py             # API endpoints
   ├─ services.py           # Business logic
   └─ models.py             # Data models and schemas

```
## Running the Project (Without Docker)

Clone the repository

Install required dependencies

Run the FastAPI application

Open:

http://127.0.0.1:8000/docs for API documentation

## Future Improvements

Complete Docker containerization

Add environment variables

Extend API functionality if required


###________________________
##_________________________

## خدمة Unified AI 

هو تطبيق Backend بسيط يوفّر خدمات عبر واجهة RESTful API

يسمح للتطبيقات الأخرى بإرسال طلبات واستلام ردود بصيغة JSON.

يهدف هذا المشروع إلى تطبيق مفاهيم تطوير الخلفية بشكل صحيح، مع استخدام Git و GitHub وتنظيم الكود وتشغيل الخدمة داخل Docker.

## أهداف المشروع

بناء RESTful API يعمل فعليًا باستخدام FastAPI

تطبيق أسلوب عمل صحيح باستخدام Git و GitHub

كتابة كود نظيف ومنظّم وقابل للتطوير

تجهيز التطبيق للتشغيل باستخدام Docker 


##تسلسل العمل
1. إنشاء المشروع

إنشاء المشروع محليًا باستخدام PyCharm

تهيئة Git Repository

إنشاء مستودع على GitHub

إضافة ملف README مبدئي

2. استخدام Git و GitHub

استخدام فرع main كفرع رئيسي

إنشاء فروع مستقلة (Feature Branches) لكل ميزة

كتابة Commit Messages واضحة

دمج الفروع مع main بطريقة صحيحة

3. تطوير الـ Backend

بناء خدمة Backend باستخدام FastAPI

التأكد من أن الخدمة تعمل فعليًا

الالتزام بمبادئ RESTful API

4. خصائص الـ API

استخدام GET و POST

التعامل مع Status Codes بشكل صحيح

إرسال واستقبال البيانات بصيغة JSON

التحقق من صحة المدخلات (Validation)

معالجة الأخطاء بدون انهيار التطبيق

5. تنظيم الكود

فصل المسارات (Routes) عن المنطق (Services)

استخدام أسماء واضحة

جعل الكود سهل القراءة والصيانة

6. Docker (الخطوة القادمة)

سيتم استخدام Docker لتشغيل التطبيق داخل Container

هذا يضمن تشغيلًا ثابتًا وسهل النقل


## ملاحظات

هذا المشروع يركّز على التنفيذ الصحيح وليس التعقيد

أي ميزة إضافية يتم تنفيذها فقط إذا كانت مطلوبة رسميًا 



































