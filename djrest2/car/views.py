from djrest import ListCreateView

from car.custom_response import OrJsonResponse
from car.forms import CarForm
from car.models import Car


class Cars(ListCreateView):
    model = Car
    form_class = CarForm

    def get_queryset(self):
        return Car.objects.with_annotations()


class CarsOrJson(ListCreateView):
    model = Car
    form_class = CarForm
    response_class = OrJsonResponse

    def get_queryset(self):
        return Car.objects.with_annotations()
