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
├─ requirements.txt
├─ main.py                  # Application entry point
├─ README.md                # Project documentation
└─ app/
   ├─ routes.py             # API endpoints
   ├─ services.py           # Business logic
   └─ models.py             # Data models and schemas

```

## Running the Project with Docker

1. Docker Image has been built: `myapp:latest`.
2. Container is running with the application accessible on `http://0.0.0.0:8000`.
3. Environment variables are loaded from `.env` file inside the container.

Future Improvements:
- Extend API functionality if required

## Docker Concepts

### Docker Image
A Docker Image is a blueprint that contains everything required to run the application,
including the base operating system, Python runtime, dependencies, and application code.
An image does not run by itself.

### Docker Container
A Docker Container is a running instance of a Docker Image.
Multiple containers can be created from the same image.

Image → Blueprint  
Container → Running instance

## Dockerfile & Project Setup

A Dockerfile has been prepared according to Docker best practices.

It includes all necessary files for the project, including:

- main.py (application entry point)
- requirements.txt (Python dependencies)

A dedicated Docker branch was created in the repository to separate Docker-related work.

requirements.txt file has been created and verified for correctness.

## Building & Running the Container

The Docker image was successfully built locally using the following command:

docker build -t myapp:latest .

To run the container:

docker run -p 8000:8000 myapp:latest

The application runs inside the Docker container and is accessible via:

http://localhost:8000

A successful response was returned from the running container, confirming correct Docker setup.

## Conclusion

The Docker image has been successfully created using a valid Dockerfile and requirements file.

The project is now Docker-ready and can be executed inside a container environment on any compatible system.

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


## تسلسل العمل
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

6. Docker 

 استخدام Docker لتشغيل التطبيق داخل Container

هذا يضمن تشغيلًا ثابتًا وسهل النقل


## ملاحظات

هذا المشروع يركّز على التنفيذ الصحيح وليس التعقيد

أي ميزة إضافية يتم تنفيذها فقط إذا كانت مطلوبة رسميًا 

## شغيل المشروع باستخدام Docker

تم بناء Docker Image باسم: myapp:latest.

الحاوية تعمل الآن والتطبيق متاح على: http://0.0.0.0:8000.

تم تحميل Environment Variables من ملف .env داخل الحاوية.

## مفاهيم Docker

### Docker Image
صورة Docker هي مخطط يحتوي على كل ما يلزم لتشغيل التطبيق،
بما في ذلك نظام التشغيل الأساسي، بيئة Python، المكتبات الضرورية، وكود التطبيق.
الصورة لا تعمل بمفردها.

### Docker Container
حاوية Docker هي نسخة تشغيلية من صورة Docker.
يمكن إنشاء عدة حاويات من نفس الصورة.

الصورة → مخطط
الحاوية → نسخة تشغيلية

## ملف Dockerfile وإعداد المشروع
تم إعداد Dockerfile وفق أفضل ممارسات Docker.

يتضمن جميع الملفات اللازمة للمشروع، مثل:

main.py (نقطة تشغيل التطبيق)

requirements.txt (مكتبات بايثون المطلوبة)

تم إنشاء فرع خاص بالـ Docker في المستودع لفصل أعمال Docker عن بقية المشروع.

كما تم إنشاء ملف requirements.txt والتأكد من صحته.

##  بناء وتشغيل الحاوية

تم بنجاح إنشاء Docker Image محليًا باستخدام الأمر التالي:

docker build -t myapp:latest .

ولتشغيل الحاوية:

docker run -p 8000:8000 myapp:latest


ويعمل التطبيق داخل الحاوية ويمكن الوصول إليه من المتصفح عبر:

http://localhost:8000

تم التأكد من نجاح التشغيل من خلال استقبال استجابة صحيحة من التطبيق.


## الخلاصة
تم إنشاء Docker Image بنجاح باستخدام Dockerfile وملف المتطلبات بشكل صحيح.

أصبح المشروع الآن جاهزًا للتشغيل داخل حاوية Docker وعلى أي نظام يدعم Docker.

































