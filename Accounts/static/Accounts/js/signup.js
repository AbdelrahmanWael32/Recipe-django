const radioButtons = document.querySelectorAll('input[name="is_admin"]');
const roleLabels = document.querySelectorAll(".role-option");

radioButtons.forEach(function (radio) {
  radio.addEventListener("change", function () {
    roleLabels.forEach(function (label) {
      label.classList.remove("selected");
    });
    this.closest(".role-option").classList.add("selected");
  });
});

document.getElementById("signup-form").addEventListener("submit", function (event) {
  const selectedRole = document.querySelector('input[name="is_admin"]:checked');
  if (!selectedRole) {
    event.preventDefault();
    alert("Please select Account Type");
    return;
  }
});