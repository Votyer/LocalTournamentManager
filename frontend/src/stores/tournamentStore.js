import {defineStore} from 'pinia'

export const useTournamentStore = defineStore('tournament', {
    state: () => ({
        name: '',
        code: '',
        tables: [],
        players: []
    }),
    actions: {
        resetTournament() {
            this.name = ''
            this.code = ''
            this.tables = []
            this.players = []
        },
        setTournament(tournament) {
            this.name = tournament.name
            this.code = tournament.code
            this.tables = tournament.tables
            this.players = tournament.players
        }
    }
})

