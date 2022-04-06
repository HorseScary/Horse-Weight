window.onload = function () {
    document.getElementById("ign").addEventListener("keydown", function(key) {
        if (key.code == "Enter") {
            calc()
        }
    })
}



function calc() {
    ign = document.getElementById("ign").value.toUpperCase()

    weight = ign.charCodeAt(0) + ign.charCodeAt(2)
    if (isNaN(weight)) {
        weight = "put a fucking ign in you fucking bitch"
    }
    else if (ign == "JPERRM") {
        weight = weight * 90.2
    }
    else if (ign == "HORSESCARY") {
        weight = weight * 200.6
    }
    else {
        weight = weight * 135.7
    }

    document.getElementById("weight").innerHTML = weight
}
