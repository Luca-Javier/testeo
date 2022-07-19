((d) => {
	const $btnMenu = d.querySelector(".menu-btn"),
		$menu = d.querySelector(".menu"),
		$menuBg = d.querySelector(".menu-bg");

	$btnMenu.addEventListener("click", () => {
		$btnMenu.firstElementChild.classList.toggle("none");
		$btnMenu.lastElementChild.classList.toggle("none");
		$menu.classList.toggle("inBottom");
		$menuBg.classList.toggle("isActive");
	});
	d.addEventListener("click", (e) => {
		/* si quiero ejecutar solo una cosa no necesito las llaves. Y el return rompe el evento. Al final no lo use */
		if (e.target == $menuBg || e.target.matches(".menu a") || e.target.matches(".menu h2")) {
			$btnMenu.firstElementChild.classList.add("none");
			$menuBg.classList.remove("isActive");
			$btnMenu.lastElementChild.classList.remove("none");
			$menu.classList.remove("inBottom");
		}
	});
})(document);
