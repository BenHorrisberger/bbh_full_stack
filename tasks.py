from invoke import task

@task
def list_viable(c, range, seats, bags):

    print(range, seats, bags)

    