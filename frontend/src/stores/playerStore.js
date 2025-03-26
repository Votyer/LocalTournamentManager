import {defineStore} from "pinia";

export const usePlayerStore = defineStore('player', {
    state: () => ({
        name: '',
        player_id: ''
    }),
    actions: {
        register_player(player){
            this.name = player.name
            this.player_id = player.player_id
        }
    }
})