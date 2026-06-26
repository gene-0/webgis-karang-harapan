document.addEventListener("DOMContentLoaded", function () {
	const sidebar = document.querySelector(".sidebar");
	const mainContent = document.querySelector(".main-content");
	const toggleBtn = document.getElementById("sidebarToggle");

	// Periksa status sidebar sebelumnya dari localStorage
	if (localStorage.getItem("sidebar-collapsed") === "true") {
		sidebar.classList.add("collapsed");
		mainContent.classList.add("expanded");
	}

	if (toggleBtn) {
		toggleBtn.addEventListener("click", function (e) {
			e.preventDefault();

			// Toggle class
			sidebar.classList.toggle("collapsed");
			mainContent.classList.toggle("expanded");

			// Simpan status ke localStorage
			const isCollapsed = sidebar.classList.contains("collapsed");
			localStorage.setItem("sidebar-collapsed", isCollapsed);

			// Trigger refresh untuk peta Leaflet (minimap) jika ada, agar ukurannya menyesuaikan grid baru
			if (typeof minimap !== "undefined") {
				setTimeout(() => {
					minimap.invalidateSize();
				}, 300);
			}
		});
	}

	// Menutup sidebar otomatis di layar mobile jika di-klik di luar sidebar
	document.addEventListener("click", function (event) {
		const isClickInside =
			sidebar.contains(event.target) || toggleBtn.contains(event.target);
		if (
			!isClickInside &&
			window.innerWidth <= 768 &&
			!sidebar.classList.contains("collapsed")
		) {
			sidebar.classList.add("collapsed");
			mainContent.classList.add("expanded");
		}
	});
});
