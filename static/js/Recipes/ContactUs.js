function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showNotification(message, type) {
  const old = document.querySelector(".form-notification");
  if (old) old.remove();
  const note = document.createElement("div");
  note.className = `form-notification ${type}`;
  note.textContent = message;
  document.querySelector(".contact-right").append(note);
  setTimeout(() => {
    note.style.opacity = "0";
    setTimeout(() => note.remove(), 500);
  }, 4000);
}

document.addEventListener("DOMContentLoaded", () => {
  const serverNotification = document.querySelector(".form-notification");
  if (serverNotification) {
    setTimeout(() => {
      serverNotification.style.opacity = "0";
      setTimeout(() => serverNotification.remove(), 500);
    }, 3000);
  }

  const form = document.querySelector(".contact-form");
  form.addEventListener("submit", (e) => {
    const name    = form.name.value.trim();
    const email   = form.email.value.trim();
    const message = form.message.value.trim();
    if (!name || !email || !message) {
      e.preventDefault();
      showNotification("Please fill in all fields.", "error");
      return;
    }
    if (!isValidEmail(email)) {
      e.preventDefault();
      showNotification("Please enter a valid email address.", "error");
      return;
    }
  });
});