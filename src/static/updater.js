function update_values(msg){
    var json = JSON.parse(msg);
    alert(json);
    document.getElementById("temp_cooler").innerHTML = json.temp_cooler;
    document.getElementById("temp_hotside").innerHTML = json.temp_hotside;
    document.getElementById("temp_ambient").innerHTML = json.temp_ambient;
    document.getElementById("temp_target").innerHTML = json.temp_target;
}