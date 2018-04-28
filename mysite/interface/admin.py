from django.contrib import admin
from .models import Course,Chapter,Department,Material


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 0

class CourseInline(admin.TabularInline):
    model = Course
    extra = 0

class MaterialInline(admin.TabularInline):
    model = Material
    extra=0

class Filter0(admin.ModelAdmin):
    inlines = [
        CourseInline
    ]

class Filter(admin.ModelAdmin):
    #list_display = ('title','department',)
    list_filter = ('department',)
    search_fields = ('title',)
    ordering = ('title',)
    inlines = [
        ChapterInline
    ]
class Filter1(admin.ModelAdmin):
    #list_display = ('chapter_title','course',)
    list_filter = ('course',)
    search_fields = ('chapter_title',)
    ordering = ('chapter_title',)
    inlines = [
        MaterialInline
    ]
class Filter2(admin.ModelAdmin):
    #list_display = ('name','chapter',)
    list_filter = ('chapter',)
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Department,Filter0)
admin.site.register(Material,Filter2)
admin.site.register(Course,Filter)
admin.site.register(Chapter,Filter1)
