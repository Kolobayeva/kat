
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, BatchType,SimpleStatement
from cassandra import ConsistencyLevel


cluster = Cluster()
session = cluster.connect('keyspace1')

session.execute("SELECT user_id, user_name, event_data from keyspace1.user_event where event_id=1;")
session.execute("SELECT temperature, seasonality from keyspace1.event_clothers where options_id=1;")
session.execute("SELECT user_name, style,outwear,lowerwear,shoes from keyspace1.clothers_options where style_id=1;")
session.execute("SELECT count_of_version from keyspace1.clothers_options where  options_id=1;")


