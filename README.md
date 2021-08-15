# ⚙️⛓️ THE VAULT ⛓️⚙️

A Django web app that is optimized for a specific inventory tracking system.

Startup Django App Basics for who the code is intended:
---
+ Open your command terminal
+ `cd` into the root folder `.../The-Vault-App-main`.
+ We first need to migrate the models with `python manage.py makemigrations`.
+ Then `python manage.py migrate`.
+ Run the server locally for personal use `python manage.py runserver`.
+ Localhost will take you instantly to the frontend at URL `.../products/`.
+ Before you get into the backend you need to create a superuser with `python manage.py createsuperuser`.
+ Now to get into the backend change the URL to the admin portal at `.../admin/`.
+ Here you will find the interface you will use to interact with the database and imput the product data.
+ Anything you imput in the `.../admin/` backend will then be displayed visually in the `.../products/` frontend.

