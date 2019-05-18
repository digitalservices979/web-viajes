function soloNumeros (e) {
	var key = e.KeyCode || e.which;
	var teclado = String.fromCharCode(key);
	var numero = "0123456789";
	var especiales ="8-37-38-46";
	var teclado_especial = false;

	for (var i in especiales){
		if(key==especiales[i]){
			teclado_especial = true;
		}
	}

	if(numero.indexOf(teclado)==-1 && !teclado_especial){
		return false;
	}

}