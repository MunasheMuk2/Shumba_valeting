// Wait until the page loads
window.onload = function() {
    // Get the messages container
    var messageDiv = document.getElementById("messages");
    
    if (messageDiv) {
        // Get all messages from the data attribute
        var messages = messageDiv.dataset.messages.split("|");
        
        // Show each message using an alert
        for (var i = 0; i < messages.length; i++) {
            var msg = messages[i].trim();
            if (msg) {
                alert(msg);
            }
        }
    }
};