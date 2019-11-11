<template>

    <ul class="col-lg-4 list-group">
        <videoListItem v-for="video in videos" :key="video.etag" :video="video" @videoSelect="onVideoSelect">
        </VideoListItem>
    </ul>

    <!-- etag: 지문과도 같은것, 유일무이하다 --> 
    <!-- <li v-for="video in videos" :key="video.etag"> 
        
        {{ video.snippet.title }} 
    </li>   -->
</template>

<script>
import VideoListItem from './VideoListItem';

export default {
    name: 'VideoList',
    // props 쓰기: step1. props 가 넘어온다고 명시한다. 여러개 넘어올 수 있음! []
    // props 는 data 랑 똑같이 쓸수 있음. props === 물려받은 data 
    props: {  // 배열로 써도 되지만, 객체를 매우 권장.
        videos: Array,  // validation. videos 가 array 인지 먼저 확인! 

    },
    /*
    절대 이렇게 하면 안됨! 
        data() {
        return {
            videos: this.videos
        }
    }
    */
   components: {
       VideoListItem,
   }, 
   methods: {
       onVideoSelect (video) {
           this.$emit('videoSelect', video)
       }
   },


}
</script>

<style>
    
</style>