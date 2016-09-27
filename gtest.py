import gviz_api

page_template = """
<html>
  <script src="https://www.google.com/jsapi" type="text/javascript"></script>
  <script>
    google.load('visualization', '1', {packages:['table']});

    google.setOnLoadCallback(drawTable);
    function drawTable() {
      %(jscode)s
      var jscode_table = new google.visualization.Table(document.getElementById('table_div_jscode'));
      jscode_table.draw(jscode_data, {showRowNumber: true});

      var json_table = new google.visualization.Table(document.getElementById('table_div_json'));
      var json_data = new google.visualization.DataTable(%(json)s, 0.6);
      json_table.draw(json_data, {showRowNumber: true});
    }
  </script>
  <body>
    <H1>Table created using ToJSCode</H1>
    <div id="table_div_jscode"></div>
    <H1>Table created using ToJSon</H1>
    <div id="table_div_json"></div>
  </body>
</html>
"""
def main():
    # Creating the data
    description = {"indicator": ("string", "Indicator"),
                   "city_name": ("string", "City Name"),
                   "timestamp": ("string", "Timestamp"),
                   "temperature": ("string", "Temperature"),
                   "unit": ("string", "Temperature Unit")}
    data = [{"indicator": "Source", "city_name": "", "timestamp": "", "temperature": "", "unit": "Degree Celcius"},
            {"indicator": "Destination", "city_name": "", "timestamp": "", "temperature": "", "unit": "Degree Celcius"}]

    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Create a JavaScript code string.
    jscode = data_table.ToJSCode("jscode_data",
                                 columns_order=("indicator", "city_name", "timestamp", "temperature", "unit"))
    # Create a JSON string.
    json = data_table.ToJSon(columns_order=("indicator", "city_name", "timestamp", "temperature", "unit"))

    # Put the JS code and JSON string into the template.
    print "Content-type: text/html"
    print
    print page_template % vars()
    f = file('city/route/templates/route/temperature.html', 'w+')
    f.write(page_template % vars())
    f.close()
if __name__ == '__main__':
  main()
