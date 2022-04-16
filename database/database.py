from database.schema import Session, ToDo, engine


def mutate_task(task, content):
    
    if not task or not content: return False, 'Please provide task id and content to update'

    if not task.strip().isdigit(): return False, 'Invalid task id is provided'
    if not content: return False, 'Please provide content for task'
    
    session = Session(bind=engine)
    task = session.query(ToDo).filter(ToDo.id==task).first()
    if not task: return False, 'No task found against the task id' 
    task.content = content
    session.commit()
    return True, 'Task has been updated'

def remove_task(task):
    
    if not task: return False, 'Please provide task id to delete'
    if not task.strip().isdigit(): return False, 'Invalid task id is provided'
    session = Session(bind=engine)
    task = session.query(ToDo).filter(ToDo.id==task).first()
    if not task: return False, 'No task found against the task id' 
    session.delete(task)
    session.commit()
    
    return True, 'Task has been deleted'

def add_task(content, user):
    if not content: return False, 'Please provide content for task'
    try:
        session = Session(bind=engine)
        item = ToDo(user=user.id, content=content)
        session.add(item)
        session.commit()
        return True, 'Task is created'
    except Exception as e:
        return False, e

def get_tasks(user):
    try:
        session = Session(bind=engine)
        tasks = session.query(ToDo).filter(ToDo.user==user.id)
        tasks = [task.dictify() for task in tasks]
        
        if tasks:
            return True, tasks
        else:
            return False, 'No associated tasks found'
    except Exception as e:
        return False, e
