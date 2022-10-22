function callAiueo(result){
    console.log(result);
}

function successLogin(result){
    console.log(result);
    location.href = "./index.html?id=" + result.id + "&username=" +result.username;
}

async function callApi(url) {
    console.log(url);
    fetch(url, {
        mode: 'cors'
    }).then(response => response.json())
      .then(result => {
        callAiueo(result.message);
    });
};

async function callLoginApi(url) {
    console.log(url);
    fetch(url, {
        mode: 'cors'
    }).then(response => response.json())
      .then(result => {
        successLogin(result);
    });
};

// document.getElementById("part1").onclick = function() {
//     const url = 'http://127.0.0.1:8000/aiueo';
//     callApi(url);
// };

document.getElementById("login").onclick = function() {
    let createUserName = document.getElementById('username').value;
    console.log(createUserName);
    const url = 'http://127.0.0.1:8000/users_create/' + createUserName;
    callLoginApi(url);
};
