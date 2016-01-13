import sys
import picklemigrate


class KeyRenameMigrator(picklemigrate.PickleMigrator):

    def __init__(self, db):
        super(KeyRenameMigrator, self).__init__(db)

    def latest_version(self):
        return 1

    def do_single_migration(self, target_version):
        if target_version == 1:
            key_a = self.db.get('key_a')
            if key_a is not None: self.db.set('key_b', 10)
            self.db.rem('key_a')
        else:
            raise Exception('unknown target_version ' + str(target_version))


if __name__ == '__main__':
    db_file = sys.argv[1]
    db = picklemigrate.load_and_migrate(db_file, KeyRenameMigrator)
    db.dump() # Persist migration.
    assert(db.get('key_a') is None)
    assert(db.get('key_b') == 10)
    print("Success.")
