function successMoney(result,increaseMoney){
    console.log(result);
    location.href = "./point.html?id=" + result.id + "&count=" + result.count + "&increasemoney=" + increaseMoney + "&userspeed=" + result.speed;
}

async function callMoneyApi(url,increaseMoney) {
    console.log(url);
    fetch(url, {
        mode: 'cors'
    }).then(response => response.json())
      .then(result => {
        successMoney(result,increaseMoney);
    });
};

document.getElementById("money").onclick = function() {
    const locationUrl = new URL(window.location.href);
    const params = locationUrl.searchParams;
    const userId = params.get("id");
    let registerNumMoney = document.getElementById('num_money').value;
    let increaseMoney = Math.floor(registerNumMoney / 100);
    console.log(registerNumMoney);
    const url = 'http://127.0.0.1:8000/register_point/' + userId + '/' +registerNumMoney;
    callMoneyApi(url,increaseMoney);
};
