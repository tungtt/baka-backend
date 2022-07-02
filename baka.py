from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class BiddingItem(Resource):
    def get(self, event_id=None):
        # get event detail
        event_item = {
            'id': event_id,
            'name': 'Title',
            'description': 'Description',
            'start_time': '2022-07-02 09:00:00',
            'end_time': '2022-07-02 12:00:00',
            'price': 1,
            'price_currency': 'ASA'
        }
        return {'data': event_item}, 200  # data and status code

class BiddingEvent(Resource):
    def get(self, event_id=None):
        # Get the summary of a specific event
        bidding_summary = {
            'id': event_id,
            'title': 'Title',
            'start_time': '2022-07-02 09:00:00',
            'end_time': '2022-07-02 12:00:00',
            'high': 150,
            'low': 1.2,
            'total_biddings': 1000,
            'watching': 1200000
        }
        return {'data': bidding_summary}, 200

class BiddingLeaderboard(Resource):
    def get(self, event_id=None):
        # get the leaderboard of a specific event
        leaderboard = [
            {
                'user_id': 123456,
                'username': 'tungt3',
                'bidding_count': 3,
                'bidding_total': 150,
                'rank': 1
            }
        ]
        return {'data': leaderboard}, 200

class BiddingListing(Resource):
    def get(self):
        # get event listing
        listing_data = [{
            'id': 123456,
            'title': 'Title',
            'start_time': '2022-07-02 09:00:00',
            'end_time': '2022-07-02 12:00:00',
            'high': 150,
            'low': 1.2,
            'total_biddings': 1000,
            'watching': 1200000
        }]
        return {'data': listing_data}, 200  # data and status code

class BiddingUser(Resource):
    def get(self, event_id=None, user_id=None):
        # get the bidding details of a user for a specific resource
        print('BiddingUser > get')
        user_bidding = {
            'event_id': event_id,
            'user_id': user_id,
            'username': 'tungt3',
            'bidding_count': 3,
            'bidding_total': 150,
            'rank': 1
        }
        return {'data': user_bidding}, 200

    def post(self, event_id=None, user_id=None):
        # submit a bidding to a specific resource
        parser = reqparse.RequestParser()
        parser.add_argument('bidding_amount', required=True)
        args = parser.parse_args()
        user_bidding = {
            'event_id': event_id,
            'user_id': user_id,
            'username': 'tungt3 POST',
            'latest_bidding_amount': args['bidding_amount'],
            'bidding_count': 3,
            'bidding_total': 150,
            'rank': 1
        }
        return {'data': user_bidding}, 200
    
    def delete(self, event_id=None, user_id=None):
        # release a bidding after the event ended
        user_bidding = {
            'event_id': event_id,
            'user_id': user_id,
            'username': 'tungt3 DELETE',
            'bidding_count': 3,
            'bidding_total': 150,
            'rank': 1
        }
        return {'data': user_bidding}, 200


api.add_resource(BiddingListing, '/bidding/events')
api.add_resource(BiddingEvent, '/bidding/<string:event_id>')
api.add_resource(BiddingItem, '/bidding/item/<string:event_id>')
api.add_resource(BiddingLeaderboard, '/bidding/leaderboard/<string:event_id>')
api.add_resource(BiddingUser, '/bidding/user/<string:event_id>/<string:user_id>')

if __name__ == "__main__":
    app.run(debug=True)
