=====
Pictures
=====

Pictures is a Django app to list and add pictures.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "pictures" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pictures',
    ]

2. Include the pictures URLconf in your project urls.py like this::

    path('pictures/', include('pictures.urls')),

3. Run ``python manage.py migrate`` to create the pictures models.

4. Visit http://127.0.0.1:8000/pictures/ to list and add pictures.
