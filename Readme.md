# Vehicle Showroom & Content Management System (Django Backend)

This is a Django-based backend for a Vehicle Showroom & Content Management System.  
It supports user authentication, blog & showroom content handling, and full vehicle lifecycle management — including categories, variants, and pricing. Designed with modular APIs and OpenAPI documentation (Swagger/ReDoc) for seamless frontend integration.

## Use Case

- A platform where **admins** can manage users and post blogs/showroom content.
- **Users (or buyers)** can:
  - Browse vehicles by category
  - View different variants
  - See detailed pricing

This system can also serve as the backend for a **vehicle dealership web app or mobile app**.

### modules

AUTH
-------
✅ Login & Authentication (Token Refresh, Verify, Login)
✅ User Profile (List All Users, Get User by ID)
✅ Admin User Management (Create, Update, Delete)

CONTENT
---------
✅ Blogs (List, Create, Update, Delete)
✅ Showrooms (List, Create, Update, Delete)

VEHICLE
----------
✅ Category Management (Create, Update, Delete, List)
✅ Vehicle Management (Create, Read, Update, Delete)
✅ Variant Management (Color & Image Category)
✅ Vehicle Pricing (Different Spec Types & Prices)


Backend developers test the API without Postman or curl SWAGGER UI can use


Swagger UI is interactive:
You can send requests like GET, POST, PUT, DELETE directly from the browser.

🔧 Test how your endpoints behave with different:

Parameters

Headers (like Authorization tokens)

Request bodies (JSON data)

ReDoc UI is more of a viewer:
It gives a clean and readable reference for your API endpoints, models, and expected inputs/outputs.

Raw JSON/YAML spec is used with external tools or for sharing your API design with others.


Testing & Exploring APIs 
|||----------------------------|||
Swagger UI: http://localhost:8000/swagger/

ReDoc UI: http://localhost:8000/redoc/

Raw schema: http://localhost:8000/swagger.json

