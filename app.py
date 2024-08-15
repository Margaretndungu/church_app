from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Common church data
churches_data = [
    {'name': 'PEFA KIMBO', 'location': 'Githurai Progressive'},
    {'name': 'PEFA CATHEDRAL', 'location': 'Githurai 44'},
    {'name': 'PEFA CLAYCITY', 'location': 'Clay city'},
    {'name': 'PEFA MWIHOKO', 'location': 'Mwihoko'},
    {'name': 'PEFA FINANCE', 'location': 'Finance'},
    {'name': 'PEFA INFINITY', 'location': 'Infinity'},
    {'name': 'PEFA GIKOMBA', 'location': 'Gikomba'},
    {'name': 'PEFA THIKA ROAD', 'location': 'Roysambu'},
    {'name': 'PEFA CATHEDRAL', 'location': 'Ruiru'},
    {'name': 'PEFA KAHAWA WEST', 'location': 'Kahawa West'}
]

# Sample data
messages = [
    {
        "title": "Sunday Service",
        "time": "10:00 AM",
        "details": "Join us for our Sunday morning service.",
        "live_stream_link": "https://example.com/live"
    },
    {
        "title": "Bible Study",
        "time": "7:00 PM",
        "details": "Weekly Bible study session."
    }
]

events = {
    "2024-06-15": "Church Picnic",
    "2024-06-20": "Youth Group Meeting",
    "2024-06-25": "Bible Study"
}

# Dummy function to simulate database storage
def save_to_database(name, email, prayer_request):
    # Implement database storage logic here
    # For demonstration, we'll print the data to console
    print(f"Saving Prayer Request: Name={name}, Email={email}, Request={prayer_request}")

# Dummy function to simulate fetching prayer requests from database
def fetch_prayer_requests_from_database():
    # Implement database fetching logic here
    return [
        "Please pray for healing for my father.",
        "I'm struggling with anxiety; please pray for peace.",
        "Pray for my job interview next week."
    ]

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/live_streams')
def live_streams():
    recorded_videos = [
        "https://www.facebook.com/HeavenBoundTelevision/videos/1112178270001562/",
        "https://www.facebook.com/HeavenBoundTelevision/videos/966031691721426/",
        "https://www.facebook.com/HeavenBoundTelevision/videos/991404645888098/",
        "https://www.facebook.com/HeavenBoundTelevision/videos/26412845441662322/",
        "https://www.facebook.com/HeavenBoundTelevision/videos/1091970125222209/",
        "https://www.facebook.com/HeavenBoundTelevision/videos/405002749023904/",
        "https://www.facebook.com/HeavenBoundTelevision/videos/1634622340409623/"
    ]
    return render_template('live_streams.html', recorded_videos=recorded_videos)

@app.route('/churches')
def churches():
    return render_template('churches.html', churches=churches_data)

@app.route('/page4')
def page4():
    return render_template('page4.html', messages=messages, events=events)

@app.route('/events')
def events_page():
    return render_template('events.html', events=events)

@app.route('/donation_form')
def donation_form():
    return render_template('donation_form.html')

@app.route('/first_time_guests')
def first_time_guests():
    return render_template('first_time_guests.html')

@app.route('/prayer_request', methods=['GET', 'POST'])
def prayer_request():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        prayer_request = request.form.get('prayer_request')

        # Process the prayer request (e.g., store in database)
        save_to_database(name, email, prayer_request)

        # Redirect to a thank you page or render another template
        return redirect(url_for('thank_you'))

    # Fetch previously submitted prayer requests
    prayer_requests = fetch_prayer_requests_from_database()

    return render_template('prayer_request.html', prayer_requests=prayer_requests)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/who_are_we')
def who_are_we():
    return render_template('who_are_we.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

# JSON endpoint for churches data
@app.route('/api/churches')
def get_churches():
    return jsonify(churches_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


