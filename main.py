import psutil
import time
import winsound
import platform
import os
from plyer import notification

def clear_screen() :
    '''
    Clearing the screen on various operating systems
    '''
    if os.name == 'nt' :
        os.system('cls')
    else :
        os.system('clear')

def sound() :
    '''
    Audio playback on 3 operating systems
    '''
    try :
        sys_name = platform.system()

        if sys_name == 'Windows' : # Windows
            winsound.Beep(1200, 400) 
            time.sleep(0.15) 
            winsound.Beep(900, 400)
            time.sleep(0.15)
            winsound.Beep(1200, 400)
            time.sleep(0.15)

        elif sys_name == 'Linux' : # Linux
            os.system('paplay /usr/share/sounds/freedesktop/stereo/message-new-instant.oga 2>/dev/null || printf "\\a"')

        elif sys_name == 'Darwin':  # macOS
            os.system('say "Battery alert"')

    except Exception as e:
        return e

def main() :
    '''
    The main function is for managing battery status in the 3 operating systems Windows, macOS, and Linux.
    - Supports manual and automatic mode
    - Alarm sound and notification when reaching the limit
    - Smooth user interface
    '''

    try :
        user = input('''
Panel :
    Run in manual mode -> 1
    Run in automatic mode -> 2
    Exit -> 3
>>> ''')

        while True :
            last_alert = 0

            try :
                if user == '1' :
                    in_alert_mode = input('Is the alert active?(y/n) -> ').lower()
                    if in_alert_mode == 'y' :
                        in_alert_mode = True
                        LOWEST_CHARGE = int(input('lowest charge -> '))
                        HIGHEST_CHARGE = int(input('highest charge -> '))
                        CHECK_INTERVAL = int(input('check interval -> '))
                        WARNING_TIME = int(input('Warning time(seconds) -> '))
                        break

                    elif in_alert_mode == 'n' :
                        in_alert_mode = False
                        CHECK_INTERVAL = int(input('check interval -> '))
                        break

                    else :
                        print('🚫 Try Again')
                        continue

                elif user == '2' :
                    LOWEST_CHARGE = 10
                    HIGHEST_CHARGE = 90
                    CHECK_INTERVAL = 8     
                    in_alert_mode = True
                    WARNING_TIME = 60
                    break

                elif user == '3' :
                    exit('👋 Good Bye!')


            except ValueError :
                print('🚫 The input value is incorrect')
                continue

            except Exception as e :
                print(e)
                continue



        while True :
            current_time = time.time() # Now time

            try :
                clear_screen()
                
                battery = psutil.sensors_battery() # Get battery information

                if battery is None :
                    print('❌ Battery not detected')
                    
                else :
                    percent = battery.percent
                    secs_left = battery.secsleft       
                    plugged = battery.power_plugged

                    print(f'🔋 Battery percentage : {percent}%')

                    if plugged :
                        print('It is charging')
                        print('⚡ Charging status : On')

                        if in_alert_mode and percent >= HIGHEST_CHARGE :

                            if current_time - last_alert > WARNING_TIME :
                                notification.notify(title='⚠️ Battery Almost Full' , message=f'Battery reached {percent}% — Unplug to protect battery')
                                sound()
                                last_alert = current_time

                    else :
                        print(f'⏰ Time to stay on : {secs_left // 3600} hour | {(secs_left % 3600) // 60} minutes | {secs_left % 60} seconds')
                        print('⚡ Charging status : Off')

                        if in_alert_mode and percent <= LOWEST_CHARGE  :

                            if current_time - last_alert > WARNING_TIME :
                                notification.notify(title='⚠️ Low Battery Warning' , message=f'Battery is only {percent}% — Please plug in!')
                                sound()
                                last_alert = current_time

                    print('To return to the panel, press control+c')
  
                        
                    time.sleep(CHECK_INTERVAL)


            except KeyboardInterrupt :
                return

            except Exception as e :
                print(e)
                break

    except KeyboardInterrupt :
        clear_screen()
        exit('👋 Good Bye!')
    except Exception as e :
        exit(e)   

if __name__ == '__main__':
    main()
    while True :
        clear_screen()
        main()


