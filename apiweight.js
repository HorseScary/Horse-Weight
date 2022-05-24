window.onload = function () {
    document.getElementById("ign").addEventListener("keydown", function(key) {
        if (key.code == "Enter") {
            calc()
        }
    })
}

function calc() {
    console.log(getProfiles("horsescary"))
} 

function getProfiles(name) {
    fetch(`https://sky.shiiyu.moe/api/v2/profile/${name}`)
    .then(response => response.json())
    .then(data => profileData = (data))
//    let profiles = await fetch (`https://sky.shiiyu.moe/api/v2/profile/${name}`)
//    return(await profiles.text)
    return(profileData)
}