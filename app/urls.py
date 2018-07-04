"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from helpers.no_put_router import NoPutRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from . import views

# main modules
from unit.api.views import UnitViewset
from user.api.views import UserViewset
from certificate.api.views import CertificateViewset
from skill.api.views import SkillViewset
from portfolio.api.views import PortfolioViewset
from detail_skill.api.views import DetailSkillViewset, UserDetailSkillViewset
from education.api.views import EducationViewset, MajorViewset, UserEducationViewset
from video.api.views import VideoViewset

# change admin page title
admin.site.site_header = 'DumbWays Alumni Api'

swagger_view = get_swagger_view(
    title=admin.site.site_header
)

# router = routers.DefaultRouter()
router = NoPutRouter()

# main routers
router.register('unit', UnitViewset)
router.register('user', UserViewset)
router.register('certificate', CertificateViewset)
router.register('skill', SkillViewset)
router.register('portfolio', PortfolioViewset)
router.register('detail-skill', DetailSkillViewset)
router.register('user-detail-skill', UserDetailSkillViewset)
router.register('user-education', UserEducationViewset)
router.register('education', EducationViewset)
router.register('major', MajorViewset)
router.register('video', VideoViewset)

urlpatterns = [
    path('', swagger_view),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/authentication/', obtain_jwt_token),
    path('api/version/', views.version),
]
