from core.models import CompanyInfo

def company_info_processor(request):
    return {
        'company_info': CompanyInfo.objects.first()
    }