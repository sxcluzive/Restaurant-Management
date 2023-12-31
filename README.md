﻿# food ordering system
Django project that implements a RESTful API for managing a food ordering system. Below is a brief explanation of the code:

1. Models (`models.py`):
   - There are four models defined in the code: `Category`, `MenuItem`, `Cart`, and `Order`.
   - `Category` represents food categories, such as "Appetizers," "Main Courses," etc.
   - `MenuItem` represents individual food items with attributes like `title`, `price`, `featured`, and a foreign key relationship to the `Category`.
   - `Cart` represents a user's cart with items they have added, related to both the `User` and `MenuItem` models.
   - `Order` represents an order placed by a user, including details like `user`, `delivery_crew`, `status`, `total`, and `date`.

2. Serializers (`serializers.py`):
   - Serializers are used to convert complex data types (e.g., models) to JSON data and vice versa.
   - There are serializers defined for `Category`, `MenuItem`, `User`, `Cart`, `Order`, and `OrderItem`.

3. Views (`views.py`):
   - The views are implemented using Django's generic views and custom APIViews to handle HTTP requests for various endpoints.
   - The views support actions like listing and creating categories, menu items, and orders.
   - There are custom views for managing managers, delivery crew members, and user carts.

4. Permissions and Authentication:
   - The project uses Django's built-in authentication system, and some views have permissions set to restrict access to authenticated users only.
   - A custom permission class `IsManagerOrSuperUser` is implemented for specific actions that require manager or superuser access.

5. Filtering and Search:
   - The views use filtering and search capabilities provided by the Django Rest Framework (DRF) to allow clients to filter menu items and orders based on specific criteria.

6. Other Features:
   - The code includes some data validation using the `bleach` library to clean input data before saving it to the database.
   - The `PartialOrderSerializer` is a specialized serializer for partial updates to orders.

