from cli import*


def set_interface_Gi11():
   configuration = '''interface Gi1/0/11
                   no switchport
                   Description Connected to Border1
                   ip address 10.10.30.44 255.255.255.252
                   ip router isis
                   isis network point-to-point'''

   config_result=configure(configuration)
   print config_result

def set_interface_Gi12():
   configuration = '''interface Gi1/0/12
                    no switchport 
                    Description Connected to Border2
                    ip address 10.10.30.22 255.255.255.252
                    ip router isis
                    isis network point-to-point'''


   config_result=configure(configuration)
   print config_result


def set_loopback():
   configuration = '''interface Loopback0
                      ip address 10.10.30.84 255.255.255.255'''

   config_result = configure(configuration)
   print config_result


def set_isis():
  configuration = '''ip routing
                     router isis
                     net 49.0000.0000.0000.4444.00
                     metric-style wide
                     passive-interface Loopback0'''

  config_result = configure(configuration)

  print config_result


def set_rest_config():
    configuration =   ''' hostname Edge-02 
                          username admin privilege 15 password credentials
                          line vty 0 4
                          privilege level 15
                          transport input ssh
                          login local
                          iox'''
    #guest = cli('guest enable')
    config_result=configure(configuration)

    print config_result

if __name__=='__main__':

 set_loopback()
 set_isis()
 set_interface_Gi11()
 set_interface_Gi12()
 set_rest_config()

 api = WebexTeamsAPI(access_token='webex_access_token')

 api.messages.create(roomId="webex_room_id",markdown="edge2 is alive")