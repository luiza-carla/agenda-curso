from django.contrib import admin
from contact.models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', #exibição de campos na listagem do admin
    ordering = '-id', #ordenação da listagem
    list_filter = 'created_date', #filtros
    search_fields = 'first_name', #busca de campos
    list_per_page = 10 #quantidade de registros por pagina
    list_max_show_all = 100 #quantidade máxima de registros por pagina ao exibir tudo
    list_editable = 'first_name', #campos editaveis sem precisar abrir o registro
    list_display_links = 'phone', #campos com link para abrir o registro