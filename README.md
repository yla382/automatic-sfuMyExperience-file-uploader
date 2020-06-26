### Overview
Automatic-sfuMyExperience-file-uploader
Web Automation using Selenium to upload documents to SFU myExperience website


### Required Libary
```sh
$ pip install selenium
```

### Prior Set Up
- Context.txt contains a dictionary format texts. Fill in the empty string item for key 'username' and 'password'. ex
    ```sh
    {'username': 'user_name', 'password': 'pass'}
    ```
- Make sure all of your context.txt, uploadfiles.py, and the document you are uploading are in the same directory

### Run Instruction
- Run uploadfiles.py and sepecify the document type, document file name, and new name of the document when uploaded
    ```sh
    $ python uploadfiles.py [document_type_code] [document_name] [uploaded_as_name]
    ```
    ex.
    ```sh
    $ python uploadfiles.py cl coverletter.pdf coverletter
    ```
### Document Type Codes
| Document Type | document_type_code |
| ----------- | ----------- |
| SIS | sis|
| Coverletter | cl |
| Resume | res|
| Transcripts | tr|
| Writing sample | ws|
| Reference | ref|
| Work Permit| wp|
| Other| other|
| Report 1 | rep1|
| Report 2| rep2|
|Terms and Conditions| tc|
|Work Permit Agreement| wpa|
|Work Permit Renewal| wpr|
