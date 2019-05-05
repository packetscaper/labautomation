from netmiko import ConnectHandler
import argparse
import time
from webexteamssdk import WebexTeamsAPI
class Terminal:
  def  __init__(self):
   self.device = {
    'device_type' : 'terminal_server',
    'ip'  :  '10.10.10.11',
    'username'   : 'admin',
    'password'   : 'credentials'}

   self.console = {'fusion':'1', 'border1':'2', 'border2':'3','edge1':'4', 'edge2':'5'}
   self.net_connect = ConnectHandler(**self.device)

  def send_command(self,command,wait=2):
      c = command
      self.net_connect.write_channel(c)
      print "command issued : " + c
      time.sleep(2)
      print 'hitting enter'
      self.net_connect.write_channel('\r')
      print "waiting for " + str(wait) + " seconds"
      time.sleep(wait)
      print "Read from console " + self.net_connect.read_channel()
      time.sleep(2)


  def run_guest_shell_script(self,script):
      self.send_command('conf t')
      self.send_command('iox',150)
      self.send_command('end')
      self.send_command('guestshell enable',20)
      self.send_command('guestshell run bash',10)
      self.send_command(script,5)
      self.send_command('exit')
      self.send_command('conf t')
      self.send_command('no iox')


  def reset_switch(self,switch):
   console = str(self.console[switch])
   time.sleep(2)
   print self.net_connect.read_channel()
   time.sleep(2)
   print "choosing option " + console
   self.send_command(console)
   print "hitting enter again"
   self.send_command('\r')

   print "entering device console"
   print "entering username"
   self.send_command('admin')
   print "entering password"
   self.send_command('credentials')
   print "entering enable mode "
   self.send_command('enable')
   print "running reset script"
   self.run_guest_shell_script('python reset.py')
   print "switch reloaded"

  def init_switch(self,switch):
   script = 'python '+ switch +'.py'
   print "reading from console " + self.net_connect.read_channel()
   time.sleep(2)
   #Please answer 'yes' or 'no'.\r\nWould you like to enter the initial configuration dialog? [yes/no]:
   self.send_command('no')
   #u'no\r\n\r\nWould you like to terminate autoinstall? [yes]: '
   self.send_command('yes',5)
   self.send_command('\r')
   self.send_command('en')
   self.run_guest_shell_script(script)


if __name__ == '__main__':
  t = Terminal()
  parser = argparse.ArgumentParser(description="Node")
  parser.add_argument('n',help= 'Choose a node - edge1,edge2,border1,border2')
  args = vars(parser.parse_args())
  node = args['n']
  t.reset_switch(node)
  print "waiting for 10 minutes for switch to reboot"
  time.sleep(600)
  print "reinitializing switch"
  t.init_switch(node)

  api = WebexTeamsAPI(access_token='webex_access_token')
  message = node + " is reset"
  api.messages.create(roomId="webex_room_id",
                      markdown= message)