""" Carregamento automatico do Celery atravez do inicio do django """
from .celery import app as celery_app

#trazendo as bibliotecas todas as funcionalidades do celery para projeto from celery import *
__all__ = ['celery_app']