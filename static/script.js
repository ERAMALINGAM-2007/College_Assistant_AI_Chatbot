const chatBox = document.getElementById("chatBox");
const input = document.getElementById("message");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearBtn");

function addMessage(text, type) {

    const div = document.createElement("div");

    div.className = type;

    div.innerHTML = marked.parse(text);

    chatBox.appendChild(div);

    hljs.highlightAll();

    chatBox.scrollTop = chatBox.scrollHeight;

    return div;

}

async function sendMessage() {

    const message = input.value.trim();

    if (message === "")
        return;

    addMessage(message, "user-message");

    input.value = "";

    input.disabled = true;

    sendBtn.disabled = true;

    const loading = addMessage(
        `
<div class="typing">
    <span></span>
    <span></span>
    <span></span>
</div>
`,
        "bot-message"
    );

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    loading.remove();

    addMessage(data.response, "bot-message");

    input.disabled = false;

    sendBtn.disabled = false;

    input.focus();

}

sendBtn.onclick = sendMessage;

input.addEventListener("keydown", function (e) {

    if (e.key === "Enter") {

        sendMessage();

    }

});

clearBtn.onclick = function () {

    chatBox.innerHTML = "";

    addMessage(
`# 👋 Hello!

I'm **College Assistant AI**.

Ask me anything about

- Programming
- DBMS
- AI
- Machine Learning
- Resume
- Interviews`,
"bot-message");

};