from django.urls import path
#se importa las vistas asi debido 
#a que es mas facil de visualizar 
# en pantalla dividida
from .views import HomePageView,AboutPageView
from .views import ContactPageView,ProductIndexView
from .views import ProductShowView,ProductCreateView
from .views import CartView,CartRemoveAllView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/',ContactPageView.as_view(), name='contact'),
    path('product/', ProductIndexView.as_view(), name='index'),
    path('product/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), 
]