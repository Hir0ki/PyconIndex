from orator.migrations import Migration


class CreateEventTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Event') as table:
            table.increments('id')
            table.timestamps()
            table.

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Event')
