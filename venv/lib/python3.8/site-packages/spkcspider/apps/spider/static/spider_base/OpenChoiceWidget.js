
document.addEventListener("DOMContentLoaded", function(){
  $(".OpenChoiceTarget").selectize({
    create: true,
    delimiter: null,
    plugins: {
      'remove_button': {}
    }
  });
})
