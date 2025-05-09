/** @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    setup() {
        super.setup(...arguments);
        this.changePos(this.pos);
	}, 

    changePos(pos){
        // Crear un MutationObserver para observar cambios en el DOM
        const observer = new MutationObserver(() => {            
            this.active_invoice_all_time();
        });
        
        // Observar cambios en el DOM dentro del contenedor principal
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    },

    active_invoice_all_time(){
        const invoice_button = document.querySelector('.js_invoice');
        if(invoice_button){
            //ocultar el boton siempre
            if(invoice_button && invoice_button.style.display === ''){
                // Verifica si el botón existe y no tiene las clases "highlight" o "text-bg-primary"
                if (invoice_button && !invoice_button.classList.contains('highlight') && !invoice_button.classList.contains('text-bg-primary')) {
                    console.log("active invoice");
                    //invoice_button.click();
                    const event = new MouseEvent('click', {
                        view: window,
                        bubbles: true,
                        cancelable: true
                    });
                    invoice_button.dispatchEvent(event);
                }
                //ocultar el boton siempre
                console.log("hide button invoice");
                //invoice_button.setAttribute('style', 'display: none !important;');
            }
        }
    }
});