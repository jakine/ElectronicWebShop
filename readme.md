# Electronic web shop

Ecommerce website build in Django where user can log in and buy ittems.
User can add an item many times, and comes back the added items will still be in the basket. Other than that user can remove items too.




Data structure.
We have Customer, Product, Order, OrderItem and Shipping address models that will be inserted in SQLite database of the project.
Models controll the database, Ajax JS to handle the request submission from the user such as quantity of the items, or adding/removing in the chart and Bootstrap CSS for design.



<h3> On going steps </h3>
[X]  Design using boostrap <br>
[X]  Models and database migrations <br>
[X]  Generating product list dynamic from database <br>
[X]  Creating a User/Customer by login signup <br>
[X]  Adding Order in the database of the User <br> 
[X]  Adding multipule Order in the User database <br>
[X]  Check out properties, Event Handling <br>
[X]  Shipping Address <br>
[ ]  Payment validation <br>
[ ]  Filter based on categories <br>



Categories list, and each product is appeared based on the category it belongs.

So far --> 

Store demo:
<img src="screenshot.png" alt="">


Order Cart checkout:
<img src="orderitems_total.png" alt="">


Shipping & Payment checkout:
