from jinja2 import Template
data=["Analyst","Developer","Programmer"]

temp='''
        {%for items in data%}
            {{items}}
        {%endfor%}
'''

made_temp=Template(temp)
output=made_temp.render(data=data)
print(output)