document.getElementById("move_camera").onclick = function() {
    const url = new URL(window.location.href);
    const params = url.searchParams;
    const userId = params.get("id");
    location.href = "./camera.html?id=" + userId;
};

document.getElementById("move_bet").onclick = function() {
    const url = new URL(window.location.href);
    const params = url.searchParams;
    const userId = params.get("id");
    location.href = "./bet.html?id=" + userId;
};

document.getElementById("move_conform").onclick = function() {
    const url = new URL(window.location.href);
    const params = url.searchParams;
    const userId = params.get("id");
    location.href = "./conform.html?id=" + userId;
};