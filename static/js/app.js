// static/js/app.js

document.addEventListener("DOMContentLoaded", function() {
    // Get references to menu links and content divs
    var messagesLink = document.getElementById("messages-link");
    var messagesContent = document.getElementById("messages-content");
    var eventsLink = document.getElementById("events-link");
    var eventsContent = document.getElementById("events-content");
    var liveStreamLink = document.getElementById("live-stream-link");
    var liveStreamContent = document.getElementById("live-stream-content");

    // Toggle visibility of messages content
    messagesLink.addEventListener("click", function(event) {
        event.preventDefault();
        messagesContent.classList.toggle("hidden");
    });

    // Toggle visibility of events content
    eventsLink.addEventListener("click", function(event) {
        event.preventDefault();
        eventsContent.classList.toggle("hidden");
    });

    // Toggle visibility of live stream content
    liveStreamLink.addEventListener("click", function(event) {
        event.preventDefault();
        liveStreamContent.classList.toggle("hidden");
    });
});

