$(document).ready(function() { 
	$("#cumpleanios").ready(function(){
		$.get("/gestion/obtener_cumpleanios/",function(data){
			body = $("#cumples");
			if(data.length>0){
				
				for(var i = 0; i < data.length ; i ++ ){
					body.append("<tr><td>"+data[i]['fields']['nombre']+"</td><td>"+data[i]['fields']['fecha_nacimiento']+"</td><td>"+data[i]['fields']['telefono_numero']+"</td></tr>")
				}
			}else{
				body.append("<tr><td colspan='3'>NO HAY CLIENTES QUE CUMPLAN A&Ntilde;OS EN LOS PR&Oacute;XIMOS 15 D&Iacute;AS.</td></tr>")
			}			
		},"json");
	});
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
	$("#id_fecha_nacimiento").datepicker({
      changeMonth: true,
      changeYear: true,
      dateFormat: 'dd/mm/yy' 
    });
    $("#id_fecha_entrega").datepicker({
      changeMonth: true,
      changeYear: true,
      dateFormat: 'dd/mm/yy' 
    });
    $("#id_fecha_entrega").change(function(){
    	fecha = $("#id_fecha_entrega");

    	dia = fecha.val().substring(0,2);
    	mes = fecha.val().substring(3,5);
    	anio = fecha.val().substring(6,10);

    	fecha_nueva = new Date(mes+"/"+dia+"/"+anio);
    	fecha_actual = new Date();

    	if(fecha_actual<fecha_nueva){
    		fecha.focus();
    		fecha.val('');
    		fecha.addClass('input_error');
    		alert('La fecha de finalizacion del trabajo no puede ser mayor a la fecha actual.');
    	}else{
    		fecha.removeClass('input_error');
    	}

    });
}); 

