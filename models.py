# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class ClasificacionesResiduos(models.Model):
    id_clasificaciones_residuos = models.AutoField(primary_key=True)
    id_clase = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clasificaciones_residuos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Familias(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familias'


class Laboratorios(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    nombre_laboratorio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios'


class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_laboratorio = models.ForeignKey(Laboratorios, models.DO_NOTHING, db_column='id_laboratorio')
    fecha = models.DateField(blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'movimientos'


class MovimientosDetalle(models.Model):
    id_movimiento_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id_reactivo = models.ForeignKey('Reactivos', models.DO_NOTHING, db_column='id_reactivo', blank=True, null=True)
    id_tipo = models.ForeignKey('TiposMovimientos', models.DO_NOTHING, db_column='id_tipo')
    id_residuo = models.ForeignKey('Residuos', models.DO_NOTHING, db_column='id_residuo', blank=True, null=True)
    id_movimiento = models.ForeignKey(Movimientos, models.DO_NOTHING, db_column='id_movimiento')

    class Meta:
        managed = False
        db_table = 'movimientos_detalle'


class ProveedorReactivo(models.Model):
    id_proveedor_reactivo = models.AutoField(primary_key=True)
    id_reactivo = models.ForeignKey('Reactivos', models.DO_NOTHING, db_column='id_reactivo')
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'proveedor_reactivo'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class ReactivoLaboratorio(models.Model):
    id_reactivo_laboratorio = models.AutoField(primary_key=True)
    id_reactivo = models.ForeignKey('Reactivos', models.DO_NOTHING, db_column='id_reactivo')
    id_laboratorio = models.ForeignKey(Laboratorios, models.DO_NOTHING, db_column='id_laboratorio')
    cantidad = models.IntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reactivo_laboratorio'


class Reactivos(models.Model):
    id_reactivo_personal = models.AutoField(primary_key=True)
    nombre_reactivo = models.CharField(max_length=255, blank=True, null=True)
    id_unidad = models.ForeignKey('UnidadesDeMedida', models.DO_NOTHING, db_column='id_unidad')
    fecha_caducidad = models.DateField(blank=True, null=True)
    id_familia = models.ForeignKey(Familias, models.DO_NOTHING, db_column='id_familia')
    reutilizable = models.BooleanField(blank=True, null=True)
    cas = models.CharField(max_length=255, blank=True, null=True)
    ficha = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reactivos'


class Residuos(models.Model):
    id_residuo = models.AutoField(primary_key=True)
    id_clasificaciones_residuos = models.ForeignKey(ClasificacionesResiduos, models.DO_NOTHING, db_column='id_clasificaciones_residuos')

    class Meta:
        managed = False
        db_table = 'residuos'


class ResiduosLaboratorio(models.Model):
    id_residuos_laboratorio = models.AutoField(primary_key=True)
    id_laboratorio = models.ForeignKey(Laboratorios, models.DO_NOTHING, db_column='id_laboratorio')
    id_residuo = models.ForeignKey(Residuos, models.DO_NOTHING, db_column='id_residuo')
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residuos_laboratorio'


class TiposMovimientos(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    signo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_movimientos'


class UnidadesDeMedida(models.Model):
    id_unidad = models.AutoField(primary_key=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades_de_medida'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255, blank=True, null=True)
    apellido_usuario = models.CharField(max_length=255, blank=True, null=True)
    email_usuario = models.CharField(max_length=255, blank=True, null=True)
    tipo_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
