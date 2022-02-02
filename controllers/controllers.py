# -*- coding: utf-8 -*-
# from odoo import http


# class ImOdProjectGeolocateBase(http.Controller):
#     @http.route('/im_od_project_geolocate_base/im_od_project_geolocate_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/im_od_project_geolocate_base/im_od_project_geolocate_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('im_od_project_geolocate_base.listing', {
#             'root': '/im_od_project_geolocate_base/im_od_project_geolocate_base',
#             'objects': http.request.env['im_od_project_geolocate_base.im_od_project_geolocate_base'].search([]),
#         })

#     @http.route('/im_od_project_geolocate_base/im_od_project_geolocate_base/objects/<model("im_od_project_geolocate_base.im_od_project_geolocate_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('im_od_project_geolocate_base.object', {
#             'object': obj
#         })
