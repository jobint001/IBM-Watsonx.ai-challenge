from flask import Blueprint, request, jsonify
from app.watson import get_access_token, analyze_text
import requests, os
from pandas import read_csv
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the Smart City Feedback API'})

@main.route('/analyze_feedback', methods=['POST'])
def analyze_feedback():
    data = request.get_json()

    test_data = read_csv("D:\\IBM-Watsonx.ai-challenge\\backend\\app\\dataset.csv")
    comments = list(test_data.comments)
   
    ip=" ".join(comments)
    #print(ip)


    access_token = get_access_token()
    #access_token= os.getenv('ACCESS_TOKEN')

    analysis = analyze_text(ip, access_token)
    #analysis = 'Features Citizens Liked:1. Installation of bike lanes, making commuting by bike safer and more accessible.2. Encouragement of eco-friendly transportation options.3. Improved air quality in areas with bike lanes.4. Increased business for local businesses due to the new bike lanes.5. Safer intersections and clearer right-of-way for cyclists.6. Strategic placement of bike lanes near schools and parks.Features Citizens Did Not Like:1. Inconsistent quality and maintenance of bike lanes across the city.2. Poorly lit bike lanes, making them dangerous for night-time use.3. Insufficient bike racks, forcing cyclists to find alternative parking spots.4. Blocked bike lanes by parked cars and delivery trucks.5. Narrow bike lanes, making it difficult to pass slower cyclists and merge into traffic.6. Lack of clear markings and dedicated traffic signals, causing confusion and accidents.7. Inadequate snow removal from bike lanes, rendering them unusable during winter.8. Limited expansion of bike lanes to residential areas.Best Infrastructure Project to Consider Next:1. Investing in better maintenance and upkeep of existing bike lanes.2. Adding more bike racks around popular destinations and enforcing no-parking zones near schools.3. Improving lighting for night-time use and ensuring continuous bike lanes.4. Providing better signage and signals to prevent accidents and confusion.5. Expanding the network of bike lanes to cover more residential areas and high-traffic areas.6. Adding physical barriers to separate bike lanes from car'
  
    print(analysis)
    return jsonify(analysis)
