from invoke import task

@task
def mytask(c):
    print("inside mytask()")
    c.run ("ls -l")