document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        const userInput = e.target.value;
        if (userInput.trim() !== '') {
            // Add user message to chat history
            addMessageToHistory('You', userInput);

            // Send the message to the backend
            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: userInput })
            })
            .then(response => response.json())
            .then(data => {
                // Add AI response to chat history
                addMessageToHistory('SAGE', data.response);
            });

            // Clear the input field
            e.target.value = '';
        }
    }
});

function addMessageToHistory(sender, message) {
    const chatHistory = document.getElementById('chat-history');
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatHistory.appendChild(messageElement);
    chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to the bottom
}