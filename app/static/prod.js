
const { createApp } = Vue;
const CoinsApp = {
    data() {
        return {
            coin: '',
            coins: null
        }
    },
    created() {
        const socket = new WebSocket(`ws://${window.location.host}/ws/crypto/`);
        let _this = this;
        socket.onmessage = function (event) {
            _this.coins = JSON.parse(event.data);
            console.log(_this.coins)
        }
    }

}
createApp(CoinsApp).mount('#app')
