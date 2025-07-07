from jinja2 import Template
name="Sarvan"
age=21
place="Delhi"

#step1
temp="My name is {{name}} , my age is {{age}} and I live in {{place}}"

#step2
made_temp=Template(temp)

#step3 
output=made_temp.render(name=name,age=age,place=place)
print(output)