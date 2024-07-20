chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'generateSummary') {
        const url = window.location.href;
        fetch(`http://localhost:5000/api/summarize?youtube_url=${encodeURIComponent(url)}`)
            .then(response => response.json())
            .then(data => {
                chrome.runtime.sendMessage({ action: 'outputSummary', summary: data.summary });
            })
            .catch(error => {
                console.error('Error fetching summary:', error);
            });
    }
});


