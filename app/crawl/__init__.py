from app import *
class Email():
    def __init__(self):
        self.personal_data={
            'recruit':'',
            'find_job':'',
            'name':'',
            'age':'',
            'gender':'',
            'highest_education' : '' ,
            'want_job_name' :'' ,
            'work_experience' : '',
            'recent_work' : '',
            'address' : '',
            'email' : '',
            'cellphone' : '',
            'contact_method' : '',
            'resume_file':'',
            'Time':'',
            'ID':'',
            'creation_time':''
        }
        self.files = {
            'image':''
        }

        self.account = self.login()

    def login(self):
        self.account = ''
        try:
            credentials = Credentials(username= username,  password=password)
            version = Version(build=Build(15, 0, 12, 34))
            config = Configuration(server=server, credentials=credentials,version = version, auth_type=NTLM)

            self.account = Account(primary_smtp_address=primary_smtp_address,config=config, credentials=credentials, autodiscover=False,access_type=DELEGATE )

            ews_url = self.account.protocol.service_endpoint
            ews_auth_type = self.account.protocol.auth_type

            config = Configuration(service_endpoint=ews_url, credentials=credentials, auth_type=ews_auth_type)
            account = Account(
                primary_smtp_address=primary_smtp_address,
                config=config, autodiscover=False,
                access_type=DELEGATE,
            )
            print('信箱連接成功')
        except:
            print("mail connect fail...")
        return self.account

    def check_letter_len(self,recruit):
        #connect mailbox
        _indox=self.account.inbox / 'Archive'
        self._letters=_indox.filter(subject__contains=recruit)  
        return self._letters
                
