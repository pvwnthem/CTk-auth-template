window.onload = () => {
    eel.gud()().then((user) => {
        var name = document.getElementById("username")
        name.innerHTML = user.user.username

    })
    
}

function build() {
    eel.build()().then((data) => {
        alert(data)
        console.log(data)
    })
}