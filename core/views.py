from django.shortcuts import render
from .console import ConsoleDemo

# Create your views here.


def index(request):
    my_demo = ConsoleDemo()
    my_demo.get_login_info()
    result = my_demo.login()
    if not result:
        my_demo.quit_demo()
    else:
        my_demo.log_open()
        print("1:ASI1201E-D")
        print("2:ASI7223Y-A-V3")
        device_type = int(input('Please select device type:'))
        if device_type == 1:
            while True:
                my_demo.get_operate_info()
                if my_demo.operatetype == 0:
                    my_demo.logout()
                    my_demo.quit_demo()
                    break
                elif my_demo.operatetype == 1:
                    result = my_demo.start_operate()
                    if not result:
                        my_demo.logout()
                        my_demo.quit_demo()
                        break
                elif my_demo.operatetype == 2:
                    result = my_demo.alarm_listen()
                    if not result:
                        my_demo.logout()
                        my_demo.quit_demo()
                        break
                elif my_demo.operatetype == 3:
                    result = my_demo.access_operate()
                    if not result:
                        my_demo.logout()
                        my_demo.quit_demo()
                        break
        elif device_type == 2:
            while True:
                my_demo.get_operate_info()
                if my_demo.operatetype == 0:
                    my_demo.logout()
                    my_demo.quit_demo()
                    break
                elif my_demo.operatetype == 1:
                    result = my_demo.user_operate()
                    if not result:
                        my_demo.logout()
                        my_demo.quit_demo()
                        break
                elif my_demo.operatetype == 2:
                    result = my_demo.intelligent_operate()
                    if not result:
                        my_demo.logout()
                        my_demo.quit_demo()
                        break
                elif my_demo.operatetype == 3:
                    result = my_demo.access_operate()
                    if not result:
                        my_demo.logout()
                        my_demo.quit_demo()
                        break
        else:
            print("Wrong device type")
            my_demo.logout()
            my_demo.quit_demo()
    return render(request, 'index.html')