<template>
    <div>
        <li @click="onVideoClick" class="list-group-item">
            <img :src="thumbnailUrl" class="mr-3" :alt="video.snippet.title">
            <!-- bind 해야지 alt 에서 불러올 수 있다.  -->
            <div class="media-body">
                <span v-html="video.snippet.title"></span>
            </div>
            
           
        </li>
    </div>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
        video: Object,
    },
    methods: {
        onVideoClick () {
            this.$emit('videoSelect', this.video)  // video 객체 자체를 올려보낸다. 
        }
    },
    computed: {
        thumbnailUrl () {
            return this.video.snippet.thumbnails.default.url
        }
    }
}
</script>

<style scoped>
    li {
        display: flex;
        cursor: pointer;
    }    
    li:hover { 
        /* 커서가 올라갔을 때  */
        background-color: #eee;
    }
</style>