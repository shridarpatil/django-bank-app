"""Bank."""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bank_data.models import Branch
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
def branch(request):
    """Bank."""
    # Bank(id=1, name='IDFC').save()

    ifsc = request.GET.get('ifsc')
    bank_name = request.GET.get('name')
    city = request.GET.get('city', None)
    if ifsc:
        try:
            x = Branch.objects.get(ifsc=ifsc)
            data = {
                'ifsc': x.ifsc,
                'branch': x.branch,
                'address': x.address,
                'city': x.city,
                'district': x.district,
                'state': x.state
            }
        except ObjectDoesNotExist:
            data = {}
    elif city and bank_name:
        x = Branch.objects.filter(bank_id__name=bank_name, city=city)
        data = []

        for y in x:
            data.append(
                {
                    'ifsc': y.ifsc,
                    'branch': y.branch,
                    'address': y.address,
                    'city': y.city,
                    'district': y.district,
                    'state': y.state
                }
            )
    else:
        data = {}

    return Response({"data": data})
