import { defineStore } from 'pinia'

//controlador global para la visibilidad del dialogo de autenticacion
export const useUiStore = defineStore('ui', {
  state: () => ({
    showAuthDialog: false
  }),
  actions: {
    openAuthDialog() {
      this.showAuthDialog = true
    },
    closeAuthDialog() {
      this.showAuthDialog = false
    }
  }
})
