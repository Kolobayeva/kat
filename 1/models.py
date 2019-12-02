
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, BatchType,SimpleStatement
from cassandra import ConsistencyLevel


cluster = Cluster()
session = cluster.connect('keyspace1')

session.execute("SELECT user_id, user_name, event_data from keyspace1.user_event where event_id=1;")
session.execute("SELECT temperature, seasonality from keyspace1.event_clothers where options_id=1;")
session.execute("SELECT user_name, style,outwear,lowerwear,shoes from keyspace1.clothers_options where style_id=1;")
session.execute("SELECT count_of_version from keyspace1.clothers_options where  options_id=1;")

class option_clothes():
    def __init__(self, option_id, clothe_id):
        self.option_id = option_id
        self.clothe_id = clothe_id

### DELETE ###
delete_style_name = session.prepare("DELETE FROM clothes WHERE = ?")
session.execute(delete_style_name, ['romantic'])
session.execute(delete_style_name, ['gala'])
session.execute(delete_style_name, ['office'])

delete_ = session.prepare("DELETE FROM clothes WHERE = ?")
session.execute(delete_outwear, ['coat'])
session.execute(delete_outwear, ['dress'])
session.execute(delete_outwear, ['t-shirt'])

delete_option_id = session.prepare("DELETE FROM options WHERE = ?")
session.execute(delete_option_id, ['1'])
session.execute(delete_option_id, ['2'])
session.execute(delete_option_id, ['3'])

delete_clothe_id = session.prepare("DELETE FROM clothe WHERE = ?")
session.execute(delete_clothe_id, ['1'])
session.execute(delete_clothe_id, ['2'])
session.execute(delete_clothe_id, ['3'])

