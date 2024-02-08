$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li></li>');
  });
});
// When the user clicks on DIV#add_item, a new element LI is added to the list UL.my_list.
