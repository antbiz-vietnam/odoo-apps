/** @odoo-module **/

import { rpc } from "@web/core/network/rpc";
import options from "@web_editor/js/editor/snippets.options";
import s_dynamic_snippet_products_options from "@website_sale/snippets/s_dynamic_snippet_products/options";
import { DEFAULT_NUMBER_OF_COL, DEFAULT_NUMBER_OF_COL_SM, DEFAULT_NUMBER_OF_ROW_PER_SLIDE } from "./constants";

const productGridSnippetOptions = s_dynamic_snippet_products_options.extend({
  /**
   * @override
   * @private
   */
  _setOptionsDefaultValues: function () {
    this._super.apply(this, arguments);

    this._setOptionValue("numOfEl", DEFAULT_NUMBER_OF_COL);
    this._setOptionValue("numOfElSm", DEFAULT_NUMBER_OF_COL_SM);
    this._setOptionValue("rowPerSlide", DEFAULT_NUMBER_OF_ROW_PER_SLIDE);
  },
});

options.registry.product_carousel_grid_snippet = productGridSnippetOptions;

export default productGridSnippetOptions;
