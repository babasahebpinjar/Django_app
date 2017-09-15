https://www.slideshare.net/skabber/introduction-to-django-presentation?next_slideshow=1


https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK

1.	Install python
2.	easy_install --version
(
	https://bootstrap.pypa.io/ez_setup.py
	save it and run it using python
	i.e python ez_setup.py
)

3.	easy_install django==1.9(for specific version)
	or 
   	easy_install django

   	To check if django is installed properly

	django-admin --version

4.	To start a project
	django-admin startproject SecureLogin (Name of the folder doesn't matter at all, files inside it matter)

5.	manage.py - Never edit this file
	init.py - tells python to view it as a package
	
	
6.	python manage.py runserver in cd SecureLogin
	To start the server, go to browser and type http://localhost:8000/

7. 	python manage.py startapp Applications

	
8.	Database, it comes with default database sqlite

9.	When you do some changes in Applications, make sure you sink it with  db,

	python manage.py makemigrations Aplications
	python manage.py sqlmigrate Applications 0001(0001 is the code you get after executing the above command)
	python manage.py migrate

 
10.	python manage.py shell(to insert values into DB)
	sql>>

		windowsApp.objects.all()
		a = windowsApp()
		a.appName = "wassup"

		a.save()
		a.id
		q.pk

		windowsAp.objects.filter(id=1)
		windowsAp.objects.filter(username__startswith="was")


