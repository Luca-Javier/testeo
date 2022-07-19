((d) => {
	const $btnMenu = d.querySelector(".menu-btn"),
		$menu = d.querySelector(".menu");

	$btnMenu.addEventListener("click", () => {
		$btnMenu.firstElementChild.classList.toggle("none");
		$btnMenu.lastElementChild.classList.toggle("none");
		$menu.classList.toggle("inBottom");
	});
	d.addEventListener("click", (e) => {
		/* si quiero ejecutar solo una cosa no necesito las llaves. Y el return rompe el evento */
		if (!e.target.matches(".menu a") && !e.target.matches(".menu h2")) return false;
		$btnMenu.firstElementChild.classList.add("none");
		$btnMenu.lastElementChild.classList.remove("none");
		$menu.classList.toggle("inBottom");
	});
})(document);
