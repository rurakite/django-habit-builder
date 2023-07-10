$(document).ready(function() {
  function updateHabitProgress(habitId) {
      var completedCount = $('#habit-' + habitId + ' input[type="checkbox"]:checked').length;
      var totalCount = $('#habit-' + habitId + ' input[type="checkbox"]').length;
      var progress = (completedCount / totalCount) * 100;

      $('#habit-' + habitId + ' .progress-bar').css('width', progress + '%');
  }

  // Event listener for checkbox change
  $('input[type="checkbox"]').change(function() {
      var habitId = $(this).closest('tr').attr('id').split('-')[1];
      updateHabitProgress(habitId);
  });

  // Calculate and update progress for each habit on page load
  $('[id^=habit-]').each(function() {
      var habitId = $(this).attr('id').split('-')[1];
      updateHabitProgress(habitId);
  });

  $("td").each(function() {
      if ($(this).html().trim() === "") {
          $(this).html('<i class="bi bi-train-front fs-4"></i>');
      }
  });
});


(function () {
const modal = new bootstrap.Modal(document.getElementById("modal"))

htmx.on("htmx:afterSwap", (e) => {
// Response targeting #dialog => show the modal
if (e.detail.target.id == "dialog") {
modal.show()
}
})

htmx.on("htmx:beforeSwap", (e) => {
// Empty response targeting #dialog => hide the modal
if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
modal.hide()
e.detail.shouldSwap = false
}
})

// Remove dialog content after hiding
htmx.on("hidden.bs.modal", () => {
document.getElementById("dialog").innerHTML = ""
})
})();

(function () {
const toastElement = document.getElementById("toast")
const toastBody = document.getElementById("toast-body")
const toast = new bootstrap.Toast(toastElement, { delay: 3000 })

htmx.on("showMessage", (e) => {
toastBody.innerText = e.detail.value
toast.show()
})
})();

(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (!d.getElementById(id)) {
  js = d.createElement(s);
  js.id = id;
  js.src = 'https://weatherwidget.io/js/widget.min.js';
  fjs.parentNode.insertBefore(js, fjs);
}
})(document, 'script', 'weatherwidget-io-js');






