window.onload = () => {
    const user = eel.gud()().then((user) => {
        var name = document.getElementById("username")
        name.innerHTML = user.user.username
        console.log(user)

    })
    
}