from celery import shared_task

@shared_task
def debug_task():
    print(f'LOL')