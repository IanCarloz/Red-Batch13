var age = prompt("¿cuantos años tienes?");
var pais = prompt("¿de que pais eres?");

if(pais == "MX"){
  if (age > 17){
    alert("Si puedes entrar al antro paisano.");
  } else {
    alert("Regresate a tu casa niño mexicano.");
  }
}

if(pais == "US"){
  if (age > 20){
    alert("Si puedes entrar al antro gringo.");
  } else {
  alert("Regresate a tu casa niño gringo.");
  }
}

if(pais == "UK"){
  if (age > 15){
    alert("Si puedes entrar al antro.");
  } else {
  alert("Regresate a tu casa niño.");
  }
}
