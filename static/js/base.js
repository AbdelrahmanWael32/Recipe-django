const dropdownBtn = document.querySelector(".dropdown-toggle");
const dropdownMenu = document.querySelector(".dropdown-menu");
if (dropdownBtn && dropdownMenu) {
  dropdownBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdownBtn.classList.toggle("dropMenuIsOpen");
    dropdownMenu.classList.toggle("hidden");
  });
  document.addEventListener("click", () => {
    dropdownMenu.classList.add("hidden");
    dropdownBtn.classList.remove("dropMenuIsOpen");
  });
}