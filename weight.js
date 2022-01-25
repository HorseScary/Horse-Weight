function calc() {
    ign = document.form.ign.value.toUpperCase()

    weight = ign.charCodeAt(0) + ign.charCodeAt(2)

    if (ign == "JPERRM") {
        weight = weight * 90.2
    } 
    else if (ign == "HORSESCARY") {
        weight = weight * 191.6
    }
    else {
        weight = weight * 135.7
    }

    document.getElementById("weight").innerHTML = weight
}