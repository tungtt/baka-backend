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
            'price': 1,
            'qty_on_hand': 3,
            'price_currency': 'ASA'
        }
        return {'data': event_item}, 200  # data and status code

class BiddingEvent(Resource):
    def get(self, event_id=None):
        # get the summary of a specific event
        bidding_summary = {
            'id': event_id,
            'title': 'Title',
            'start_time': '2022-07-02 09:00:00',
            'end_time': '2022-07-02 12:00:00',
            'qty_on_hand': 3,
            'high': 150,
            'low': 1.2,
            'total_biddings': 1000,
            'watching': 1200000
        }
        return {'data': bidding_summary}, 200
    
    def patch(self, event_id=None):
        # start/stop an event
        parser = reqparse.RequestParser()
        parser.add_argument('state', required=True)
        args = parser.parse_args()
        event_info = {
            'id': event_id,
            'state': args['state']
        }
        return {'data': event_info}, 200
    
    def add_item_to_cart(self, event_id=None):
        # as soon as the event ends, freeze the bidding and add the item to the carts of the winners
        return {}, 200

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


class User(Resource):
    def get(self, user_id=None):
        # get a user info
        user_info = {
            'id': user_id,
            'tiki_id': 1234,
            'username': 'tungt3',
            'user_email': 'tung@gmail.com',
            'user_phone': '0947999999'
        }
        return {'data': user_info}, 200
    
    def post(self, user_id=None):
        # create a new user
        parser = reqparse.RequestParser()
        # get the nickname; otherwise, the full name of the user from Tiniapp
        parser.add_argument('username', required=True)
        # get the user's email from Tiniapp
        parser.add_argument('user_email', required=True)
        # get the tiki id of the user
        parser.add_argument('tiki_id', required=True)
        # get the mobile phone of the user from Tiniapp
        parser.add_argument('user_phone', required=True)
        args = parser.parse_args()
        user_info = {
            'id': 123456,
            'tiki_id': 1234,
            'username': 'tungt3',
            'user_email': 'tung@gmail.com',
            'user_phone': '0947999999'
        }
        return {'data': user_info}, 200
    
    def create_user_wallet(self):
        # create a user wallet if the user has none
        return True
    
    def generate_random_airdrop(self):
        # generate a random amount to airdrop to a new user
        return True

class UserWallet(Resource):
    def get(self, user_id=None):
        # get the user wallet info
        user_wallet = {
            'id': user_id,
            'username': 'tungt3',
            'balance': 1500
        }
        return {'data': user_wallet}, 200
    
    def patch(self, user_id=None):
        # add/subtract an amount to the user wallet
        parser = reqparse.RequestParser()
        # get the nickname; otherwise, the full name of the user from Tiniapp
        parser.add_argument('amount', required=True)
        # get the user's email from Tiniapp
        parser.add_argument('reason_id', required=True)
        # get the tiki id of the user
        parser.add_argument('reference', required=True)
        # get the mobile phone of the user from Tiniapp
        parser.add_argument('notes', required=True)
        args = parser.parse_args()
        user_wallet = {
            'id': user_id,
            'username': 'tungt3',
            'balance': 1500,
            'latest_change': args['amount'],
            'reason_id': args['reason_id'],
            'reference': args['reference'],
            'notes': args['notes']
        }
        return {'data': user_wallet}, 200

api.add_resource(User, '/user/<string:user_id>')
api.add_resource(UserWallet, '/user/wallet/<string:user_id>')

if __name__ == "__main__":
    app.run(debug=True)
