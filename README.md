This is a shopping website. A user can register user first and last name, username, email, password and profile picture. Then they can login using either email or username. After they have created a profile they can create a new item for selling. All items will be displayed and users can check the details and contact the creator of the post if they want or check their profile. Every user has an inbox where all conversations will be displayed. The user can click on whichever they want see conversation history and reply. In case a user is searching for something specific they can go to the search page and search based on word/description or category type. Furthermore, if a user forgot their password they can recover it. 

SUPERUSER:
USERNAME = martinstavrakov
EMAIL = martoo98ma@gmail.com
PASSWORD = 0987654321MS

RENDER_LINK = https://django-shop-project-owz0.onrender.com

GITHUB_LINK = https://github.com/m-stavrakov/Django-shop-project/tree/master

.env variables
SECRET_KEY=django-insecure-p+1l#gg9dd1^9$*mshi#-v7e&(713sam54d(*8)7qe6uh_07g9

# DEBUG=TRUE
DEBUG='False'

DATABASE_URL=postgresql://martinstavrakov:password@localhost:5432/online_shop_django

# DATABASE_URL = postgresql://online_shop_oe3h_user:Wnqg2VKKuiIgJ3N1gSjo5ixwI4zgVpjB@dpg-cpi20nq1hbls73baqdi0-a.frankfurt-postgres.render.com/online_shop_oe3h

EMAIL_USER='martoo98ma@gmail.com'

EMAIL_PASS='lygq misb xzdx jnol'

DJANGO_SUPERUSER_USERNAME="martinstavrakov"
DJANGO_SUPERUSER_EMAIL="martoo98ma@gmail.com"
DJANGO_SUPERUSER_PASSWORD="0987654321MS"
RENDER_HOST='django-shop-project-owz0.onrender.com'

#Personal note
Upon deploying the project on render I stumbled upon many issues. Most of them have been resolved, however there has been an issue with the superuser where I cannot access the admin page even when I provided the superuser username, email and password in Render. Furthermore, I could not use the user to login and when I tried signing up with the same user information it says that a user with that username already exists. It works localy however, even when I try using local database when on local server and Render database on Render the databssde on Render does not work. 
