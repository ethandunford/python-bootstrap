
def get_schema() -> str:
    return """
    system_user:
        id:                             serial primary key
        email:                          text
        first_name:                     text
        last_name:                      text
        password:                       text
        type:                           text
        active:                         boolean
        reset_token:                    text
        date_added:                     timestamp
        last_updated:                   timestamp
    """