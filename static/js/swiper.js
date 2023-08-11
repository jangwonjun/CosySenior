new Swiper('.swiper', {
    autoplay: {
      delay: 1500
    },
    loop: true,
    slidesPerView: 3,
    spaceBetween: 10,
    centeredSlides: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },
    navigation: {
      prevEl: '.swiper-button-prev',
      nextEl: '.swiper-button-next'
    }
  })