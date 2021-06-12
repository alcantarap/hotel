

// Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='registration']").validate({
        // Specify validation rules
        rules: {
          Nombre: "required",
          Apellidos: "required",
          Nom_usu: "required",
          correo: {
            required: true,
            // Specify that email should be validated
            // by the built-in "email" rule
            email: true
          },
          con_correo: {
            required: true,
            // Specify that email should be validated
            // by the built-in "email" rule
            email: true
          },
                  
          Num: {
            required: true,
            minlength: 9,
            digits: true
          },
          contraseña1: {
            required: true,
            minlength: 8,
            digits: true
          },
          contraseña2: {
            required: true,
            minlength: 8,
            digits: true
          },
  
        },
  
        // Specify validation error messages
        messages: {
          Nombre: "Por favor ingrese su nombre",

          Apellidos: "Por favor ingrese su apellido",
          Nom_usu: "Por favor indique su nombre de usuario",
          Num: {
            required: "Por favor ingrese su numero",
            minlength: "El numero debe tener un minimo de 9 digitos",
            digits: "Por favor ingrese solo numeros"
          },
          
          correo:  "Por favor ingrese un correo valido",
          con_correo:  "Los correos no coinciden",

          contraseña1: "Constraseña de 8 caracteres",
          contraseña2: "Las constraseñas no coinciden"
        },     
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
          form.submit();
        }     
      });