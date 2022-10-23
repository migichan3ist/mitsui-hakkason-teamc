function successPoint(userId){
    location.href = "./index.html?id=" + userId;
}

async function callPontApi(url,userId) {
    console.log(url);
    fetch(url, {
        mode: 'cors'
    }).then(response => response.json())
      .then(result => {
        successPoint(userId);
    });
};

document.getElementById("move_index").onclick = function() {
    const locationUrl = new URL(window.location.href);
    const params = locationUrl.searchParams;
    const userId = params.get("id");
    let increaseSpeed = document.getElementById('num_speed').value;
    console.log(increaseSpeed);
    const url = 'http://127.0.0.1:8000/increase_speed/' + userId + '/' + increaseSpeed;
    callPontApi(url,userId);
};