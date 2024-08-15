// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    function toggleContent(contentId) {
        var content = document.getElementById(contentId);

        if (content.classList.contains('active')) {
            // Content is already active, return
            return;
        }

        // Toggle active class for contents
        var contents = document.querySelectorAll('.content');
        contents.forEach(content => content.classList.remove('active'));
        content.classList.add('active');
    }

    // Initially hide the church content
    document.getElementById('church-content').classList.remove('active');

    // Fetch list of churches from Flask backend
    fetch('/churches')
        .then(response => response.json())
        .then(data => {
            var churchList = document.getElementById('church-list');
            data.forEach(church => {
                var li = document.createElement('li');
                li.textContent = church.name + ' - ' + church.location;
                li.addEventListener('click', function() {
                    // Update the active tab to the media tab
                    var mediaTab = document.getElementById('media-tab');
                    var churchTab = document.getElementById('church-tab');
                    mediaTab.classList.add('active');
                    churchTab.classList.remove('active');
                    
                    // Show the media content and hide the church content
                    var mediaContent = document.getElementById('media-content');
                    var churchContent = document.getElementById('church-content');
                    mediaContent.classList.add('active');
                    churchContent.classList.remove('active');
                });
                churchList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching churches:', error));
});

