"""..."""
from snowflake.snowpark.session import Session
import streamlit as st


class _SnowparkSessionWrapper:
    """
    snowpark session wrapper
    """

    def __init__(self):
        self._connection: Session = None

    def create_or_get_connection(self, _connection_parameters: dict) -> Session:
        """
        entry point to manage snowpark connection
        :param _connection_parameters: informations to connect to snowflake
        :return: snowpark Session
        """
        if not self.is_active():
            self._connection = self._create_or_get_connection(_connection_parameters)
        return self._connection

    def is_active(self) -> bool:
        """
        check snowpark connection
        :return: true if connection is active otherwise false
        """
        if self._connection is None:
            return False

        try:
            test = self._connection.sql("select 'Connected!' as status").collect()
        except Exception:
            return False

        return True

    def _create_or_get_connection(self, _connection_parameters: dict) -> Session:
        """
        check snowpark connection
        :param _connection_parameters: informations to connect to snowflake
        :return: snowpark Session
        """
        return Session.builder.configs(_connection_parameters).create()

    def get_connection(self) -> Session:
        """
        get the snowpark connection
        :return: snowpark Session
        """
        return self._connection

    def __del__(self):
        """
        class destructor -> close session if needed
        """
        if self._connection is not None:
            self._connection.close()


def create_or_get_snowpark_session(_connection_parameters: dict) -> _SnowparkSessionWrapper:
    """
    create or get snowpark session.
    :param _st_secret_name:
    :return: snowpark Session
    """

    @st.experimental_singleton
    def get_connection(_connection_parameters) -> _SnowparkSessionWrapper:
        snowpark_session = _SnowparkSessionWrapper()
        snowpark_session.create_or_get_connection(_connection_parameters)
        return snowpark_session

    return get_connection(_connection_parameters).create_or_get_connection(_connection_parameters)
