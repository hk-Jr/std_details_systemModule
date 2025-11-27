import sys

if len(sys.args)==6:
  script_name=sys.argv[0]
  m1=sys.argv[1]
  m2=sys.argv[2]
  m3=sys.argv[3]
  m4=sys.argv[4]
  m5=sys.argv[5]
  print("user details - inputeed")

else:
  print("no input given - Using default Value.")
  script_name=sys.argv[0]
  m1=80
  m2=30
  m3=60
  m4=44
  m5=66

avg=(m1+m2+m3+m4+m5)
print(f"average : {avg}")

if avg>90:
  print("grade: A")
elif avg>80:
  print("grade: B")
elif avg>70:
  print("grade: C")
elif avg>60:
  print("grade: D")
elif avg>50:
  print("grade: E")
else:
  print("grade: Fail")
