# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, request, jsonify, render_template
import json
import uuid

import os
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=path + "/misc/guest-service.json"

from models.tasks import tasks
from utils.encode import TaskEncoder
from entities.task import save_task, fetch_tasks, patch_task, delete_task


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def fetch():
    t = fetch_tasks()
    return render_template('index.html', tasks=t)
    #return jsonify(t)

@app.route('/', methods=['POST'])
def save():
    request_data = request.get_json()
    id = str(uuid.uuid4())
    t = tasks(id, request_data['name'], False)
    save_task(t)
    return json.dumps(t, indent=4, cls=TaskEncoder)

@app.route('/', methods=['PATCH'])
def patch():
    request_data = request.get_json()
    return patch_task(request_data['taskId']), 200

@app.route('/', methods=['DELETE'])
def delete():
    request_data = request.args['taskId']
    return delete_task(request_data)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
