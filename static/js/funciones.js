$(document).ready(function() { 

	$("#buscar-vehiculo").click(function(){
		if($("#id_patente").val() != ""){
			var patente = $("#id_patente").val();
			$.get("/gestion/obtener_vehiculo/"+patente+"/",function(data){
		        if(data.length>0){
		        	alerta = $("#alert");
		        	if(alerta.find('p').length == 0){
		        		alerta.append("<p class='alert alert-warning'>El Vehiculo que intenta cargar ya existe, por favor seleccione cargar trabajo.</p>");	
		        		alerta.fadeIn();		        		
		        	}else{
		        		alerta.animate({ 'zoom': 1.2 }, 400);
		        		alerta.animate({ 'zoom': 1 }, 400);
		        		alerta.animate({ 'zoom': 1.2 }, 400);
		        		alerta.animate({ 'zoom': 1 }, 400);
		        	}
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
	$("#id_cliente").change(function(){
		var cliente = $("#id_cliente").find(":selected").text();

		if(cliente !=""){
			$("#id_nuevo-propietario").hide();
		}else{
			$("#id_nuevo-propietario").show();
		}
	});
	$("#id_tbl-cliente-vehiculo").DataTable();
	$("#id_tbl-clientes").DataTable();
	$("#id_tbl-trabajos").DataTable();
	$("#id_tbl-entregados").DataTable();
	$("#tbl_job-history").DataTable();
	$("#id_vehiculo").select2({
	  placeholder: "Elija un vehiculo",
	  allowClear: true
	});
	$("#id_cliente").select2({
	  placeholder: "Elija un cliente",
	  allowClear: true
	});

}); 

