from flask import request,render_template
from model import devicelist,app,db
from sqlalchemy.exc import IntegrityError

try: 
    @app.route('/')
    def hello_world():
        return 'Hello, World!'


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
            print("Entering Addition hellhole")
            new_device=devicelist(
                ip = request.form.get('ip'),
                dmvpn= request.form.get('DMVPN'),
                description= request.form.get('Description'),
                enable = request.form.get('Enable'),
                password =request.form.get('password'),
                username =request.form.get('Username'),
                access =request.form.get('access'),
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
    @app.route('/edit_devices', methods=['POST'])
    def edit_devices():
        editableDevice=devicelist.query.filter_by(ip=request.form.get('ip')).first()
        print(editableDevice.dmvpn)
        changedIP = request.form.get('changedIP')
        print(changedIP)
        if(request.form.get('changedIP') == None):
            print("wewe")
            #editableDevice.ip = request.form.get('changedIP')
        editableDevice.dmvpn = request.form.get('dmvpn')
        editableDevice.country = request.form.get('country')
        editableDevice.project = request.form.get('project')
        editableDevice.type = request.form.get('type')
        editableDevice.access =request.form.get('access')
        editableDevice.username = request.form.get('username')
        editableDevice.password = request.form.get('password')
        editableDevice.enable = request.form.get('enable')
        editableDevice.backedup = request.form.get('backedup')
        editableDevice.description = request.form.get('description')
        #add the new device here
        try:
            db.session.commit()
            print("Edit Worked")
            return "True"
        # return the new device here
        except IntegrityError:
            print("Edit Failed")
            return "False"

except ValueError:
    print("there was an error here" + ValueError)

# app.run(host='0.0.0.0', port=8080, debug=True)