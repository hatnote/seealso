/*!
 * fitColumns layout mode for Isotope
 * v1.1.2
 * http://isotope.metafizzy.co/layout-modes/fitcolumns.html
 */

/*jshint browser: true, devel: false, strict: true, undef: true, unused: true */

( function( window ) {

'use strict';

function fitColumnsDefinition( LayoutMode ) {

  var FitColumns = LayoutMode.create('fitColumns');

  FitColumns.prototype._resetLayout = function() {
    this.x = 0;
    this.y = 0;
    this.maxX = 0;
  };

  FitColumns.prototype._getItemLayoutPosition = function( item ) {
    item.getSize();

    // if this element cannot fit in the current row
    if ( this.y !== 0 && item.size.outerHeight + this.y > this.isotope.size.innerHeight ) {
      this.y = 0;
      this.x = this.maxX;
    }

    var position = {
      x: this.x,
      y: this.y
    };

    this.maxX = Math.max( this.maxX, this.x + item.size.outerWidth );
    this.y += item.size.outerHeight;

    return position;
  };

  FitColumns.prototype._getContainerSize = function() {
    return { width: this.maxX };
  };

  FitColumns.prototype.needsResizeLayout = function() {
    return this.needsVerticalResizeLayout();
  };

  return FitColumns;

}

if ( typeof define === 'function' && define.amd ) {
  // AMD
  define( [
      'isotope/js/layout-mode'
    ],
    fitColumnsDefinition );
} else if ( typeof exports === 'object' ) {
  // CommonJS
  module.exports = fitColumnsDefinition(
    require('isotope-layout/js/layout-mode')
  );
} else {
  // browser global
  fitColumnsDefinition(
    window.Isotope.LayoutMode
  );
}

})( window );