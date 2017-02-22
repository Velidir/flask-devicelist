from flask import request,render_template
from model import devicelist,app,db
from sqlalchemy.exc import IntegrityError

try: 
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    #@app.route('/get_ip')
    # def get_ip(request):
    # 	result = "Switch IP is invalid"
    # 	print ("step 1")
    # 	if request.method == 'POST':
    # 		MyIPform = IPForm(request.POST)
    # 		print ("step 2")
    # 		if MyIPform.is_valid():
    # 			 SWIPform = MyIPform.cleaned_data['yourip']
    # 			 print ("Valid IP")
    # 			 result = getSW(SWIPform)
    			 			 
    # 	else:
    # 		MyIPform = IPForm()
    # 	return render(request, 'ip.html',{"result": result })
    
    @app.route('/show_devices', methods=['GET', 'POST'])
    def show_devices():
        if request.method == 'POST':
            print("Entering hellhole")
            result = edit_devices(request)
            print("Exited Hellhole")
            return render_template('devices.html', result=result)
        else:
            result = devicelist.query.all()
            return render_template('devices.html', result=result)
    
    @app.route('/add_devices', methods=['POST'])
    def add_devices():
        if request.method == 'POST':
            print("Entering Addition hellhole")
            new_device=devicelist(
                ip = request.form.get('ip'),
                dmvpn= request.form.get('DMVPN'),
                description= request.form.get('Description'),
                enable = request.form.get('Enable'),
                password =request.form.get('password'),
                username =request.form.get('Username'),
                access =request.form.get('Access'),
                type = request.form.get('type'),
                project =request.form.get('project'),
                country =request.form.get('country'),
                backedup = request.form.get('Backup')
            )
            try:
                db.session.add(new_device)
                db.session.commit()
                print("Worked")
                return "True"
            except IntegrityError:
                print("Did not work")
                return "False"
                
    @app.route('/delete_devices', methods=['POST'])
    def delete_devices():
        if request.method == 'POST':
            print("Entering Delete hellhole")
            ipFromAjax=request.json
            try:
                deviceForDeletion=devicelist.query.filter_by(ip=ipFromAjax).first()
                db.session.delete(deviceForDeletion)
                db.session.commit()
                print("Worked")
                return "True"
            except IntegrityError:
                print("Did not work")
                return "False"    
    # def personal_add_devices(callfromAddDevice):
    #     print(callfromAddDevice)
        
    #         # MyDeviceForm = DeviceForm(request.POST)
    #         # if MyDeviceForm.is_valid():
    #         #     deviceip = MyDeviceForm.cleaned_data['ip']
    #         #     devicecountry = MyDeviceForm.cleaned_data['country']
    #         #     deviceproject = MyDeviceForm.cleaned_data['project']
    #         #     devicetype = MyDeviceForm.cleaned_data['type']
    #         #     deviceaccess = MyDeviceForm.cleaned_data['access']
    #         #     deviceusername = MyDeviceForm.cleaned_data['username']
    #         #     devicepassword = MyDeviceForm.cleaned_data['password']
    #         #     deviceenable = MyDeviceForm.cleaned_data['enable']
    #         #     devicebackedup = MyDeviceForm.cleaned_data['backedup']
    #         #     devicedescription = MyDeviceForm.cleaned_data['description']
    #         #     devicedmvpn = MyDeviceForm.cleaned_data['dmvpn']
    #         #     new_device=devices(
    #         #         ip = deviceip,
    #         #         dmvpn= devicedmvpn,
    #         #         description= devicedescription,
    #         #         enable = deviceenable,
    #         #         password =devicepassword,
    #         #         username =deviceusername,
    #         #         access =deviceaccess,
    #         #         type =devicetype,
    #         #         project =deviceproject,
    #         #         country =devicecountry
    #         #     )
    #         #     new_device.save()
    #     return "Done"
    #             #result = list(devices.objects.all())
    
    #             #return render(request, 'devices.html', {"result": result})

    # def delete_devices(request):
    #     if request.method == 'POST':
    #         instance = devices.objects.get(id=request.POST.get('id'))
    #         instance.delete()
    #         result = list(devices.objects.all())
    #         return render(request, 'devices.html', {"result": result})
    #     else:
    #         result = list(devices.objects.all())
    #         return render(request, 'devices.html', {"result": result})
    
    
    #### THIS IS A FUNCTION NOT A VIEW####
    def edit_devices(request):
        if request.method == 'POST':
            deviceip = request.POST.get('ip')
            devicecountry = request.POST.get('country')
            deviceproject = request.POST.get('project')
            devicetype = request.POST.get('type')
            deviceaccess =request.POST.get('access')
            deviceusername = request.POST.get('username')
            devicepassword = request.POST.get('password')
            deviceenable = request.POST.get('enable')
            devicebackedup = request.POST.get('backedup')
            devicedescription = request.POST.get('description')
            devicedmvpn = request.POST.get('dmvpn')
            new_device=devicelist(
                id = request.POST.get('id'),
                ip = deviceip,
                dmvpn= devicedmvpn,
                description= devicedescription,
                enable = deviceenable,
                password =devicepassword,
                username =deviceusername,
                access =deviceaccess,
                type =devicetype,
                project =deviceproject,
                country =devicecountry
            )
            #add the new device here
            db.session.add(new_device)
            db.session.commit()
            # return the new device here
            result = devicelist.query.all()
            return result

except ValueError:
    print("there was an error here" + ValueError)

# app.run(host='0.0.0.0', port=8080, debug=True)