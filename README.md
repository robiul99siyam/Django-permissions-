
# Django permissions
This repository provides an overview and examples of how to use permissions in Django, a high-level Python web framework.


# Overview
In Django, permissions are used to control access to views and data within your web application. They determine whether a user is allowed to perform a certain action, such as viewing a page, editing content, or deleting records.

# Types of Permissions
Django provides three types of permissions out of the box:

Model-level Permissions: These permissions are associated with individual models and control access to database objects. They include:

add: Permission to create new objects.
change: Permission to modify existing objects.
delete: Permission to remove objects.
Object-level Permissions: These permissions are used to control access to specific instances of models. They allow fine-grained control over who can access individual objects based on custom logic.

View-level Permissions: These permissions are applied at the view level and determine whether a user is allowed to access a particular view or API endpoint.

# Permission Classes
In Django REST Framework (DRF), permissions are implemented using permission classes. These classes define the logic for determining whether a user has the necessary permissions to access a view or perform a specific action.

# Usage
Setting Permissions
Permissions can be set at the model level using the permissions attribute in a Django model's Meta 
