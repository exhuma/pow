from flask import Flask, request
from flask_restful import Resource, Api

from powonline.core import (
    make_dummy_team_dict,
    make_dummy_station_dict,
    make_dummy_route_dict,
)


class TeamList(Resource):

    def get(self):
        output = {
            'items': [
                make_dummy_team_dict(name='team2'),
                make_dummy_team_dict(name='team1'),
                make_dummy_team_dict(name='team3'),
            ]
        }
        return output

    def post(self):
        new_team = request.get_json()
        return new_team, 201


class Team(Resource):

    def put(self, name):
        output = make_dummy_team_dict(name=name)
        output.update(request.get_json())
        return output

    def delete(self, name):
        return '', 204

class StationList(Resource):

    def get(self):
        output = {
            'items': [
                make_dummy_station_dict(name='station2'),
                make_dummy_station_dict(name='station1'),
                make_dummy_station_dict(name='station3'),
            ]
        }
        return output

    def post(self):
        new_station = request.get_json()
        return new_station, 201


class Station(Resource):

    def put(self, name):
        output = make_dummy_station_dict(name=name)
        output.update(request.get_json())
        return output

    def delete(self, name):
        return '', 204

class RouteList(Resource):

    def get(self):
        output = {
            'items': [
                make_dummy_route_dict(name='route2'),
                make_dummy_route_dict(name='route1'),
                make_dummy_route_dict(name='route3'),
            ]
        }
        return output


    def post(self):
        new_route = request.get_json()
        return new_route, 201


class Route(Resource):

    def put(self, name):
        output = make_dummy_route_dict(name=name)
        output.update(request.get_json())
        return output

    def delete(self, name):
        return '', 204


def make_app():
    '''
    Application factory
    '''
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(TeamList, '/team')
    api.add_resource(Team, '/team/<name>')
    api.add_resource(StationList, '/station')
    api.add_resource(Station, '/station/<name>')
    api.add_resource(RouteList, '/route')
    api.add_resource(Route, '/route/<name>')
    return app
