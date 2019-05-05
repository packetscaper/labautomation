from cli import *

def set_interface_Gi06():
        configuration = '''interface Gi1/0/6
                      Description Connected to Border1
                      no switchport
                      ip address 10.10.30.38 255.255.255.252
                      ip router isis
                      isis network point-to-point'''

        config_result = configure(configuration)
        print config_result

def set_interface_Gi11():
        configuration = '''interface Gi1/0/11
                       Description Connected to Edge2
                       no siwtchport
                       ip address 10.10.30.33 255.255.255.252
                       ip router isis
                       isis network point-to-point'''

def set_interface_Gi12():
        configuration = '''interface Gi1/0/12
                          Description Connected to Edge1
                          no switchport
                          ip address 10.10.30.29 255.255.255.252
                          ip router isis
                          isis network point-to-point'''

        config_result = configure(configuration)
        print config_result

def set_loopback():
        configuration = '''interface Loopback0
                         ip address 10.10.30.82 255.255.255.255'''

        config_result = configure(configuration)
        print config_result

def set_interface_Gi1():
        configuration = '''interface Gi1/0/1
                            Description Connected to Fusion
                            switchport mode trunk'''

def set_interface_vlan702():
        configuration = ''' vlan 702
                            interface vlan702
                            ip address 10.10.30.6 255.255.255.252'''


def set_isis():
        configuration = ''' ip routing 
                         router isis
                         net 49.0000.0000.0000.2222.00
                        metric-style wide
                        passive-interface Loopback0'''

        config_result = configure(configuration)

        print config_result

def set_rest_config():
        configuration = '''    hostname BR01
                                username admin privilege 15 password Cisco 
                                 line vty 0 4
                                 privilege level 15
                                 transport input ssh
                                 login local
                             '''
        config_result = configure(configuration)

        print config_result

if __name__ == '__main__':
        set_loopback()
        set_isis()
        set_interface_Gi11()
        set_interface_Gi12()
        set_interface_Gi11()
        set_interface_vlan702()
        set_rest_config()

        api = WebexTeamsAPI(access_token='webex_access_token')

        api.messages.create(roomId="webex_room_id",markdown="border2 is alive")