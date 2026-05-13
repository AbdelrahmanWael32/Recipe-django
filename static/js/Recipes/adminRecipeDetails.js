let all_instructions_div = document.querySelector("#all_instructions");
let all_ingredients_div  = document.querySelector("#all_ingredients");
let addInstructionBtn    = document.querySelector("#add_instruction");
let addIngredientBtn     = document.querySelector("#add_ingredient");
let recipeImg            = document.querySelector("#recipe_img");
let imgPreview           = document.querySelector("#img-preview");
let saveRecipeBtn        = document.querySelector("#save_recipe");

function reorder_instructions() {
  let rows = all_instructions_div.children;
  for (let i = 0; i < rows.length; i++) {
    let input         = rows[i].children[0];
    input.placeholder = `Step ${i + 1}`;
  }
}

function reorder_ingredient() {
  let rows = all_ingredients_div.children;
  for (let i = 0; i < rows.length; i++) {
    let input         = rows[i].children[0];
    input.placeholder = `Ingredient ${i + 1}`;
  }
}

function add_delete_event(delete_btn) {
  delete_btn.addEventListener("click", () => {
    let main_parent = delete_btn.parentElement.parentElement;
    if (main_parent.children.length === 1) {
      delete_btn.previousElementSibling.value = "";
    } else {
      delete_btn.parentElement.remove();
      reorder_instructions();
      reorder_ingredient();
    }
  });
}

function createInstructionRow() {
  let div = document.createElement("div");
  div.className = "flexbox flex-row gap-small";
  div.innerHTML = `
    <input name="instructions" class="width-100" type="text" placeholder="Step" />
    <button class="delete-btn" type="button">Delete</button>
  `;
  add_delete_event(div.querySelector(".delete-btn"));
  return div;
}

function createIngredientRow() {
  let div = document.createElement("div");
  div.className = "flexbox flex-row gap-small";
  div.innerHTML = `
    <input name="ingredients" class="width-100" type="text" placeholder="Ingredient" />
    <button class="delete-btn" type="button">Delete</button>
  `;
  add_delete_event(div.querySelector(".delete-btn"));
  return div;
}

document.querySelectorAll(".delete-btn").forEach((btn) => {
  add_delete_event(btn);
});

addInstructionBtn.addEventListener("click", () => {
  all_instructions_div.appendChild(createInstructionRow());
  reorder_instructions();
});

addIngredientBtn.addEventListener("click", () => {
  all_ingredients_div.appendChild(createIngredientRow());
  reorder_ingredient();
});

function updatePreview() {
  imgPreview.src = recipeImg.value.trim();
}

function showError(element) {
  let warning = element.parentElement.querySelector(".warning");
  if (warning) warning.hidden = false;
}

function clearError(element) {
  let warning = element.parentElement.querySelector(".warning");
  if (warning) warning.hidden = true;
}

saveRecipeBtn.addEventListener("click", () => {
  let isValid = true;

  let recipe_name         = document.querySelector("#recipe_name");
  let course_type         = document.querySelector("#course_type");
  let cooking_time        = document.querySelector("#cooking_time");
  let selected_difficulty = document.querySelector("#selected_difficulty");
  let recipe_img_input    = document.querySelector("#recipe_img");

  if (!recipe_name.value.trim()) {
    showError(recipe_name); isValid = false;
  } else { clearError(recipe_name); }

  if (!course_type.value) {
    showError(course_type); isValid = false;
  } else { clearError(course_type); }

  if (!cooking_time.value.trim()) {
    showError(cooking_time); isValid = false;
  } else { clearError(cooking_time); }

  if (!selected_difficulty.value) {
    showError(selected_difficulty); isValid = false;
  } else { clearError(selected_difficulty); }

  if (!recipe_img_input.value.trim()) {
    showError(recipe_img_input); isValid = false;
  } else { clearError(recipe_img_input); }

  for (let i = 0; i < all_instructions_div.children.length; i++) {
    if (!all_instructions_div.children[i].children[0].value.trim()) {
      showError(all_instructions_div); isValid = false; break;
    } else { clearError(all_instructions_div); }
  }

  for (let i = 0; i < all_ingredients_div.children.length; i++) {
    if (!all_ingredients_div.children[i].children[0].value.trim()) {
      showError(all_ingredients_div); isValid = false; break;
    } else { clearError(all_ingredients_div); }
  }

  if (!isValid) return;

  document.querySelector('form').submit();
});