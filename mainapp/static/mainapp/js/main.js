// Fixed header
window.onscroll = function showHeader() {
	let header = document.querySelector('.navbar');
	let blueLogo = document.querySelector('.blueLogo');
	if(window.pageYOffset > 30){
		header.classList.add('navbar_white');
		blueLogo.style.display="block";
	}else{
		header.classList.remove('navbar_white');
	}
}
////For dropdown
//let dropBtn = document.querySelector('.dropbtn')
//let dropdownContent = document.querySelector('.dropdown-content')
//
//
//dropBtn.addEventListener('click', function(params) {
//    dropdownContent.classList.toggle('active')
//})
// Universities slider
const swiper1 = new Swiper('.universities-slider',{
	slidesPerView: 4,
	loop:true,
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
		clickable: true,
	},
	autoplay:{
		delay:1500,
	},
	breakpoints:{
		1146:{
			slidesPerView: 4,
		},
		846:{
			slidesPerView:3,
		},
		550:{
			slidesPerView:2,
		},
		200:{
			slidesPerView:1
		}
	},
	//	pagination:{
	//	el:'.swiper-pagination',
	//	clickable: true,
	//}
});
// Team slider
const swiper2 = new Swiper('.team-slider',{
	slidesPerView:4,
	breakpoints:{
		1184:{
			slidesPerView:4,
		},
		892:{
			slidesPerView:3,
		},
		616:{
			slidesPerView:2,
		},
		300:{
			slidesPerView:1,
		},
	},
});

// Burger menu
const burgerMenu = document.querySelector('.navbar__burger');
const menuList = document.querySelector('.navbar__menu');
const body = document.querySelector('body');
const links = document.querySelectorAll('.navbar__link');
const showFilter = document.querySelector('.btnAside');
const fliterList = document.querySelector('.news-filter');
const asideBurger = document.querySelector('.aside-burger');

for (i = 0; i < links.length; ++i) {
	links[i].onclick = function hideMenu(){
		burgerMenu.classList.toggle('activeBurger');
		menuList.classList.toggle('activeBurger');
		body.classList.remove('lockScroll');
		asideBurger.classList.toggle('hidden');
	}
}
burgerMenu.onclick = function showBurger(){
	this.classList.toggle('activeBurger');
	menuList.classList.toggle('activeBurger');
	body.classList.toggle('lockScroll');
	asideBurger.classList.toggle('hidden');
}
//Show filter
showFilter.onclick = function showFilter(){
	fliterList.classList.toggle('activated');
	body.classList.toggle('lockScroll');
}
