from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from courses.models import Course
from pure_pagination import Paginator, PageNotAnInteger


class CoursesListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-create_time")
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        orgs = p.page(page)

        return render(request, 'course-list.html',
                      {'all_courses': orgs,
                       'sort':sort,
                       'hot_courses':hot_courses})
