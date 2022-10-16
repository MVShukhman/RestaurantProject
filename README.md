# RestaurantProject
<h2>Installation</h2>
1. Build images <br>
  <code>docker-compose build</code> <br>
2. Run server <br>
  <code>docker-compose up -d</code> <br>
3. Make migrations <br>
  <code>docker-compose exec web python manage.py migrate</code> <br>
4. Create a superuser for django admin <br>
  <code>docker-compose exec web python manage.py createsuperuser</code> <br>
<strong><h3>Note: this is debug-only configuration!</h3></strong>

<h2>Usage</h2>
1. Admin's page for editing data <br>
<code>http://0.0.0.0:8000/admin</code>
2. Food items marked as publish grouped by categories <br>
<code>http://0.0.0.0:8000/api/v1/food</code>
