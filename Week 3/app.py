import sys
import csv
if len(sys.argv) != 3:
    print("Usage: python app.py -s <student_id> OR -c <course_id>")
    sys.exit(1)

flag = sys.argv[1]
input_id = sys.argv[2]

if flag not in ['-s', '-c']:
    print("Error: Invalid flag. Use -s for student or -c for course.")
    sys.exit(1)


data=[]
with open("data.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        row['Marks']=int(row['Marks'])
        data.append(row)
    
from jinja2 import Template
if flag=="-s":
    student_data=[row for row in data if row["Student id"]==input_id]
    if not student_data:
        # No matching student found
        error_html = """<!DOCTYPE html>
<html>
  <body>
    <h2>Invalid student or course ID</h2>
  </body>
</html>"""

        with open("output.html",'w') as f:
            f.write(error_html)
        sys.exit(0)

    total=sum(row["Marks"] for row in student_data)
    student_template='''
<!DOCTYPE html>
<html>
  <head><title>Student Details</title></head>
  <body>
    <h2>Student Details</h2>
    <table border="1">
      <tr>
        <th>Student ID</th>
        <th>Course ID</th>
        <th>Marks</th>
      </tr>
      {% for row in student_data %}
      <tr>
        <td>{{ row['Student id'] }}</td>
        <td>{{ row['Course id'] }}</td>
        <td>{{ row['Marks'] }}</td>
      </tr>
      {% endfor %}
      <tr>
        <td colspan="2"><strong>Total</strong></td>
        <td><strong>{{ total }}</strong></td>
      </tr>
    </table>
  </body>
</html>
'''

    template = Template(student_template)
    rendered_html = template.render(student_data=student_data, total=total)

    # Write to output.html
    with open("output.html", "w") as f:
        f.write(rendered_html)