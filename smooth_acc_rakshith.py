#!/usr/bin/python

import sys

s_displacement = 10
t_time = 2


def smooth_acc(s_displacement,t_time,v_velocity=0):
 print "The smooth acceleration for the given time %f, velocity %f and the displacement %f is" % (t_time,v_velocity,s_displacement)
 a_acceleration=(float)(2*(s_displacement-(v_velocity*t_time)))/(t_time*t_time)
 return a_acceleration


def choose_velocity():
 print "Do you wish to provide velocity. Please enter y or n"
 u_input=raw_input()
 if u_input == "y":
  print "Enter the value for velocity"
  try:
   v_velocity=input()
   a_acc=smooth_acc(s_displacement,t_time,v_velocity);
   return a_acc
  except:
   print "Invalid input, taking velocity = 0"
   a_acc=smooth_acc(s_displacement,t_time);
   return a_acc
 elif u_input == "n":
  print "Default velocity = 0"
  a_acc=smooth_acc(s_displacement,t_time);
  return a_acc
 else:
  print "!!! Invalid input, Try again !!!"
  a_acc1=choose_velocity();
  return a_acc1


def usr_input_time():
  print "Please enter the value of time"
  try:
   t_time=input()
   a_acc=smooth_acc(s_displacement,t_time)
   return a_acc
  except:
   print "Invalid input, taking time = 1"
   t_time=1
   a_acc=smooth_acc(s_displacement,t_time)
   return a_acc



def show_credits_calc():
 print "Name    : Tumkur Nagabhushana, Rakshith"
 print "Poly Id : 0525670"
 a_acc1=usr_input_time();
 return a_acc1


def Complete_prog():
  print "------SMOOTH ACCELERATION CALCULATION--------"
  print "1. Calculate smooth acceleration for system values"
  print "2. Enter time as user input for a 1000 metre racing track with initial starting velocity = 0"
  print "3. Show credits of the user and input time to calculate smooth accleration for the track"
  print "4. Exit"
  print "Enter an option"

  u_inp=raw_input()
  if u_inp == "1":
   print "Calculating smooth acceleration with system values"
   a_acc1=choose_velocity();
   print a_acc1
   Complete_prog();
  elif u_inp == "2":
   print "Calculating smooth accleration with user inputting time" 
   a_acc1=usr_input_time();
   print a_acc1
   Complete_prog();
  elif u_inp == "3":
   print "Show credits and calculate smooth accleration with user inputting time"
   a_acc1=show_credits_calc();
   print a_acc1
   Complete_prog();
  elif u_inp == "4":
   print "Thanks for using the smooth acceleration calculator"
   sys.exit();
  else:
   print "!!! Invalid input, Try again !!!"
   Complete_prog();

##############################################################
Complete_prog();
