function callAiueo(result){
    console.log(result);
}

function successMoney(result){
    console.log(result);
    location.href = "./point.html?id=" + result.id + "&count=" +result.count;
}

async function callMoneyApi(url) {
    console.log(url);
    fetch(url, {
        mode: 'cors'
    }).then(response => response.json())
      .then(result => {
        successMoney(result);
    });
};

document.getElementById("money").onclick = function() {
    const locationUrl = new URL(window.location.href);
    const params = locationUrl.searchParams;
    const userId = params.get("id");
    let registerNumMoney = document.getElementById('num_money').value;
    console.log(registerNumMoney);
    const url = 'http://127.0.0.1:8000/register_point/' + userId + '/' +registerNumMoney;
    callMoneyApi(url);
};
