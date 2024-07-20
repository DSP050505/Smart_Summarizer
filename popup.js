document.addEventListener('DOMContentLoaded', function() {
    const summarizeButton = document.getElementById('summarize-btn');
    const resultDiv = document.getElementById('result');

    if (summarizeButton && resultDiv) {
        summarizeButton.addEventListener('click', function() {
            const youtubeUrl = document.getElementById('youtube-url').value;
            if (youtubeUrl) {
                chrome.runtime.sendMessage({ action: 'generateSummary', url: youtubeUrl }, function(response) {
                    if (response && response.summary) {
                        resultDiv.innerText = response.summary;
                    } else {
                        resultDiv.innerText = 'Failed to get summary.';
                    }
                });
            } else {
                resultDiv.innerText = 'Please enter a YouTube URL.';
            }
        });

        chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
            if (request.action === 'outputSummary') {
                resultDiv.innerText = request.summary;
            }
        });
    } else {
        console.error('Required elements not found.');
    }
});



  