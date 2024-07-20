chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'generateSummary') {
        const url = request.url;
        fetch(`http://localhost:5000/api/summarize?youtube_url=${encodeURIComponent(url)}`)
            .then(response => response.json())
            .then(data => {
                chrome.runtime.sendMessage({ action: 'outputSummary', summary: data.summary });
                sendResponse({ summary: data.summary });
            })
            .catch(error => {
                console.error('Error fetching summary:', error);
                sendResponse({ summary: 'Error fetching summary.' });
            });
        return true; 
    }
});


  