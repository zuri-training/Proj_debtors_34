const imgWrap = document.querySelector(".img");
let img = document.createElement("img");
img.src; //equate this to the src value of the school image
if (img.src == ''){
    img.src = 'design_resources/dashboard user image.png';
}

img.style.width = "100%";
imgWrap.appendChild(img)

let contendersMesage;
// contendersMesage.push("usersMessage") //remove userMessage and use the actual value

let butt;
let inb =  document.querySelector(".inbox")

//looping through the contenders messages DB
for (let x of contendersMesage){
    butt = document.createElement("button");
    butt.innerHTML = x;
    butt.setAttribute("class", "inboxMsg")
    inb.appendChild(butt)

    //onclick function for messages
    butt.onclick = function(e){
        e.preventDefault()
        chatInterface()
    }
}

//chat interface
function chatInterface(){
    let msgSection = document.querySelector(".msgbox");
    let msgWrap = document.createElement("div")
    msgWrap.setAttribute("class", "wrap")
    let mesgBox = document.createElement("div");
    let stdId = document.createElement("div");
    stdId.setAttribute("class", "stdId");
    let std = document.createElement("div");
    std.setAttribute("class", "std");
    let stdImg = document.createElement("img");
    stdImg.src; //equate to the src value of the student
    let stdName = document.createElement("span");
    stdName.innerHTML = "student name"; //replace this with the variable name of the the student
    let chat = document.createElement("div");
    let close = document.createElement("a");
    close.setAttribute("href", "javascript:void(0)")
    close.setAttribute("class", "close")
    close.innerHTML = "X";
    chat.setAttribute("class", "chatBox");
    mesgBox.setAttribute("class", "mesgBox");
    let inpWrap = document.createElement("div");
    let idWrap = document.createElement("div")
    inpWrap.setAttribute("class", "inputWrap");
    let inputBox = document.createElement("input");
    inputBox.setAttribute("class", "input");
    inputBox.setAttribute("placeholder", "Enter message");
    let sendButton = document.createElement("button")
    sendButton.setAttribute("class", "msgBox");
    let sendIcon = document.createElement("img")
    sendButton.appendChild(sendIcon)
    sendIcon.src = "design_resources/Email send.svg"
    let uploadButton = document.createElement("button")
    uploadButton.setAttribute("class", "msgBox");
    let uploadIcon = document.createElement("img")
    uploadButton.appendChild(uploadIcon)
    uploadIcon.src = "design_resources/Upload to cloud.svg";
    idWrap.appendChild(stdImg);
    idWrap.appendChild(stdName);
    stdId.appendChild(idWrap)
    stdId.appendChild(close)
    chat.appendChild(stdId)
    chat.appendChild(mesgBox);
    chat.appendChild(inpWrap);
    inpWrap.appendChild(uploadButton);
    inpWrap.appendChild(inputBox);
    inpWrap.appendChild(sendButton);
    msgWrap.appendChild(chat)
    msgSection.appendChild(msgWrap)
    sendButton.style.outline = 'none'
    inputBox.style.width = "65%"
    inputBox.style.height = "40px"
    sendButton.style.width = "30px"
    sendButton.style.backgroundColor = "#fff"
    uploadButton.style.backgroundColor = "#fff"
    sendButton.style.height = "30px"
    uploadButton.style.width = "30px"
    sendIcon.style.width = "100%"
    uploadIcon.style.width = "100%"
    inputBox.style.outline = '#fff';
    idWrap.style.gap = '10px';
    stdImg.style.width = "30px";



    //closing the chat interface
    close.onclick = function(e){
        e.preventDefault();
        msgWrap.style.display = "none";
    }

    //creating a messsage.
    function create(Msg, messageBody, type='receive'){
        let msgBox = document.createElement("div");
        msgBox.setAttribute("class", "box");
        let text = document.createElement("div");
        let textcont = document.createElement("div");
        textcont.setAttribute("class", "textcont");
        if (type == "receive"){
            text.style.color= 'black';
            text.style.float = 'left';
            text.setAttribute('class', 'contender');
        } else {
            text.style.color= 'black';
            text.setAttribute('class', 'school');
            text.style.float = 'right';
        }
        textcont.appendChild(text);
        msgBox.appendChild(textcont);
        mesgBox.appendChild(msgBox);
        text.innerHTML = Msg;
    }

    //receiving a message
    function receive(msg){
        create(msg, mesgBox, 'receive')
    }

    for (let i of contendersMesage){
        for (let k of i){
            receive(k);
        }
    }
    
    //replying a message
    function reply(msg){
        create(msg, mesgBox, "reply")
    }
    
    //send button
    sendButton.onclick = function(e){
        e.preventDefault();
        let userMsg = inputBox.value;
        if (inputBox.value.trim().length != 0){
            reply(userMsg);
        }
        inputBox.value = '';
    }
}