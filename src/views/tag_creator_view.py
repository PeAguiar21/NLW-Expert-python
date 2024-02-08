from src.views.http_types.http_request import HttpResquest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    '''
        responsability for interacting with HTTP

    '''

    def validade_and_create(self, http_request: HttpResquest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        formatted_response =  tag_creator_controller.create(product_code)

        # retorno http
        return HttpResponse(status_code=200, body=formatted_response)
