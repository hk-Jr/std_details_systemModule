import sys

if len(sys.argv)==6:
  script_name=sys.argv[0]
  m1 = int(sys.argv[1])
  m2 = int(sys.argv[2])
  m3 = int(sys.argv[3])
  m4 = int(sys.argv[4])
  m5 = int(sys.argv[5])
  print("user details - inputted")

else:
  print("no input given - Using default Value.")
  script_name=sys.argv[0]
  m1=80
  m2=30
  m3=60
  m4=44
  m5=66

avg=(m1+m2+m3+m4+m5)/5
print(f"average : {avg}")

if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
elif avg >= 50:
    print("Grade: E")
else:
    print("Grade: Fail")
