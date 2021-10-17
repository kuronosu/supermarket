// var $searchResults, $form, $searchInput, $productsList;
var searchTimer,
  oldSearchLen = 0;
const $form = document.getElementById("create_invoice_form");
const $searchInput = document.getElementById("search_product");
const $searchResults = document.getElementById("search_results");
const $productsList = document.getElementById("products_list");

function onFormSubmit(e) {
  e.preventDefault();
  const $form = e.target;
  const csrftoken = $form.csrfmiddlewaretoken.value;
  let data = Object.fromEntries(new FormData($form));
  let [products, error] = getAddedProducts();
  if (error) {
    alert(error);
    return;
  }
  if (products.length <= 0) {
    alert("Add at least 1 product");
    return;
  }
  data.products = products;
  fetch($form.action, {
    method: "POST",
    mode: "same-origin",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(data),
  })
    .then((res) => {
      if (res.ok) {
        res.json().then((data) => {
          let nextUrl = document.location.pathname;
          if (!document.location.href.endsWith("/")) {
            nextUrl += "/";
          }
          nextUrl += `${data.invoice}/`;
          document.location.pathname = nextUrl;
        });
      } else if (res.status == 400) {
        res.json().then((data) => alert(data.errors));
      }
    })
    .catch((err) => alert(err));
}

function getAddedProducts() {
  let products = [];
  for (let it of $productsList.children) {
    try {
      let quantity = parseInt(
        document.getElementById(`product_${it.dataset.id}`).value
      );
      if (quantity <= 0) {
        return [
          [],
          "Invalid quantity of product " + it.firstElementChild.innerText,
        ];
      }
      products.push({
        id: parseInt(it.dataset.id),
        quantity,
      });
    } catch (error) {}
  }
  return [products, null];
}

function searchProduct(query) {
  let url = "/api/products/search/?";
  url += new URLSearchParams({ name: query }).toString();
  fetch(url)
    .then((res) => res.json())
    .then((data) => showProducts(data.products))
    .catch((e) => ($searchResults.innerHTML = "error" + e));
}

function clearProductsSearch() {
  $searchResults.innerHTML = "";
}

function onSearchInputChange(e) {
  clearTimeout(searchTimer);
  $searchResults.innerHTML = "...";
  searchTimer = setTimeout(() => searchProduct(e.target.value), 300);
}

function showProducts(products) {
  clearProductsSearch();
  products.forEach((product) => {
    $container = document.createElement("div");
    $container.classList.add("search-result-element");
    $name = document.createElement("span");
    $name.innerText = `${product.name.capitalize()}: ${"$"}${product.price}`;
    $button = document.createElement("button");
    $button.classList.add("btn", "btn-outline-dark", "btn-sm");
    $button.innerText = "Add";
    $button.addEventListener("click", (e) => {
      addProduct(product);
      $searchInput.focus();
    });
    $container.appendChild($name);
    $container.appendChild($button);
    $searchResults.appendChild($container);
  });
}

function addProduct(product) {
  for (let it of $productsList.children) {
    if (it.dataset.id == product.id) {
      return;
    }
  }
  $container = document.createElement("li");
  $container.dataset.id = product.id;
  $container.classList.add("product-item");
  $name = document.createElement("label");
  $name.htmlFor = `product_${product.id}`;
  $name.innerText = product.name.capitalize();
  $name.classList.add("p-3");
  $input = document.createElement("input");
  $input.classList.add("form-control");
  $input.type = "number";
  $input.value = 1;
  $input.id = `product_${product.id}`;
  $input.addEventListener("input", (e) => {
    if (e.target.value <= 0) {
      e.target.value = 1;
    }
  });
  $container.appendChild($name);
  $container.appendChild($input);
  $productsList.appendChild($container);
}

String.prototype.capitalize = function () {
  return this[0].toUpperCase() + this.slice(1).toLowerCase();
};

(() => {
  $form.addEventListener("submit", onFormSubmit);
  $searchInput.addEventListener("input", onSearchInputChange);
})();
