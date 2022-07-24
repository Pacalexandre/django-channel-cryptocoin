""" Classe que instancia e carrega o Celery no projeto django"""
import os

from celery import Celery
#carregando as variaveis do django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
#abrindo uma instancia do Celery
app = Celery('app')
#colocando na configuração do django um namespace para as tarefas
app.config_from_object('django.conf:settings', namespace='CELERY')

#definicao de shchedule busca de dados
app.conf.beat_schedule = {
    'get_coins_30s':{
        'task': 'crypto.tasks.get_coins_data',
        'schedule': 30.1,
    }
}

#definindo autodiscovery qnd for procurar uma tarefa 
app.autodiscover_tasks()

# é definido no setting um broker para celery
# CELERY_BROKER_URL = 'redis://localhost:6379'
# preciso ter um broker pode ser um redis ou um rabbitmq ou kafta depende da configuração