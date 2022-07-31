
class LINKS:

    ROOT = "http://automation-test.local"
    ADMIN_LOGIN = f"{ROOT}/wp-admin/?localwp_auto_login=1"

    # BetterDocs Pages
    BD_ALL_DOCS = f"{ROOT}/wp-admin/admin.php?page=betterdocs-admin"
    BD_ALL_DOCS_CLASSIC = f"{ROOT}/wp-admin/edit.php?post_type=docs&bdocs_view=classic"
    BD_ADD_NEW = f"{ROOT}/wp-admin/post-new.php?post_type=docs"
    BD_CATEGORIES = f"{ROOT}/wp-admin/edit-tags.php?taxonomy=doc_category&post_type=docs"
    BD_TAGS = f"{ROOT}/wp-admin/edit-tags.php?taxonomy=doc_tag&post_type=docs"
    BD_QUICK_SETUP = f"{ROOT}/wp-admin/admin.php?page=betterdocs-setup"
    BD_SETTINGS = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings"

    BD_SETTINGS_GENERAL = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#general"
    BD_SETTINGS_LAYOUT = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#layout"
    BD_SETTINGS_DESIGN = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#design"
    BD_SETTINGS_SHORTCODES = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#shortcodes"
    BD_SETTINGS_ADVANCED_SETTINGS = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#betterdocs_advanced_settings"
    BD_SETTINGS_INSTANT_ANSWER = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#betterdocs_instant_answer"
    BD_SETTINGS_LICENSE = f"{ROOT}/wp-admin/admin.php?page=betterdocs-settings#go_license_tab"

    BD_ANALYTICS = f"{ROOT}/wp-admin/admin.php?page=betterdocs-analytics"
    BD_MULTIPLE_KB = f"{ROOT}/wp-admin/edit-tags.php?taxonomy=knowledge_base&post_type=docs"

    # WP Admin Pages
    PLUGINS = f"{ROOT}/wp-admin/plugins.php"
    PLUGINS_ADD_NEW = f"{ROOT}/wp-admin/plugin-install.php"

    USERS = f"{ROOT}/wp-admin/users.php"
    USERS_ALL_USERS = f"{ROOT}/wp-admin/users.php"
    USERS_ADD_NEW = f"{ROOT}/wp-admin/user-new.php"


class USERS:
    # Site Users
    ADMIN = {
        "username": "admin",
        "email": "dev-email@flywheel.local",
        "first_name": "adminf",
        "last_name": "adminl",
        "password": "admin",
        "role": "administrator"
    }

    EDITOR = {
        "username": "editor",
        "email": "wpdabh+editor31jul@gmail.com",
        "first_name": "editorf",
        "last_name": "editorl",
        "password": "pass1234",
        "role": "editor"
    }

    AUTHOR = {
        "username": "author",
        "email": "wpdabh+author31jul@gmail.com",
        "first_name": "authorf",
        "last_name": "authorl",
        "password": "pass1234",
        "role": "author"
    }

    CONTRIBUTOR = {
        "username": "contributor",
        "email": "wpdabh+contributor31jul@gmail.com",
        "first_name": "contributorf",
        "last_name": "contributorl",
        "password": "pass1234",
        "role": "contributor"
    }
