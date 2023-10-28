from django.db import models


class Year(models.Model):
    year = models.CharField(max_length=50)

class Team(models.Model):
    year = models.ForeignKey(Year, on_delete = models.CASCADE)
    team = models.CharField (max_length=50) #팀명
    p_name = models.TextField() #프로젝트 이름
    

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete= models.CASCADE) #팀
    name = models.CharField(max_length= 50) #이름
    m_id =  models.IntegerField()  #나이 primary_Key 이슈로 id를 m_id로 변경/ 학번
    major = models.CharField(max_length= 50) #전공

class Info(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    madeby = models.ForeignKey(Member, on_delete= models.CASCADE)
    # planning_background = models.TextField()
    # problem_define = models.TextField()
    # service_info = models.TextField()
    # funtion  = models.ForeignKey(Function, on_delete = models.CASCADE)
    # main_technology = models.ForeignKey(Technology, on_delete = models.CASCADE)

class Photo(models.Model):
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    index = models.IntegerField()
    photo = models.ImageField(upload_to="")     #여기에 기능설명 및 프로젝트에 대한 설명들이 스크린 샷으로 들어갈 예정


#  주석처리된 부분은 향후 관리자페이지로 들어가 글을 작성하는 기능을 만들 경우 Info테이블에 넣을 것들이다(현재는 photo에 이 내용이 다 들어갈 예정) 

# class Technology(models.Model):
#     team =models.ForeignKey(Team, on_delete=models.CASCADE)
#     explain = models.TextField()

# class Function(models.Model):
#     team = models.ForeignKey(Team, on_delete= models.CASCADE)
#     explain = models.TextField()

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class TestEntity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_entity'


class TestEntitySeq(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_entity_seq'

