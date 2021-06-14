jQuery.validator.addMethod("lettersonly", function(value, element) 
{
return this.optional(element) || /^[a-z ]+$/i.test(value);
}, "Letters and spaces only please");

// Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='registration']").validate({
        // Specify validation rules
        rules: {
          Nombre: 
            {required: true, 
            lettersonly: true} ,
          Apellidos: 
            {required: true, 
            lettersonly: true} ,
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
            email: true,
            equalTo:"#correo"
          },
                  
          Num: {
            required: true,
            minlength: 9,
            digits: true
          },
          contraseña1: {
            required: true,
            minlength: 8
          },
          contraseña2: {
            required: true,
            minlength: 8,
            equalTo:"#contraseña1"

          },
  
        },
  
        // Specify validation error messages
        messages: {
          Nombre: {
            required: "Por favor ingrese su nombre",
            lettersonly: "Solo letras y espacios por favor"
          },

          Apellidos: {
            required: "Por favor ingrese su nombre",
            lettersonly: "Solo letras y espacios por favor"
          },
          Nom_usu: "Por favor indique su nombre de usuario",
          Num: {
            required: "Por favor ingrese su numero",
            minlength: "El numero debe tener un minimo de 9 digitos",
            digits: "Por favor ingrese solo numeros"
          },
          
          correo:  "Por favor ingrese un correo valido",
          con_correo:  "El correo no coincide",

          contraseña1: "Contraseña de  minimo de 8 caracteres",
          contraseña2: "La contraseña no coincide"
        },     
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
          form.submit();
        }     
      });