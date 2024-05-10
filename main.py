import requests
import json
from flask import Flask, request, redirect, render_template_string, render_template
import os
from flask import send_from_directory



app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/", methods=["GET", "POST"])
def site():
  url = "https://www.izmir.art/eventsContent.json?month=&date=&eventType=60253c568db21f41d5e141e4,601d10512a1ad610386f8c94&eventDateRange=0&eventDateRangeStart=&eventDateRangeEnd=&eventLocation=0&priceStatus=0"
  response = requests.get(url)
  data = json.loads(response.text)
  image = []
  title = []
  location = []
  eventType = []
  eventDate = []
  eventTime = []
  link = []
  icon = []
  for i in range(100):
    campaign = data[i]['campaignText']
    if campaign == "Genç Bilet '23":
      if data[i]['eventType']== "Tiyatro":
        print("")
      else:
        title.append(data[i]['title'])
        print(data[i]['title'])
        location.append(data[i]['location'])
        eventType.append(data[i]['eventType'])
        eventDate.append(data[i]['eventDate'])
        eventTime.append(data[i]['eventTime'])
        link.append(f"https://izmir.art{data[i]['eventlink']}")
        image.append(f"https://izmir.art{data[i]['image']}")
        icon.append(f"https://izmir.art{data[i]['icon']}")
  return render_template('slm.html', image=image, title=title, eventType=eventType,eventDate=eventDate,eventTime=eventTime, location=location, link=link, icon=icon)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
