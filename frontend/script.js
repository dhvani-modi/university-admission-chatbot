const chatBody = document.getElementById("chatBody");
const questionInput = document.getElementById("questionInput");
const sendButton = document.getElementById("sendButton");

function addUserMessage(question) {

    const message = document.createElement("div");

    message.className = "message user-message";

    message.innerHTML = `
        <div class="message-content">
            <strong>You</strong>
            <p>${question}</p>
        </div>
    `;

    chatBody.appendChild(message);

    chatBody.scrollTop = chatBody.scrollHeight;
}


function addBotMessage(answer) {

    const message = document.createElement("div");

    message.className = "message bot-message";

    message.innerHTML = `
        <div class="message-icon">
            <i class="bi bi-robot"></i>
        </div>

        <div class="message-content">
            <strong>Admission Assistant</strong>
            <p>${formatAnswer(answer)}</p>
        </div>
    `;

    chatBody.appendChild(message);

    chatBody.scrollTop = chatBody.scrollHeight;
}


function formatAnswer(answer) {

    return answer
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/\n/g, "<br>");
}


function addTypingMessage() {

    const message = document.createElement("div");

    message.className = "message bot-message";
    message.id = "typingMessage";

    message.innerHTML = `
        <div class="message-icon">
            <i class="bi bi-robot"></i>
        </div>

        <div class="message-content">
            <strong>Admission Assistant</strong>
            <p class="typing">Thinking...</p>
        </div>
    `;

    chatBody.appendChild(message);

    chatBody.scrollTop = chatBody.scrollHeight;
}


async function sendQuestion() {

    const question = questionInput.value.trim();

    if (question === "") {
        return;
    }

    addUserMessage(question);

    questionInput.value = "";

    sendButton.disabled = true;

    addTypingMessage();

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        const typingMessage = document.getElementById("typingMessage");

        if (typingMessage) {
            typingMessage.remove();
        }

        if (response.ok) {
            addBotMessage(data.answer);
        } else {
            addBotMessage("Sorry, something went wrong.");
        }

    } catch (error) {

        const typingMessage = document.getElementById("typingMessage");

        if (typingMessage) {
            typingMessage.remove();
        }

        addBotMessage(
            "Unable to connect to the backend. Please make sure the FastAPI server is running."
        );

    }

    sendButton.disabled = false;

    questionInput.focus();
}


sendButton.addEventListener("click", sendQuestion);


questionInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendQuestion();
    }

});