from google.cloud import datastore

datastore_client = datastore.Client()

def save_task(t):
    entity = datastore.Entity(key=datastore_client.key('task'))
    entity.update({
        'taskId': t.taskId,
        'name': t.name,
        'completed': t.completed
    })

    datastore_client.put(entity)

def fetch_tasks():
    query = datastore_client.query(kind='task')
    t1 = list(query.fetch())
    return t1

def patch_task(taskId):
    entity = datastore_client.get(getKey(taskId).key)
    entity["completed"] = True
    datastore_client.put(entity)
    return "OK"

def delete_task(taskId):
    key = getKey(taskId).key
    datastore_client.delete(key)
    return "OK"

def getKey(taskId):
    query = datastore_client.query(kind="task")
    query.add_filter("taskId", "=", taskId)
    return list(query.fetch())[0]
