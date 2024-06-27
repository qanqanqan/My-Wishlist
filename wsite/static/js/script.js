var diffs = [];

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
    const link = window.location.href + a.innerText;
    navigator.clipboard.writeText(link);
    alert('Copied: ' + link);
}

function add_diff(pk) {
    if (diffs.includes(pk)) {
        diffs = diffs.filter(function (pks) {
            return pks !== pk;
        });
    }
    else {
        diffs.push(pk);
    }
    if (diffs.length != 0) {
        let btn = document.getElementById("shareform-submit-button");
        btn.classList.remove("is-disabled");
        btn.classList.add("is-primary");
        btn.setAttribute("type", "submit");
    }
    else {
        let btn = document.getElementById("shareform-submit-button");
        btn.classList.remove("is-primary");
        btn.classList.add("is-disabled");
        btn.setAttribute("type", "button");
    }
}
