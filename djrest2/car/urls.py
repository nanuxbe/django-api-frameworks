from django.urls import path

from car.views import Cars, CarsOrJson

urlpatterns = [
    path("cars-json/", Cars.as_view()),
    path("cars-orjson/", CarsOrJson.as_view()),
]

# For load-testing
urlpatterns += [
    path("cars/", Cars.as_view()),
]
