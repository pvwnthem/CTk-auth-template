window.onload = () => {
    const user = eel.gud()().then((user) => {
        var name = document.getElementById("name")
        name.innerHTML = user.user.username
        console.log(user)

    })
    
}