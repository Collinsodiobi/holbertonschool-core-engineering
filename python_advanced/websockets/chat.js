const socket = new WebSocket("ws://localhost:8000/ws");
const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("message-input");
const sendBtn = document.getElementById("send-btn");
const statusDiv = document.getElementById("status");

socket.onopen = () => {
    statusDiv.textContent = "Connected";
    statusDiv.className = "status connected";
};

socket.onclose = () => {
    statusDiv.textContent = "Disconnected";
    statusDiv.className = "status disconnected";
};

socket.onmessage = (event) => {
    const msg = document.createElement("div");
    msg.className = "message received";
    msg.textContent = event.data;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
};

function sendMessage() {
    const text = messageInput.value.trim();
    if (text && socket.readyState === WebSocket.OPEN) {
        const msg = document.createElement("div");
        msg.className = "message sent";
        msg.textContent = text;
        messagesDiv.appendChild(msg);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        socket.send(text);
        messageInput.value = "";
    }
}

sendBtn.addEventListener("click", sendMessage);

messageInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});
