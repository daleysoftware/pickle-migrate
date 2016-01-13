import pickledb
import abc


SCHEMA_VERSION = 'schema_version'


class PickleMigrator(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, db):
        self.db = db

    def current_version(self):
        current_version = self.db.get(SCHEMA_VERSION)
        if current_version is None:
            return 0
        else:
            return int(current_version)

    def migrate(self):
        target_version = self.latest_version()
        current_version = self.current_version()
        for v in xrange(current_version + 1, target_version + 1):
            self.do_single_migration(v)
            self.db.set(SCHEMA_VERSION, v)

    @abc.abstractmethod
    def latest_version(self):
        """
        Return the latest version known to the migrator.
        """
        return 0

    @abc.abstractmethod
    def do_single_migration(self, target_version):
        """
        Do a single migration idempotent migration to the `target_version`.
        """
        return


def load_and_migrate(db_file, pickle_migrator_class):
    # Set force save to false, because we don't want to save when we have partially completed a
    # migration.
    db = pickledb.load(db_file, False)
    pickle_migrator_class(db).migrate()
    return db
