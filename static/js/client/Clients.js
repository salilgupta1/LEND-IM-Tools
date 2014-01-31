var Clients = (function($){
	var delete_client = function(){
    	$("#delete_client>a").on("click", function(){
    		var uuid = $(this).data("uuid");
			var x = confirm("You are about to delete this client are you sure?");
			if(x ===true){
				var form = document.createElement("form");
				form.setAttribute("method","POST");
				form.setAttribute("action","/clients/delete_client/");
				uuid_field = document.createElement("input");
				uuid_field.setAttribute("type",'hidden');
				uuid_field.setAttribute("name","uuid");
				uuid_field.setAttribute("value",uuid);
				form.appendChild(uuid_field);
				form.submit();
				return false;
			}
		});
	},
	create_client = function(){
		$("#id_client_type").on("change",function(){
			if($("#id_client_type").val() == "BTP"){
				$("label[for = id_repayment_time],#id_repayment_time").hide();
				$("label[for = id_loan_amount],#id_loan_amount").hide();
			}
			else{
				$("label[for = id_repayment_time],#id_repayment_time").show();
				$("label[for = id_loan_amount],#id_loan_amount").show();
			}
    	})
	},
	init = function(){
		$(document).ready(function(){
			create_client();
			delete_client();
		});
	};
	return {
		init:init
	};
}(jQuery));

//figure out the delete_client how to send information back to the view for it to make a decision before doing anything