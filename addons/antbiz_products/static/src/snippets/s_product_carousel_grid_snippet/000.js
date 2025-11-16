/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { utils as uiUtils } from "@web/core/ui/ui_service";
import { DEFAULT_NUMBER_OF_COL, DEFAULT_NUMBER_OF_COL_SM, DEFAULT_NUMBER_OF_ROW_PER_SLIDE } from "./constants";

const dynamic_snippet_products = publicWidget.registry.dynamic_snippet_products;
const dynamic_snippet_products_cta = publicWidget.registry.dynamic_snippet_products_cta;

const ProductCarouselGridSnippet = dynamic_snippet_products.extend({
    selector: '.s_product_carousel_grid_snippet',

    /**
     * @override
     */
    _getQWebRenderOptions: function () {
        const dataset = this.el.dataset;

        const defaultOptions = this._super.apply(this, arguments);
        const defaultChunkSize = parseInt(dataset.chunkSize);

        const overrideOptions = {
            chunkSize: defaultChunkSize,
        }

        /**
         * Detect if the snippet is displayed as mobile or not
         */
        const isSmall = uiUtils.isSmall();

        /**
         * Get the number of elements to display
         * If the number of elements is not defined in the dataset, use the default value
         */
        let numberOfElements;
        if (isSmall) {
            numberOfElements = parseInt(dataset.numOfElSm) || defaultChunkSize || DEFAULT_NUMBER_OF_COL_SM;
        } else {
            numberOfElements = parseInt(dataset.numOfEl) || defaultChunkSize || DEFAULT_NUMBER_OF_COL;
        }

        /**
         * Get the number of row for display
         */
        let rowPerSlide;
        console.log(`isSmall`, isSmall);
        if (isSmall) {
            rowPerSlide = parseInt(dataset.rowPerSlideSm) || DEFAULT_NUMBER_OF_ROW_PER_SLIDE;
        } else {
            rowPerSlide = parseInt(dataset.rowPerSlide) || DEFAULT_NUMBER_OF_ROW_PER_SLIDE;
        }

        /**
         * Set the number of elements to display
         * If the number of elements is not defined in the dataset, use the default value
         * If the number of records is less than the number of elements, use the number of records
         */
        const numberOfRecords = parseInt(dataset.numberOfRecords);
        overrideOptions.chunkSize = Math.min(numberOfRecords, numberOfElements);
        overrideOptions.rowPerSlide = rowPerSlide

        return Object.assign(
            defaultOptions,
            overrideOptions
        );
    },
});

const ProductCarouselGridSnippetCard = dynamic_snippet_products_cta.extend({});

publicWidget.registry.product_carousel_grid_snippet_cta = ProductCarouselGridSnippetCard;
publicWidget.registry.product_carousel_grid_snippet = ProductCarouselGridSnippet;

export default ProductCarouselGridSnippet;
