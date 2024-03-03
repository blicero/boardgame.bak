;;; boardgame.el --- bla
;;; Time-stamp: <2024-03-03 21:34:12 krylon>

;; Copyright (C) 2024 Benjamin Walkenhorst

;; Author: Benjamin Walkenhorst
;; Created: 03. 03. 2024
;; Version: 0.0.1
;; Keywords: krylon Boardgame

;;; Commentary:

;; This program is free software; you can redistribute it and/or
;; modify it under the terms of the GNU General Public License as
;; published by the Free Software Foundation; either version 2 of
;; the License, or (at your option) any later version.

;; This program is distributed in the hope that it will be
;; useful, but WITHOUT ANY WARRANTY; without even the implied
;; warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
;; PURPOSE.  See the GNU General Public License for more details.

;; You should have received a copy of the GNU General Public
;; License along with this program; if not, write to the Free
;; Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
;; MA 02111-1307 USA

;; See www.gnu.org for details or press C-h C-c
;; to display the GPL from within emacs

;;; Code:

(defclass field ()
  ((level
    :initarg :level
    :initform 0
    :type integer
    :documentation "The elevation level of the field")
   (terrain
    :initarg :terrain
    :type symbol
    :documentation "The kind of terrain of the field"))
  "A field on the board")

(defclass coord ()
  ((x
    :initarg :x
    :type integer)
   (y
    :initarg :y
    :type integer))
  "Describes the position of a field or piece on a board")

;; (defclass board ()
;;   ((size
;;     :initarg :size
;;     :type coord
;;     :documentation "The dimensions of the board in fields")
;;    (fields
;;     :initarg :fields


(provide 'boardgame)

;;; boardgame.el ends here
