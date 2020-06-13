import sys
sys.path.append('.')
from app.crawl import *


def parse_letters(_email,item):
    html_body = item.body #取出郵件內容
    sp = BeautifulSoup(html_body, 'lxml') #使用beautifulsoup解析文本

    recruit = sp.title.text.split(' ')[0]

    try:
        name = sp.find_all('table')[0].find('div',{'class':'resume_face'}).find('table').find_all('td')[1].find('b').text
    except:
        try:
            name = sp.title.text.split(' ')[-1]
        except:
            name = "無"
    try:
        find_job = sp.title.text.split('应聘 ')[1]
    except:
        try:
            find_job = sp.title.text.split(name)[0].split('圆才')[1]
        except:
            find_job = sp.title.text.split(' ')[1]

    try:
        age = sp.find_all('table')[0].find_all('div')[6].find(id="p_info_view").find_all('tr')[1].find_all('td')[1].text.split('(')[1].split(')')[0]
    except:
        age = "無"

    try:
        gender = sp.find_all('table')[0].find('div',{'class':'resume_face'}).find('table').find_all('td')[1].text.split('\r\n')[1]
    except:
        gender = "無"

    #---------------------------------------------------------------------
    try:
        school = sp.find_all('table')[0].find('div',{'class':'edu'}).find('span',{'class':'sub_title'}).text
    except:
        school = "無"
    if school == '':
        school = "無"

    try:
        high_edu = sp.find_all('table')[0].find_all('div')[6].find(id="p_info_view").find_all('tr')[6].find_all('td')[1].text
    except:
        high_edu = "無"
    if high_edu == '':
        high_edu = "無"
    highest_education = high_edu + "-" + school
    #---------------------------------------------------------------------
    try:
        want_job_name = sp.find(id="p_want_view").find('td',{'class':'lantd'}).text
    except:
        want_job_name = "無"

    if want_job_name == '':
        want_job_name = "無"

    try:
        work_experience =  sp.find('div',{'class':'company_name'}).find('time').text.split()[0]
    except:
        work_experience = "無"

    if work_experience != "無":
        try:
            job_name = sp.find_all('div',{'class':'job_box'})[0].find_all('div',{'class':'info'})[2].text.split('职位：')[1]
        except:
            job_name = sp.find_all('div',{'class':'work'})[0].find_all('div',{'class':'info'})[1].text.split('Department：')[1]
        try:
            #company_name = sp.find_all('div',{'class':'work'})[0].find('div',{'class':'company_name'}).text.split()[1]
            company_name = sp.find('div',{'class':'company_name'}).text.split()[1]
        except:
            company_name = "求職者隱藏公司名稱"
        recent_work = company_name + "-" + job_name
    else:
        recent_work = "無-無"
    #-----------------
    try:
        address = sp.find_all('table')[0].find_all('div')[6].find(id="p_info_view").find_all('tr')[5].find_all('td')[1].text
    except:
        address = "無"
    if address == '':
        address = "無"

    try:
        email = sp.find_all('table')[0].find_all('div')[6].find(id="p_info_view").find_all('tr')[3].find_all('td')[1].text
    except:
        email = "無"
    if(email == ""):
        email = "無"

    try:
        cellphone = sp.find_all('table')[0].find_all('div')[6].find(id="p_info_view").find_all('tr')[2].find_all('td')[1].text
    except:
        cellphone = "無"
    #cellphone =  sp.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text
    contact_method = "全時段"
    date = sp.find('strong').text.split()[1]
    time = sp.find('strong').text.split()[2]
    Time = date + " " + time

    if cellphone == "無":
        t = datetime.datetime.now()
        ID = str(time.mktime(t.timetuple())).split('.')[0]
    else:
        ID = cellphone


    sImgSrc = sp.find_all('img')[0]['src']
    r = requests.get(sImgSrc,verify=False)
    image = BytesIO(r.content).read()

    creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    _email.personal_data={
            'recruit':recruit,
            'find_job':find_job,
            'name':name,
            'age':age,
            'gender':gender,
            'highest_education' : highest_education ,
            'want_job_name' :want_job_name ,
            'work_experience' : work_experience,
            'recent_work' : recent_work,
            'address' : address,
            'email' : email,
            'cellphone' : cellphone,
            'contact_method' : contact_method,
            'resume_file':html_body,
            'Time':Time,
            'ID':ID,
            'creation_time':creation_time
        }
    print(_email.personal_data)



def get_letters(recruit):
    _email = Email()
    letters = _email.check_letter_len(recruit)
    
    for item in letters:
        parse_letters(_email,item)


    
