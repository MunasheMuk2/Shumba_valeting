// Wait for the page to load
document.addEventListener("DOMContentLoaded", function() {
    // Get the messages div
    var messagesDiv = document.getElementById("messages");
    
    if (messagesDiv) {
        // Read the messages from the data attribute and split by "|"
        var messages = messagesDiv.dataset.messages.split("|");
        
        // Loop through each message
        for (var i = 0; i < messages.length; i++) {
            var msg = messages[i].trim();
            if (msg) {
                // Show a pop-up alert for each message
                alert(msg);
            }
        }
    }
});