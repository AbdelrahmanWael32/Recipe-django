document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const recipeBoxes = Array.from(document.querySelectorAll('.recipe_box'));
  const noResults = document.getElementById('no-results');

  function filterRecipes() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    let matches = 0;

    recipeBoxes.forEach((box) => {
      const name = box.dataset.name || '';
      const course = box.dataset.course || '';
      const difficulty = box.dataset.difficulty || '';
      const match =
        name.includes(searchTerm) ||
        course.includes(searchTerm) ||
        difficulty.includes(searchTerm);

      box.style.display = match ? '' : 'none';
      if (match) {
        matches += 1;
      }
    });

    if (matches === 0) {
      noResults.style.display = 'block';
    } else {
      noResults.style.display = 'none';
    }
  }

  searchInput.addEventListener('input', filterRecipes);
});