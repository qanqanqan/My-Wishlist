function overlogo() {
    if (document.getElementsByClassName("logo-text").length == 0) {
        const newDiv = document.createElement("div");
        const newContent = document.createTextNode("Hoo");

        const currentDiv = document.getElementById("logo-wrapper");

        newDiv.classList.add('logo-text');
        newDiv.appendChild(newContent);

        currentDiv.appendChild(newDiv);
    }
}

function outlogo() {
    const foundDivs = document.getElementsByClassName('logo-text');
    if (foundDivs.length != 0) {
        const foundDiv = foundDivs[0];
        foundDiv.remove();
    }
}