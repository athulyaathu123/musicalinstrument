from .models import Cart


def cart_count(request):
    if request.user.is_authenticated:
        cnt=Cart.objects.filter(user=request.user,status="cart").count()
        return{"count":cnt}
    else:
        return {"count":0}
    