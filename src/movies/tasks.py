from celery import shared_task


@shared_task
def add(x, y):
    # do not use django model instances as args.
    return x + y