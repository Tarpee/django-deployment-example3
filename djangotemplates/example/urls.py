from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
     url(r'^data/$', views.DataPageView.as_view(), name='data'),
     url(r'^testfile/$', views.TestFilePageView.as_view(), name='testfile'),
     url(r'^$', views.HomePageView.as_view(), name='sample'),

      # hooking up sample button from the my first bootstrap page is done
      # by doing this  <li class="active"><a href="{% url 'sample' %}">Sample</a></li>
      # in the testfile.html then doing the last line on the urlpatterns observe 
      ]
