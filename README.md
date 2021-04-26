# whitestamp-tasks

To run the app locally you need to install virtualdev
and do the following:

* pip install virtualenv
* virtualenv misc
* source misc/bin/activate
* misc/bin/pip install google-cloud-datastore

To get a json with all the properties for the cloud run:

* gcloud iam service-accounts keys create guest-service --iam-account wisestamp-user@wise-stamp-shlomi.iam.gserviceaccount.com

<b>Place under the misc folder</b>

* change under templates/index.html baseUrl to localhost
* run python main.py
