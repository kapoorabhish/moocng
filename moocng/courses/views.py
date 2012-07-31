from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from moocng.courses.models import Course


def home(request):
    return render_to_response('courses/home.html', {
            'courses': Course.objects.all(),
            }, context_instance=RequestContext(request))


def course_overview(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)

    return render_to_response('courses/overview.html', {
            'course': course,
            }, context_instance=RequestContext(request))


def course_classroom(request):
    pass


def course_progress(request):
    pass