import gviz_api
import datetime
import mraa
import time
import sys
import math



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
    <H1>Temperature from Intel Edison</H1>
    <div id="table_div_jscode"></div>
  </body>
</html>
"""
#    <H1>Table created using ToJSon</H1>
#    <div id="table_div_json"></div>
def main():
    tempSensor_pin_number = 1
 
    # Configuring the switch and temperature Sencor as GPIO interfaces
    tempSensor = mraa.Aio(tempSensor_pin_number)
 
    # Configuring the switch and buzzer as input & output respectively
    reading = tempSensor.read()
    r = 100000*(float(1023/float(reading)) - 1)
    temperatureC = (1/(math.log(r/100000.0)/4275 + (1/298.15))) - 273.15
    tempStr = "%.4f" % temperatureC

    # Creating the data
    description = {"current_time": ("string", "Current Time"),
                   "temperature": ("string", "Temperature"),
                   "unit": ("string", "Temperature Unit")}
    data = [{"current_time": str(datetime.datetime.now()), "temperature": tempStr, "unit": "Degree Celcius"}]

    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Create a JavaScript code string.
    jscode = data_table.ToJSCode("jscode_data",
                                 columns_order=("current_time", "temperature", "unit"),
                                 order_by="temperature")
    # Create a JSON string.
    json = data_table.ToJSon(columns_order=("current_time", "temperature", "unit"),
                             order_by="temperature")

    # Put the JS code and JSON string into the template.
    print "Content-type: text/html"
    print
#    print page_template % vars()
    f = file('polls/templates/polls/index2.html', 'w+')
    f.write(page_template % vars())
    f.close()
if __name__ == '__main__':
  main()




