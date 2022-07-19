const $menu = document.querySelector(".menu");
const $btnMenu = document.querySelector(".menu-btn"),
	$menuBg = document.querySelector(".bg-");

$btnMenu.addEventListener("click", () => {
	$btnMenu.firstElementChild.classList.toggle("none");
	$btnMenu.lastElementChild.classList.toggle("none");
	$menu.classList.toggle("inBottom");
	$menuBg.classList.toggle("isActive");
});

/* document.addEventListener("click", () => {
	if ($menu.classList.contains("inBottom")) $menu.classList.remove("inBottom");
});
 */
document.addEventListener("click", (e) => {
	if (e.target == $menuBg || e.target.matches(".menu a") || e.target.matches(".menu h2")) {
		$btnMenu.firstElementChild.classList.add("none");
		$menuBg.classList.remove("isActive");
		$btnMenu.lastElementChild.classList.remove("none");
		$menu.classList.remove("inBottom");
	}
});
