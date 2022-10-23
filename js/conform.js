document.getElementById("cnform_close").onclick = function() {
    const url = new URL(window.location.href);
    const params = url.searchParams;
    const userId = params.get("id");
    location.href = "./index.html?id=" + userId;
};