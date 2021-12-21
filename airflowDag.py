from string import Template


email_temp = {}


body = Template(
  """
    <table>
      <%
      {% for item in [1,2,3,4]: %}
        %>
        <tr>
          <th>Name</th>
          <td><%={% item %} %></td>
        </tr>
        <%
      %>
    </table>

  """
)

# body.substitute(name='thushar')

print(body.substitute(items=['thsuahr', 'someone'])+body.substitute(items=['thsuahr', 'someone']))