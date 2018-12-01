<template>
  <div
    v-swiper:swiper="swiperOption"
    ref="swiperBox"
    class="swiper swiperBox"
    @mouseenter="stopSwiper"
    @mouseleave="startSwiper"
  >
    <div class="swiper-wrapper">
      <div
        v-for="(banner,i) in banners"
        :key="i"
        class="swiper-slide">
        <img :src="banner">
      </div>
    </div>
    <div
      slot="pagination"
      class="swiper-pagination"></div>
    <div
      slot="button-prev"
      class="swiper-button-prev"></div>
    <div
      slot="button-next"
      class="swiper-button-next"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      banners: [
        "1.jpg",
        "2.jpg"
      ],
      // 所有配置均为可选（同Swiper配置）
      swiperOption: {
        loop: true,
        speed: 50,
        // notNextTick是一个组件自有属性，如果notNextTick设置为true，组件则不会通过NextTick来实例化swiper，也就意味着你可以在第一时间获取到swiper对象，假如你需要刚加载遍使用获取swiper对象来做什么事，那么这个属性一定要是true
        notNextTick: true,
        slidesPerView: "auto",
        centeredSlides: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        },
        on: {
          slideChange() {
            // console.log('onSlideChangeEnd', this);
          },
          tap() {
            // console.log('onTap', this);
          }
        },
        autoplay: {
          delay: 5000,
          disableOnInteraction: false
        },
        autoplayDisableOnInteraction: false,
        // effect:'cube',
        mousewheel: true,
        preloadImages: false,
        lazy: true
      }
    }
  },
  swiper() {
    // 如果你需要得到当前的swiper对象来做一些事情，你可以像下面这样定义一个方法属性来获取当前的swiper对象，同时notNextTick必须为true
    return this.$refs.swiperBox.swiper;
  },
  methods: {
    stopSwiper() {
      this.swiper.autoplay.stop();
    },
    startSwiper() {
      this.swiper.autoplay.start();
    }
  }
}
</script>

<style>
  .swiper-pagination-bullet-active {
    background-color: #41b883!important;
  }
</style>

