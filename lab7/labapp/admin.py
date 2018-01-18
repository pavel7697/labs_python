from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #fields = ('first_name', 'last_name')
    list_display = ('username','full_name','age','has_reviews',)
    list_filter = ('age',)
    search_fields = ['last_name', 'first_name']

    def full_name(self, obj):
        return "{} {}".format(obj.last_name, obj.first_name)

    def username(self, obj):
        return "{}".format(obj.user.username)

    # def has_reviews(self, obj):
    #     hs = Review.objects.filter(user=obj)
    #     return len(hs)>0


@admin.register(Pulpit)
class PulpitAdmin(admin.ModelAdmin):
    list_display = ('name','year','zav','info',)
    list_filter = ('year',)
    search_fields = ['name', 'info', 'zav']
    empty_value_display = '-empty-'

    def pulpit_name(self, obj):
        return "{} - {}".format(obj.pulpit.name, obj.pulpit.info)

@admin.register(Teacher)
class PulpitAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'phone', 'mail', 'description',)
    list_filter = ('second_name', 'name')
    search_fields = ['name', 'second_name']
    empty_value_display = '-empty-'

    def teacher_name(self, obj):
        return "{} {} {}".format(obj.second_name, obj.name, obj.third_name)

    def teacher_info(self, obj):
        return "{} {} {}".format(obj.teacher.phone, obj.teacher.mail, obj.teacher.description)
# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     empty_value_display = '-empty-'

@admin.register(Membership)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('teachername', 'pulpitinfo',)
    empty_value_display = '-empty-'

    def teachername(self, obj):
        return "{} {} {}".format(obj.teacher.second_name, obj.teacher.name, obj.teacher.third_name)

    def pulpitinfo(self, obj):
        return "{} - {}".format(obj.pulpit.name, obj.pulpit.info)