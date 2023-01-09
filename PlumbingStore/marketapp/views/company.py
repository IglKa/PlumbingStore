from django.views import View

from .company_detail import CompanyDetail
from .follow_company import FollowCompany


class CompanyPageView(View):
    def get(self, request, *args, **kwargs):
        view = CompanyDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = FollowCompany.as_view()
        return view(request, *args, **kwargs)
