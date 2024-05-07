The APIs above created are for an Ecommerce platform. We have CRUD operations for products, users and orders being processed. Along with that we have used Integrated Filtering, sorting and ordering using django-filters
library. To start with the program:
1) Clone the repo
2) pip3 install -r requirements.txt
3) python manage.py makemigrations
4) python manage.py migrate

After these steps, you need to create a superuser so you can generate an access token and a refresh token as these JWT tokens will give you access to other endpoints
To create a superuser(staff member), run the following command: *python manage.py createsuperuser*. Fill the upcoming prompts and you are now a superuser.
To create a normal user, go to the /register/ endpoint and add your username and password which are the required fields. First_name, last_name, address, phone are optional fields.

A normal user can only view the products, where as a superuser or a staff member can view, add, delete and update the products.
A staff member or a superuser can place order for others users and themselves whereas, a normal user can place order for themselves only.

After this, you can run the following command: *python manage.py runserver*, click on the URL which comes in the terminal and open it. Once thats open visit, */api/token/* and enter the username and password you
created to generate the access and refresh tokens. Be mindful that the access token is valid for 30 mins and refresh token is valid for a day. Once the access token expires, go to
*/api/token/refresh* endpoint and paste the refresh token you received earlier, to get your new access token. 

All the below endpoints can be accessed only if you have an access token and through postman. The token needs to be pasted under the Auth tab, under the Bearer Token Auth Type.
1) **/users/** (GET, POST). For POST, in the body you have to pass username, password, first_name, last_name as required fields. Email, address and phone are optional fields. Users can be searched by using username, first_name, last_name, phone or address. For example, **GET /users/?search=john**
2) **/users/pk/** (GET, UPDATE, DELETE). For update, you can pass the fields you want to update.
3) **/products/** (GET, POST). For POST, you have to pass name, description and price as the fields to create a product in the database. Products can be searched using name or description.
4) **/products/pk/** (GET, UPDATE, DELETE). For UPDATE, pass the field you want to update.
5) **/orders/** (GET, POST). For POST, pass {"customer": id, "items": [{"product": id, "quantity": int}]}. Orders can be searched using username of the user who wants the order, total_price or products
6) **/orders/pk/** (GET, POST, DELETE). For update, pass the field you want to update.

pk: Primary key

Searching Syntax: **GET /users/?search=john**

Ordering Syntax: **GET /orders/?ordering=-total_price**

Filtering Syntax: **GET /products/?name=shirt&price_min=10&price_max=50**
