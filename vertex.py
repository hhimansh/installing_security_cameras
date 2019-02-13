#!/usr/bin/env python2

import math
import sys

class Generate_streets(object):

  def dictionnary(self):
    self.dict_1={}

  def list_dict(self):
    self.dict_2={}
    self.dict_3={}
    self.i_sect=set()
    self.t_list=set()
    self.dict_4={}
    self.cnt=0
    self.dict_5={}
    self.list_10=[]
    self.tf=True
    self.i_sect_new=set()
    self.i_sect_test=set()
  
  def addInput(self):
    self.list_1=[]
    self.street=raw_input()
    self.list_1.append(self.street.strip(" ").split('"'))
    for list_var in range (len(self.list_1[0])):
      self.list_1[0][list_var]=self.list_1[0][list_var].strip(" ")
    self.aut_addInput()
    return self.list_1
  
  def aut_addInput(self):
    if self.list_1[0][0]=="a":
      self.addStreet()
      self.addInput()
    elif self.list_1[0][0]=="c":
      self.input_Change_Street()
      self.addInput()
    elif self.list_1[0][0]=="r":
      self.input_Remove_Street()
      self.addInput()
    elif self.list_1[0][0]=="g":
      self.list_dict()
      self.construct_intersect()
    #elif self.list_1[0][0]=="e":
     # sys.exit()
    else:
    # print "Please enter any one of the (a :add, c:change, r:remove, g:graph) commands"
      self.addInput()

  def addStreet(self):
    if len(self.list_1[0])<2:
      print "Wrong input format, please try again"
      self.addInput()
    self.list_2=[]
    self.variable_1=self.list_1[0][1]
    self.variable_2=self.list_1[0][2]
    self.list_2.append(self.variable_2.strip(" ").split(" "))
    if len(self.list_2[0])<2:
      print "Number of Coordinates must be greater than 1, please enter again"
      self.addInput()
    else:
      self.dict_1[self.variable_1]=self.list_2[0]
      self.addInput()

  def input_Remove_Street(self):
    self.list_3=[]
    if len(self.list_1[0])==3:
      string_1=self.list_1[0][1]
      if string_1 in self.dict_1.keys():
        del self.dict_1[string_1]
        self.addInput()
      else:
        print "Given name of the street does not exist"
        self.addInput()
    else:
      print "String format not correct, please enter again"
      self.addInput()
  
  def input_Change_Street(self):
    self.list_4=[]
    if len(self.list_1[0])>2:
      string_2=self.list_1[0][1]
      string_3=self.list_1[0][2]
      self.list_4.append(string_3.strip(" ").split(' '))
      if string_2 in self.dict_1.keys():
        self.dict_1[string_2]=self.list_4[0]
      else:
          print "Street name not found, please enter again"
    else:
      print "Something wrong with the input, please try again with street name and coordinates"
  

  def construct_intersect(self):
    st_name=self.dict_1.keys()
    for st_1 in range(0,len(st_name)-1):
      for st_2 in range(st_1 +1, len(st_name)):
        st_1_name=st_name[st_1]
        st_2_name=st_name[st_2]
        
        self.dict_3[st_1_name]=set()
        self.dict_3[st_2_name]=set()

        st_1_node=self.dict_1[st_1_name]
        st_2_node=self.dict_1[st_2_name]

        for node_1 in range(0,len(st_1_node)-1):
          for node_2 in range(0,len(st_2_node)-1):
            line_1=(st_1_node[node_1],st_1_node[node_1 +1])
            line_2=(st_2_node[node_2],st_2_node[node_2 +1])
            self.dict_3[st_1_name].add(line_1)
            self.dict_3[st_2_name].add(line_2)
            pt=self.line_intersect(line_1,line_2)
            if self.tf!=False and pt!=0:
              self.i_sect.add(str(pt))
    if len(self.i_sect)>0:
      self.get_V_E()
      self.final_output()
      self.addInput()
    else:
      self.final_output()
      self.addInput()
        
  def line_intersect(self,l_1,l_2):
    list(l_1)
    list(l_2)
    list_app1=[]
    list_app2=[]
    list_app1_store=[]
    list_app2_store=[]
    for x in range(len(list(l_1))):
      var1=list(l_1)[x]
      list_app1.append(var1.strip("(").strip(")").split(','))
    for x in range(len(list(l_2))):
      var2=list(l_2)[x]
      list_app2.append(var2.strip("(").strip(")").split(','))
    list_app1_store=self.line1(list_app1)
    list_app2_store=self.line1(list_app2)

    R1=self.intersect(list_app1_store,list_app2_store)
    if R1:
      self.Pt=self.aut_on_intersect(R1,list_app1,list_app2)
      self.tf=self.on_line()
      return R1
    else:
      return 0

  def on_line(self):
    if self.Pt!=False:
      return True
    else:
      return False


  def line1(self,l1):
    ll1=[]
    A=int(l1[0][1])-int(l1[1][1])
    B=int(l1[1][0])-int(l1[0][0])
    C=int(l1[0][0])*int(l1[1][1])-int(l1[1][0])*int(l1[0][1])
    ll1.append(A)
    ll1.append(B)
    ll1.append(-C)
    return ll1
  
  def intersect(self,L1,L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D!=0:
      x = Dx / D
      y = Dy / D
      return x,y
    else:
      return False

  def aut_on_intersect(self,RR,dec1,dec2):
    distance_line1_1=math.sqrt((RR[0]-int(dec1[0][0]))**2 + (RR[1]-int(dec1[0][1]))**2)
    distance_line1_2=math.sqrt((RR[0]-int(dec1[1][0]))**2 + (RR[1]-int(dec1[1][1]))**2)
    total_distance_line1=distance_line1_1+distance_line1_2

    distance_line1_i1=math.sqrt((int(dec1[0][0])-int(dec1[1][0]))**2 + (int(dec1[0][1])-int(dec1[1][1]))**2)

    distance_line2_1=math.sqrt((RR[0]-int(dec2[0][0]))**2 + (RR[1]-int(dec2[0][1]))**2)
    distance_line2_2=math.sqrt((RR[0]-int(dec2[1][0]))**2 + (RR[1]-int(dec2[1][1]))**2)
    total_distance_line2=distance_line2_1+distance_line2_2

    distance_line2_i1=math.sqrt((int(dec2[0][0])-int(dec2[1][0]))**2 + (int(dec2[0][1])-int(dec2[1][1]))**2)

    if int(distance_line1_i1)==int(total_distance_line1) and int(distance_line2_i1)==int(total_distance_line2):
      return True
    else:
      return False
  

  def conv_i_sect(self):
    for x in self.i_sect:
      l_test=[]
      l_test.append(x.strip("(").strip(")").split(','))
      test_var_1=l_test[0][0]
      test_var_2=l_test[0][1]
      pnt=(int(test_var_1),int(test_var_2))
      self.i_sect_new.add(pnt)
    return self.i_sect_new
    


  def get_V_E(self):
    self.conv_i_sect()
    for x in self.i_sect_new:
      str11=self.conver_x(x)
      for st_name in self.dict_3.keys():
        r_list=[]
        a_list=[]
        for x1 in self.dict_3[st_name]:
          if self.online(str11,x1)==True:
            (l_0,l_1)=x1
            add_l_0=(str11,l_0)
            add_l_1=(str11,l_1)
            r_list.append(x1)
            a_list.append(add_l_0)
            a_list.append(add_l_1)
        for r_line in r_list:
          self.dict_3[st_name].remove(r_line)
          if r_line in self.t_list:
            self.t_list.remove(r_line)
        for a_line in a_list:
          self.dict_3[st_name].add(a_line)
          self.t_list.add(a_line)
    #nd=set()
    ed=set()
    for t_node in self.t_list:
      ed.add(t_node)
      for n in t_node:
        if n not in self.dict_4.values():
          self.cnt+=1
          self.dict_4[self.cnt]=n
    for e in ed:
      (n0,n1)=e
      nodei_n0=0
      nodei_n1=0
      for nodei in self.dict_4.keys():
        if n0==self.dict_4[nodei]:
          nodei_n0=nodei
          self.dict_5[nodei_n0]=n0
        elif n1==self.dict_4[nodei]:
          nodei_n1=nodei
          self.dict_5[nodei_n1]=n1
        if nodei_n0 and nodei_n1:
          break
      self.list_10.append((nodei_n0,nodei_n1))
  
  def conver_x(self,xxx):
    str1=str(xxx)
    count=0
    for i in str1:
      if i==" ":
        str1=str1[:count]+str1[count+1:]
      count+=1
    return str1

  def online(self,v1,v2):
    list11=[]
    list12=[]
    list12.append(v1.strip(" ").strip("(").strip(")").split(','))
    for x in range(len(v2)):
      list11.append(v2[x].strip(" ").strip("(").strip(")").split(','))
    distance_line1_1=math.sqrt((int(list12[0][0])-int(list11[0][0]))**2 + (int(list12[0][1])-int(list11[0][1]))**2)
    distance_line1_2=math.sqrt((int(list12[0][0])-int(list11[1][0]))**2 + (int(list12[0][1])-int(list11[1][1]))**2)
    total_distance_line1=distance_line1_1+distance_line1_2

    distance_line1_i1=math.sqrt((int(list11[0][0])-int(list11[1][0]))**2 + (int(list11[0][1])-int(list11[1][1]))**2)
    if int(distance_line1_i1)==int(total_distance_line1):
      return True
    else:
      return False

  def convert(self):
    for i in self.dict_5.keys():
      j = 0
      while j < len(self.dict_5[i]):
        if self.dict_5[i][j] == " ":
          self.dict_5[i] = self.dict_5[i][0:j] + (self.dict_5[i][(j+1):(len(self.dict_5[i]))])
        else:
          j += 1
  
  def convert_dict_4(self):
    for i in self.dict_4.keys():
      j = 0
      while j < len(self.dict_4[i]):
        if self.dict_4[i][j] == " ":
          self.dict_4[i] = self.dict_4[i][0:j] + (self.dict_4[i][(j+1):(len(self.dict_4[i]))])
        else:
          j += 1

  def convert_dict_3(self):
    for i in self.dict_3.keys():
      print i
  
  def final_output(self):
    sv1=[]
    sv2=[]
    s3=""
    s1=""
    s2=""
    cc=0
    self.convert()
   # print "V={"

    for d1 in self.dict_5.keys():
      cc+=1

    s1="V "+str(cc)
    print s1
    sys.stdout.flush()
     # print str(d1) + ": (" + self.dict_5[d1].strip("(").strip(")").split(',')[0] + "," + self.dict_5[d1].strip("(").strip(")").split(',')[1] + ")"

   # print "}"

  #  print "E {"
    c0=0
    for d2 in self.list_10:
      if c0==len(self.list_10)-1:
        if int(d2[0])!=0 and int(d2[1])!=0:
        #  print "<"+str(int(d2[0]))+","+str(int(d2[1]))+">,"
          s1="<"+str(int(d2[0]))+","+str(int(d2[1]))+">,"
          s3+=s1
      else:
        if int(d2[0])!=0 and int(d2[1])!=0:
       #   print "<"+str(int(d2[0]))+","+str(int(d2[1]))+">,"
          s2="<"+str(int(d2[0]))+","+str(int(d2[1]))+">,"
          s3+=s2
          c0+=1
          
  #  print " }"
    s4="E {"+s3+"}"
    s4=s4[:len(s4)-2]+s4[len(s4)-1:]
    print s4
    sys.stdout.flush()

object_1=Generate_streets()
object_1.dictionnary()
object_1.addInput()
