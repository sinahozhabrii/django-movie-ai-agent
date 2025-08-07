
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.postgres import PostgresStore
from dec



DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"

store = PostgresStore.from_conn_string(DB_URI)
checkpointer = PostgresSaver.from_conn_string(DB_URI)
