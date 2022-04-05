const linkNorthAmerica = document.querySelector('.north-america__link');
const listNorthAmerica = document.querySelector('.north-america__list');
const linkEurope = document.querySelector('.europe__link');
const listEurope = document.querySelector('.europe__list');
const linkAsia = document.querySelector('.asia__link');
const listAsia = document.querySelector('.asia__list');

linkNorthAmerica.onclick = function showList() {
	listNorthAmerica.classList.toggle('map-block');
}
linkEurope.onclick = function showList() {
	listEurope.classList.toggle('map-block');
}
linkAsia.onclick = function showList() {
	listAsia.classList.toggle('map-block');
}
