function logohandler() {
    const foundDivs = document.getElementsByClassName('logo-text');
    if (document.getElementsByClassName("logo-text").length == 0) {
        const newDiv = document.createElement("div");
        const newContent = document.createTextNode("Hoo");

        const currentDiv = document.getElementById("logo-wrapper");

        newDiv.classList.add('logo-text');
        newDiv.appendChild(newContent);

        currentDiv.appendChild(newDiv);
    }
    else {
        foundDivs[0].remove();
    }
}

function copy_url_on_click(val) {
    const a = document.getElementById('pub-url-wishlist-' + val);
    navigator.clipboard.writeText(window.location.href + a.innerText);
}