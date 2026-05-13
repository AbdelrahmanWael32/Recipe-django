let addInstructionBtn = document.querySelector("#add_instruction");
let addIngredientBtn = document.querySelector("#add_ingredient");
let addRecipeBtn = document.querySelector("#add_recipe");
let recipeName = document.querySelector("#recipe_name");
let courseType = document.querySelector("#course_type");
let difficulty = document.querySelector("#selected_difficulty");
let recipeImg = document.querySelector("#recipe_img");
let cooking_time = document.querySelector("#cooking_time");
let all_ingredients_div = document.querySelector("#all_ingredients");
let all_instructions_div = document.querySelector("#all_instructions");

// console.log(addInstructionBtn);
// console.log(addIngredientBtn);
// console.log(addRecipeBtn);
// console.log(recipeName);
// console.log(courseType);
// console.log(difficulty);
// console.log(recipeImg);
// console.log(cooking_time);
// console.log(all_ingredients_div);
// console.log(all_instructions_div);

function reorder_instructions() {
  let all_instructions = all_instructions_div.children;
  for (let i = 0; i < all_instructions.length; i++) {
    let instruction = all_instructions[i];
    let inputBtn = instruction.children[0];
    inputBtn.id = `instruction_${i + 1}`;
    inputBtn.placeholder = `Step ${i + 1}`;
  }
}

function reorder_ingredient() {
  let all_ingredient = all_ingredients_div.children;
  for (let i = 0; i < all_ingredient.length; i++) {
    let ingredient = all_ingredient[i];
    let inputBtn = ingredient.children[0];
    inputBtn.id = `ingredient_${i + 1}`;
    inputBtn.placeholder = `Ingredient ${i + 1}`;
  }
}

function add_delete_event(delete_btn) {
  delete_btn.addEventListener("click", () => {
    let main_parent = delete_btn.parentElement.parentElement;

    if (main_parent.children.length == 1) {
      delete_btn.previousElementSibling.value = "";
    } else {
      delete_btn.parentElement.remove();
      reorder_instructions();
      reorder_ingredient();
    }
  });
}

addInstructionBtn.addEventListener("click", () => {
  let instruction_count = all_instructions_div.children.length;
  let new_instruction = `<div class="flexbox flex-row gap-small">
              <input
                id="Instruction_${instruction_count + 1}"
                class="width-100"
                type="text"
                placeholder="Step ${instruction_count + 1}"
                name="instructions"
              />
              <button class="delete-btn" type="button">Delete</button>
            </div>`;
  all_instructions_div.insertAdjacentHTML("beforeend", new_instruction);

  let added_instruction = all_instructions_div.children[instruction_count];
  let delete_btn = added_instruction.children[1];

  add_delete_event(delete_btn);
  reorder_instructions();
});

addIngredientBtn.addEventListener("click", () => {
  let ingredient_count = all_ingredients_div.children.length;
  let new_ingredient = `<div class="flexbox flex-row gap-small">
                <input
                id="ingredient_${ingredient_count + 1}"
                class="width-100"
                type="text"
                placeholder="Ingredient ${ingredient_count + 1}"
                name="ingredients"
                />
                <button class="delete-btn" type="button">Delete</button>
            </div>`;
  all_ingredients_div.insertAdjacentHTML("beforeend", new_ingredient);

  let added_ingredient = all_ingredients_div.children[ingredient_count];
  let delete_btn = added_ingredient.children[1];

  add_delete_event(delete_btn);
  reorder_ingredient();
});

// ADD THE DELETE EVENT LISTENER TO ALL LOADED DELETE BUTTONS
let all_delete_btns = document.querySelectorAll(".delete-btn");
for (let i = 0; i < all_delete_btns.length; i++) {
  add_delete_event(all_delete_btns[i]);
}



/*














Add recipe checking:
*/

function showError(element) {
  let warning = element.parentElement.querySelector(".warning");
  warning.hidden = false;
}

function clearError(element) {
  let warning = element.parentElement.querySelector(".warning");
  warning.hidden = true;
}

addRecipeBtn.addEventListener("click", () => {
  let isAddedRecipeValid = true;

  // Validate recipe name
  if (!recipeName.value.trim()) {
    showError(recipeName);
    isAddedRecipeValid = false;
  } else {
    clearError(recipeName);
  }

  // Validate Course Type
  if (!courseType.value) {
    showError(courseType);
    isAddedRecipeValid = false;
  } else {
    clearError(courseType);
  }

  // Validate Cooking Time
  if (!cooking_time.value.trim()) {
    showError(cooking_time);
    isAddedRecipeValid = false;
  } else {
    clearError(cooking_time);
  }

  // Validate Difficulty
  if (!difficulty.value) {
    showError(difficulty);
    isAddedRecipeValid = false;
  } else {
    clearError(difficulty);
  }

  // Validate Recipe Image
  if (!recipeImg.value.trim() || !recipeImg.value.startsWith("http")) {
    showError(recipeImg);
    isAddedRecipeValid = false;
  } else {
    clearError(recipeImg);
  }

  // Validate **ALL** Recipe instructions
  for (let i = 0; i < all_instructions_div.children.length; i++) {
    let instruction_parent = all_instructions_div.children[i];
    if (!instruction_parent.children[0].value.trim()) {
      showError(all_instructions_div);
      isAddedRecipeValid = false;
      break;
    } else {
      clearError(all_instructions_div);
    }
  }

  // Validate **ALL** Recipe ingredients
  for (let i = 0; i < all_ingredients_div.children.length; i++) {
    let ingredient_parent = all_ingredients_div.children[i];
    if (!ingredient_parent.children[0].value.trim()) {
      showError(all_ingredients_div);
      isAddedRecipeValid = false;
      break;
    } else {
      clearError(all_ingredients_div);
    }
  }

  // FINALY!!!!!!!!!
  // IF EVERYTHING IS VALID SAVE IT
  if (isAddedRecipeValid) {
    document.querySelector('form').submit();
  }
});