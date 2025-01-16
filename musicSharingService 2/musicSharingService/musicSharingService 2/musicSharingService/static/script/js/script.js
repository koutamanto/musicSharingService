document.getElementById("search-button").onclick = () => {
    var searchQuery = document.getElementById("search-text").value;
    location.href = "/search?q=" + searchQuery;
}

document.getElementById("search-text").onkeydown = (ev) => {
    if(ev.key == "Enter") {
        var searchQuery = document.getElementById("search-text").value;
        location.href = "/search?q=" + searchQuery;
    }
}