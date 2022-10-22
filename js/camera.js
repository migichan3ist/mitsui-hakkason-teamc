document.getElementById("move_money").onclick = function() {
    const url = new URL(window.location.href);
    const params = url.searchParams;
    const userId = params.get("id");
    location.href = "./money.html?id=" + userId;
};