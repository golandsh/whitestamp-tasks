# whitestamp-tasks

To run the app locally you need to install virtualdev
do the following:

* pip install virtualenv
* virtualenv misc
* source misc/bin/activate
* misc/bin/pip install google-cloud-datastore

To get a json with all the properties for the cloud run:

* gcloud iam service-accounts keys create <local_path_to_download.json> --iam-account wisestamp-user@wise-stamp-shlomi.iam.gserviceaccount.com

<b>This file rename to guest-service.json and place under the misc folder</b>
