$(document).ready(function() { 

	$("#buscar-vehiculo").click(function(){
		if($("#id_patente").val() != ""){
			var patente = $("#id_patente").val();
			$.get("/gestion/obtener_vehiculo/"+patente+"/",function(data){
		        if(data.length>0){
		        	$("#buscar-vehiculo").hide();
		        	alerta = $("#alert");
		        	alerta.show();
		        	alerta.append("<p class='alert alert-warning'>El Vehiculo que intenta cargar ya existe, por favor seleccione cargar trabajo.</p>");	
		        }else{
		        	$("#buscar-vehiculo").hide();
		        	alerta = $("#alert");
		        	alerta.show();
		        	alerta.append("<p class='alert alert-warning'>No hay datos del vehiculo buscado.<br>Puede cargar uno nuevo.</p>");
		        	$("#carga").show();

		        }
		    },"json");
		}else{
			alert("No ingreso numero de patente.");
			$("#id_patente").focus();
		}
	});

	$("#id_vehiculo").select2({
	  placeholder: "Elija un vehiculo",
	  allowClear: true
	});

}); 

